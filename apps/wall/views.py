from django.shortcuts import render, redirect
from apps.login_registration.models import Users
from apps.wall.models import Messages, Comments
def index(request):
    context = {
        'messages' : Messages.objects.all(),
        'user' : Users.objects.get(id=request.session['userid']),
    }
    return render(request, 'wall/index.html', context)

def post(request):
    Messages.objects.create(user_id=Users.objects.get(id=request.session['userid']), message=request.POST['emily'])
    return redirect("/wall")

def comment(request):
    Comments.objects.create(user_id=Users.objects.get(id=request.session['userid']), comment=request.POST['reply'], message_id=Messages.objects.get(id=request.POST['num']))
    return redirect('/wall')