from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

#Importing piado_website models
from piadouro_website.models import Piado,Follow
from piadouro_website.forms import FormItemPiado
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User


# Create your views here.
@login_required
def home(request):
  followed_ids = Follow.objects.filter(follower_user=request.user).values_list('followed_user')
  my_piados = Piado.objects.filter(user=request.user).values('user__username','text')
  piados = Piado.objects.filter(user__in=followed_ids).values('user__username','text')
  piados = piados | my_piados
  return render_to_response("piadouro_website/home.html", 
                  { "piados" : piados, 'user':request.user})


@login_required
def mypiados(request):
  return render_to_response("piadouro_website/home.html", 
                  { "piados" : Piado.objects.filter(user=request.user), 'user':request.user})

@login_required
def users(request):
  return render_to_response("piadouro_website/users.html",
                 { "users" : User.objects.all(), "user": request.user} )

@login_required
def profile(request,username):
  #Get the user object
  user = get_object_or_404(User,username=username)
  #Get all piados
  piados = Piado.objects.filter(user=user)
  if 'Follow' in request.GET:
    if request.GET['Follow'] == 'Follow': 
      follow = Follow()
      follow.followed_user = user
      follow.follower_user = request.user
      follow.save()
    else:
      follow = Follow.objects.filter(followed_user__username=username,
                          follower_user=request.user)[0]
      follow.delete()
    return HttpResponseRedirect('/users/'+user.username+'/')
  #See if the user is a follow
  followed= len(Follow.objects.filter(followed_user__username=username,
                                       follower_user=request.user)) > 0
  return render(request,"piadouro_website/profile.html",{'u':user,'piados':piados, 
                                                          'followed': followed,
                                                          'amount_followeds': len(Follow.objects.filter(follower_user__username=username,
                                                                                 follower_user=request.user)),
                                                          'amount_followers': len(Follow.objects.filter(followed_user__username=username,
                                                                                 followed_user=request.user))})


@login_required
def piado_add(request):
  if request.method == 'POST':
    form = FormItemPiado(request.POST,request.FILES)
    if form.is_valid():
      piado = form.save(commit=False)
      piado.user = request.user
      piado.save()
      return HttpResponseRedirect('/')
    else:
      pass
  else:
    form = FormItemPiado()
  return render(request,'piadouro_website/new_piado.html', {'form' : form})
    
