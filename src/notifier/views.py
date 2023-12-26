from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Notification

def test(request):
    return render(request, 'notifier/test.html', {"count": Notification.objects.filter(user=request.user, is_seen=False).count(),})


@login_required
def notifications(request):
    current_user = request.user
    channel_layer = get_channel_layer()
    data = Notification.objects.create(user=current_user, text=f"{current_user.name} has been notified")
    
    # Trigger message sent to group
    async_to_sync(channel_layer.group_send)(
        str(current_user.pk),  # Channel Name, Should always be string
        {
            "type": "notify",   # Custom Function written in the consumers.py
            "text": {
                "message": f"{data.text} on {data.created_at}",
                "count": Notification.objects.filter(user=current_user, is_seen=False).count(),
            }
        },
    )
    return render(request, 'notifier/notifications.html')