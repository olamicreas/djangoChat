from django.shortcuts import render, redirect
from .models import Chat
from django.contrib.auth.models import User
from user.models import Profile, Friends 
from online_users.models import OnlineUserActivity
from .forms import MessageForm
from django.http import JsonResponse
from django.contrib import messages
from django.core import serializers
from django.views.generic.list import ListView
import json
from datetime import timedelta, datetime

# Create your views here.
def Chathome(request):

    user = request.user.profile
    friends = Friends.objects.filter(userss=user)
    profile = Profile.objects.filter(user=request.user.id)

    chat = Chat.objects.all()
    unread = Chat.objects.filter(id=user.id, read=False)
    context = {
        'user': user,
        'friends': friends,
        'chat' : chat,
        'profile': profile,
        'unread': unread
    }

    return render(request, 'chathome.html', context)

def detail(request, pk):
    friends = Friends.objects.get(users=pk, userss=request.user.profile)
    user = request.user.profile
    profile = Profile.objects.get(id=friends.users.id)
    chats = Chat.objects.all()
    
    rec_chats = Chat.objects.filter(sender=profile, receiver=user, read=False)
    rec_chats.update(read=True)
    c = len(rec_chats)
    
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.sender = user
            chat_message.receiver = profile
            chat_message.save()
            
            return redirect("detail", pk=friends.users.id)
    context = {"friends": friends, "form": form, "user":user, 
               "profile":profile, "chats": chats, "num": rec_chats.count()}
    return render(request, "chatdetail.html", context)

def sentMessages(request, pk):
    user = request.user.profile
    friend = Friends.objects.get(userss=pk, users=request.user.profile)
    profile = Profile.objects.get(id=friend.userss.id)
    data = json.loads(request.body)
    new_chat = data["msg"]
    new_chat_message = Chat.objects.create(body=new_chat, sender=user, receiver=profile, read=False )
    print(new_chat)
    return JsonResponse(new_chat_message.body, safe=False)

def receivedMessages(request, pk):
    friends = Friends.objects.get(users_id=pk, userss_id=request.user.profile)
    user = request.user.profile
    profile = Profile.objects.get(id=friends.users.id)
    arr = []
    chats = Chat.objects.filter(sender=profile, receiver=user)

    for chat in chats:
        
        arr.append(chat.body)
        
    return JsonResponse(arr, safe=False)

def addFriend(request):
    
    profile = Profile.objects.all()
    
    return render(request, 'add.html', {'profile': profile})
def add(request, pk):
    
    if request.method == 'POST':
        from_user = request.user.profile
        to_user = Profile.objects.get(id=pk)
        
    
        
        Friends.objects.get_or_create(users=from_user, userss=to_user)
        Friends.objects.get_or_create(users=to_user, userss=from_user)

        return redirect('Chathome')

        
    return JsonResponse(profile, safe=False)



    


def accpt(request, pk):
    friend = Friends.objects.get(id=pk)
   
    if friend.userss == request.user.profile: 
       
        friend.userss.friend.add(friend.users)
        friend.users.friend.add(friend.userss)
        friend.delete()
        return redirect('Chathome')
    else:
        print('nah')
        

    return render(request, 'accpt.html', {'friend': friend})

class SearchView(ListView):
    model = User
    template_name = 'add.html'
    context_object_name = 'results'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get('username')
        context['results'] = User.objects.filter(username__icontains=username)
        if context['results'] == self.request.user:
            messages.success('pls search')
        return context


def onlineUsers(request):
    user_activity_objects = OnlineUserActivity.get_user_activities()
    user = request.user.profile
    friends = Friends.objects.filter(userss=user)
    profile = Profile.objects.filter(user=request.user.id)

    chat = Chat.objects.all()
    date = datetime.now()

    context = {
        'user_activity_objects': user_activity_objects,
        'date': date ,
        'user':user,
        'friends': friends,
        'profile': profile
    }


    return render(request, 'online.html', context)
