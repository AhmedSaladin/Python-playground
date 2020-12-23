from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req,f'Your account has been created! you are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(req, 'users/register.html', {'form': form})
 