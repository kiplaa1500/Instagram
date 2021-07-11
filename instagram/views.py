from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Registration, UpdateUser, UpdateProfile, CommentForm, postImageForm

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(
          request, f'Account for {username} created,you can now login')
      return redirect('login')
  else:
    form = Registration()
  return render(request, 'auth/registration.html', {"form": form})

