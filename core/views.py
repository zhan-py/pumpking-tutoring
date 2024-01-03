from django.shortcuts import render, redirect
from django.contrib.auth import login
from userprofile.forms import UserCreationForm
from userprofile.models import Userprofile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def frontpage(request):
  tutor_users = User.objects.filter(userprofile__is_tutor=True)
  query = request.GET.get('query', '')
  if query:
    tutor_users = tutor_users.filter(Q(username__icontains=query) | Q(userprofile__self_intro__icontains=query) | Q(userprofile__brief_intro__icontains=query))
  return render(request, 'core/frontpage.html', {'tutor_users': tutor_users})


@login_required
def tutor_intro(request, user_id):
  tutor = User.objects.get(pk=user_id)
  return render(request, 'core/tutor_intro.html', {'tutor': tutor})


def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid:
      user = form.save()

      account_type = request.POST.get('account_type', 'tutee')
      if account_type == 'tutor':
        userprofile = Userprofile.objects.create(user=user, is_tutor=True)
        userprofile.save()
      else:
        userprofile = Userprofile.objects.create(user=user)
        userprofile.save()

      login(request, user)
      return redirect('dashboard')
    
  else:
    form = UserCreationForm()

  return render(request, 'core/signup.html', {'form': form})