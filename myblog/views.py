from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import blog
from .forms import add_form
from django.contrib.auth import authenticate, decorators
from django.views import View


# Create your views here.

def home(request):
    ds_list = blog.objects.all()
    return render(request, 'myblog/../home/templates/home/home.html', {'ds_list': ds_list})


def view(request):
    ds = blog.objects.all()
    return render(request, 'myblog/view.html', {'ds': ds})


class add_content(LoginRequiredMixin, View):
    login_url = '/user/login/'
    def get(request):
        add_title = add_form()
        return request(request, 'myblog/add.html', {'f': add_title})

    def post(request):
            try:
                ds = add_form(request.POST)
                if ds.is_valid():
                    ds.save()
                    return render(request, 'myblog/add_ok.html', status='OK')
                else:
                    return render(request, 'myblog/add_no.html')
            except:
                return HttpResponse('Loi Form')
