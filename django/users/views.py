from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                req, f'Your account has been created! you are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(req, 'users/register.html', {'form': form})


@login_required
def profile(req):
    if req.method == 'POST':
        user_form = UserUpdateForm(req.POST, instance=req.user)
        profile_form = ProfileUpdateForm(req.POST,
                                         req.FILES,
                                         instance=req.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                req, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=req.user)
        profile_form = ProfileUpdateForm(instance=req.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(req, 'users/profile.html', context)
