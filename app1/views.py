from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

import logging
logger = logging.getLogger('django')

@login_required(login_url='login_url')
def student_view(request):
    template_name = 'app1/student.html'
    form= StudentForm()
    if request.method =='POST':
        form =StudentForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Student profile created successfully')
        else:
            logger.debug('This is debug log in student_view')
            return redirect('display_url')
    context ={'form':form}
    return render(request,template_name,context)
    
def update_view(request, pk):
    template_name = 'app1/student.html'
    obj = Student.objects.get(sid=pk)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            logger.info('Student profile updated successfully')
        else:
            logger.debug('This is  debug log update_view')
            return redirect('display_url')
    context = {'form': form}
    return render(request, template_name,  context)

def delete_view(request, pk):
    template_name = 'app1/delete.html'
    obj = Student.objects.get(sid=pk)
    if request.method == 'POST':
        obj.delete()
        logger.info('Student profile deleted successfully')
    else:
        logger.debug('This is  debug log in delete_view')
        return redirect('display_url')
    return render(request, template_name)

@login_required(login_url='login_url')
def display_view(request):
    template_name = 'app1/display.html'
    data2 = Student.objects.all()
    context = {'data': data2}
    logger.debug('This is  debug log in display_view')
    return render(request, template_name, context)


