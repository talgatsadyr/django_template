from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from users.forms import AuthenticationForms, RegistrationForm
from users.models import User
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForms(request.POST)
        form.is_valid()
        try:
            user = User.objects.get(password=request.POST.get('password'), email=request.POST.get('email'))
        except User.DoesNotExist:
            return HttpResponse('Неправильный пароль или логин')
        login(request, user)
        return redirect('/files/')  # Перенаправление на главную страницу после успешного входа
    else:
        form = AuthenticationForms()
    return render(request, 'registration/login.html', {'form': form})


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user is not None:
                token = default_token_generator.make_token(user)
                email_message = f'Ваш код подтверждения: {token}'
                send_mail('Восстановление пароля', email_message, 'from@example.com', [email])
                return redirect('password_reset_confirm')
            else:
                form.add_error('email', 'Пользователь с таким адресом электронной почты не существует.')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset.html', {'form': form})


def password_reset_confirm(request):
    token = request.GET.get('token')
    email = request.GET.get('email')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
        return render(request, 'registration/password_reset_confirm.html', {'form': form})
    else:
        return redirect('password_reset_invalid')


def password_reset_invalid(request):
    return render(request, 'registration/password_reset_invalid.html')


def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')