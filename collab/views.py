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
    if request.user.is_authenticated:
        message = 'Hai, this is ' + username
        
    else:
        message = 'Login to view ' + username +'\'s page'

    context = {
            'name': name, 
            'message': message,
        }

    return render(request, 'details.html', context = context)