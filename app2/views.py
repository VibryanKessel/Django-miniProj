from datetime import datetime
from django.shortcuts import render

def index(request):
    context = {
        'messages': [{
        'title': 'My Django App',
        'content': 'Welcome to my Django app',
        'created_at': datetime.now()
    },{
        'title': 'Another Django',
        'content': 'Welcome to the other Django app',
        'created_at': datetime.now()
    }]
        }
    return render(request, template_name='index.html', context=context)