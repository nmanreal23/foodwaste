from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from foodwaste_app.models import Data_Model_table, Employee_Model

#proj 2
#this is the django authentication system
from django.contrib.auth import authenticate, login, logout
#messages to show when user successfully logged in or logged out
from foodwaste_app.forms import EmployeeRego

# from django.contrib.auth.forms import UserCreationForm

# from .foodwastemodel import Food, Bin, User, Waste

# Create your views here.

def home(request):
    return render(request, 'foodwaste_app/index.html')

# function to populate the title of the items in the list.html
def list_Topics(request):
    topics_data = {
        'topics_list': topic_title()
    }
    return render(request, 'foodwaste_app/list.html', topics_data)

def topic_title():
    the_topics = []
    
    the_topics.append('Reducing Food Waste at Home: Tips and Strategies')
    the_topics.append('Sustainable Food Consumption: Making Informed Choices')
    the_topics.append('Food Waste Segregation')
    the_topics.append('Data Recording: Food Wastage Recording Sheet')
    return the_topics


# function to populate the title of the items in the details.html
def details_Topics(request):
    details_data = {
        'details_list': details_title()
    }
    return render(request, 'foodwaste_app/details.html', details_data)

def details_title():
    the_details = []
    
    the_details.append('Reducing Food Waste at Home: Tips and Strategies')
    the_details.append('Sustainable Food Consumption: Making Informed Choices')
    the_details.append('Food Waste Segregation')
    the_details.append('Data Recording: Food Wastage Recording Sheet')
    return the_details

# function for Featured topic details
def details1(request):
    return render(request,'foodwaste_app/details1.html')

def details2(request):
    return render(request,'foodwaste_app/details2.html')

def details3(request):
    return render(request,'foodwaste_app/details3.html')

def details4(request):
    return render(request,'foodwaste_app/details4.html')

# function for all_data_model_table.html
def datamodel(request):
    results = Data_Model_table.objects.order_by('waste_source_id')
    
    content_data = { 
            'list_data_model_table' : results
    }

    return render(request, 'foodwaste_app/datamodel.html', content_data )

"""
PROJECT 2 Commence Here
"""
def adminuser_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            return redirect('user_login')
    else:
        return render(request, 'foodwaste_app/login.html',{})

def adminuser_logout(request):
    logout(request)
    return redirect('home')

def add_employee(request):
    emp_data = {
        'user_form':EmployeeRego(),
    }
    return render(request,'foodwaste_app/useregistration.html',emp_data)

def add_employee_submit(request):  
    if request.method != 'POST':
        return HttpResponseRedirect('/add/employee/')
    else:
        emp_data = {}
        empform = EmployeeRego(request.POST)
        if empform.is_valid():
            empform.save()
            return HttpResponseRedirect(reverse('home'))
        else:
        #display validation erors
            emp_data = {'value_errors': empform.errors,}

    return render(request, 'foodwaste_app/done.html', emp_data)

def read_empinfo(request):
    list_emp = Employee_Model.objects.order_by('emp_id')

    emp_data = { 
        'emp_list':list_emp 
        }

    return render(request,'foodwaste_app/employeeinfo.html', emp_data)

def update_employee(request, emp_id):

    emp_dets = Employee_Model.objects.get(emp_id=emp_id)
    
    if request.method == 'POST':
        empform = EmployeeRego(request.POST, instance=emp_dets)
        if empform.is_valid() != True:
            emp_data={ 'userform':empform }
        else:
            empform.save()
            return HttpResponseRedirect(reverse('empinfo'))
    else:
        empform = EmployeeRego(instance=emp_dets)
        emp_data = {'user_form':empform}

    return render(request,'foodwaste_app/update_employee.html', emp_data)

def delete_employee_rec(request, emp_id):

    emp_dets = Employee_Model.objects.get(emp_id=emp_id)

    if request.method == 'POST':
        emp_dets.delete()
        return HttpResponseRedirect(reverse('empinfo'))
    else:
        empform = EmployeeRego(instance=emp_dets)
        emp_data = { 'user_form':empform }
    
    return render(request,'foodwaste_app/delete_employee_rec.html', emp_data)