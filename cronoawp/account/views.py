from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from cronoawp.account.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from cronoawp.account.models import Profile

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])

        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')

    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form':form})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)

            return render(request,'account/register_done.html', {'new_user':new_user})
    else:

        user_form = UserRegistrationForm()
        return render(request, 'account/register_done.html', {'user_form': user_form})
@csrf_exempt
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST)
        profile_form = ProfileEditForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Perfil editado com sucesso')
        else:
            messages.error(request,'Erro ao atualizar o perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user)

        return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form})
@csrf_exempt
@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request,'account/user/detail.html',{'section':'people', 'user': user})


