from django.shortcuts import render
from django.contrib.auth.models import User   
from django.http import HttpResponse, JsonResponse
from .models import Message
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.utils.timesince import timesince
from notifications.models import Notification
from notifications.signals import notify
# Create your views here.
@login_required
def home(request):
    #people=User.objects.all()
    people = request.user.friends_list.all()
    #print(people)
    return render(request,"chat/index.html",{"people":people})
    
def get_message(request):
    username = request.GET["username"]
    #print("------------------+±+++_-------------_------------")
    #print(request.GET)
    ins = User.objects.get(username=username)
    messages = Message.objects.filter(sender=request.user, reciever = ins)|Message.objects.filter(reciever=request.user, sender = ins)
    messages = messages.order_by("timestamp")
    messages=list(messages.values())
    Notification.objects.filter(actor_object_id=ins.id, recipient=request.user,verb="new message").mark_all_as_read()
    #print("message about to be gotten")
    return JsonResponse({"messages": messages})
    
def register(request):    
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=UserRegisterForm()            
    return render(request,"chat/register.html", {"form":form})
    
def mark_specific_as_read(request):
    sender_name =  request.POST["sender"]
    sender =  User.objects.get(username=sender_name).id
    reciever = request.user.id
    n=Notification.objects.filter(actor_object_id = sender,recipient=reciever)
    n.mark_all_as_read() 
    n.delete()
   # print(sender)
#    print(reciever)
#    print(n)
    return HttpResponse("done")
    
def send_message(request):
    print(request.POST)
    sender = request.user
    reciever = request.POST["reciever"]
    msg = request.POST["message"]
    reciever = User.objects.get(username=reciever)
    new_msg = Message.objects.create(sender=sender, reciever=reciever, content=msg)
   # new_msg.save()
    notify.send(sender, recipient=reciever, verb='new message')
    return HttpResponse("done")