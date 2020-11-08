from django.shortcuts import render

# Create your views here.
def index(request):
    greeting = "Hai! page is working"
    username = request.user.username
    context = {
        'greeting': greeting,
        'username': username, 
    }

    return render(request,'index.html', context = context)

def details(request, username):
    name = request.user.username
    
    context = {
        'name': name, 
    }

    return render(request, 'details.html', context = context)