from django.shortcuts import render

# Create your views here.
def index(request):
    greeting = "Hai! page is working"
    username = request.user.username

    searched_item = request.GET.get('search_people')
    
    # if not searched_item:
    #     searched_item = "no results found"

    print(searched_item)

    context = {
        'greeting': greeting,
        'username': username,
        'searched_item': searched_item, 
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
            'username': username,
        }

    return render(request, 'details.html', context = context)
