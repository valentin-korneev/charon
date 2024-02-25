from django.http import JsonResponse
from telegram.user.bot.model import Bot


def get_updates(request):
    response = {'ok': True}

    try:
        for bot in Bot.objects.all():
            bot.last_update_id = bot.get_updates()
            bot.save()
    except Exception as e:
        response['ok'] = False
        response['description'] = str(e)

    return JsonResponse(response)
