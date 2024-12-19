from datetime import datetime
from django.shortcuts import render
from app2.models import Message

def index(request):
    context = {}
    # The '-' in front of 'created_at' means to order the results in descending order.
    context['messages'] = Message.objects.order_by('-created_at')
    return render(request, template_name='index.html', context=context)