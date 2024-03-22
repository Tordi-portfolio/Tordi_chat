from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import View


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.



def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
     else:
        return render(request, 'login.html')

def join(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        birthday_date = request.POST['birthday_date']
        location = request.POST['location']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('join')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('join')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('join')
    else:
        return render(request, 'join.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


@login_required
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


@login_required
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


@login_required
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


def index(request):
    return render(request, 'index.html')


@login_required
def guild(request):
    return render(request, 'guild.html')


@login_required
def sign_out(request):
    auth.logout(request)
    return redirect('/')
