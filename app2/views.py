from datetime import datetime
from django.shortcuts import render
from app2.models import Message

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        Message.objects.create(title=title, content=content, user=user)
        #* OR
        #* message = Message(title=title, content=content, user=user)
        #* message.save()
    
    context = {}
    #* The '-' in front of 'created_at' means to order the results in descending order.
    context['messages'] = Message.objects.order_by('-created_at')
    return render(request, template_name='index.html', context=context)