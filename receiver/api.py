import re
from django.db.models import Q
from django.http import JsonResponse
from gateway.rule.model import Rule
from receiver.message.model import Message as MainMessage
from gateway.message.model import Message
from receiver.token.model import Token


def json_response(description=None):
    response = {
        'ok': True
    }

    if description is not None:
        response['ok'] = False
        response['description'] = description

    return JsonResponse(response)


def send_message(request):
    if request.method != 'GET':
        return json_response('Method Not Allowed')

    http_token = request.META.get('HTTP_TOKEN')
    if http_token is None:
        return json_response('Token is required')

    message = request.GET.get('message')
    if message is None:
        return json_response('Message is required')

    token = Token.objects.filter(token=http_token).first()
    if token is None or not token.is_active:
        return json_response('Invalid token')

    message = MainMessage.objects.create(group=token.group, content=message)
    sended = insecure = 0
    for gate in token.group.gate_set.all():
        gate_message = Message.objects.create(message=message, gate=gate, content=message.content)
        rules = Rule.objects.filter((Q(gate__isnull=True) | Q(gate=gate)) & Q(is_active=True))

        for rule in rules:
            if rule.type == Rule.RULE_TYPE_CONTAIN and rule.pattern in gate_message.content:
                gate_message.is_blocked = True
                break
            if rule.type == Rule.RULE_TYPE_REGEX and re.search(rule.pattern, gate_message.content):
                gate_message.is_blocked = True
                break
            if rule.type == Rule.RULE_TYPE_MASK:
                gate_message.content = re.sub(rule.pattern, '***', gate_message.content)

        gate_message.save()

        if gate_message.is_blocked:
            insecure += 1
            continue

        gate_message.gate.chat.send_message(gate_message.content)
        sended += 1

    if insecure > 0:
        return json_response(f'Insecure message{" for some Chat" if sended > 0 else ""}')

    return json_response()
