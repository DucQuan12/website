from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, decorators
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from User.forms import Singupform
from User.tokens import account_activate_token
from django.core.mail import EmailMessage
from django.conf import settings


class singup(View):
    def get(self, request):
        form1 = Singupform()
        return render(request, 'User/signup.html', {'form': form1})

    def post(self, request):
        form = Singupform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(User.objects.filter(username__exact=user.username))
            print(User.objects.filter(username__exact=user.username).exists())
            if not User.objects.filter(username__exact=user.username).exists() and \
                    not User.objects.filter(email__exact=user.email).exists():
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                subject = 'Active Your Account'
                message = render_to_string('User/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activate_token.make_token(user),
                })
                email = EmailMessage(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                )
                email.fail_silently = False
                email.send()
                return redirect('/user/account_active_sent/')
            else:
                return HttpResponse('Tai khoan da ton tai!')
        else:
            return HttpResponse('Nhap sai khi dang ky!')

class login1(View):
    def get(self, request):
        return render(request, 'User/login.html')

    def post(self, request):
        usename = request.POST.get('username')
        if User.objects.filter(username__exact=usename):
            password1 = request.POST.get('my_password')
            myuser = authenticate(username=usename, password=password1)
            if myuser is not None:
                login(request, myuser)
                return render(request, 'User/home.html', {'myuser': usename})
            return HttpResponse('Mat khau khong dung!')
        else:
            return HttpResponse('Tai khoan khong ton tai!')


def account_active_sent(request):
    return render(request, 'User/account_active_sent.html')


def activate(request, uidbase64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidbase64))
        user = User.objects.get(pk=uid)
    except(ValueError, TypeError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activate_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.is_staff = True
        user.save()
        login(request, user)

        return redirect('/user/login/')
    else:
        return render(request, 'User/account_activation_invalid.html')

@decorators.login_required(login_url='/user/login/')
def home(request):
    return redirect('myblog:view')


class login_view(LoginRequiredMixin, View):
    login_url = '/user/login/'
    def get(self, request):
        return render(request, '')
    def post(self, request):
        pass

