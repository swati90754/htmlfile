from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
import logging
logger = logging.getLogger('django')

# Create your views here.
def register_view(request):
    template_name = 'auth_app/register.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('user sign successfully')
        else:
            logger.error('user sign error')
            return redirect('login_url')
    context = {'form': form}
    return render(request, template_name, context)

def login_view(request):
    template_name = 'auth_app/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(username=un, password=pw)
        if user is not None:
            login(request, user)
            logger.info('user login successfully')
        else:
            logger.error('user login error')
            return redirect('display_url')
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    logger.info('user logout successfully')
    return redirect('login_url')
   
