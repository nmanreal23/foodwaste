
from django.contrib import admin
from django.urls import path, include, re_path

from foodwaste_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('index/', views.home, name='home'),
    path('list/',views.list_Topics, name='list_Topics'),
    path('details/',views.details_Topics, name='details_Topics'),
    path('datamodel/',views.datamodel, name='datamodel'),
    
    path('details1/',views.details1, name='details1'),
    path('details2',views.details2, name='details2'),
    path('details3/',views.details3, name='details3'),
    path('details4/',views.details4, name='details4'),
    
    path('user_app/', include('django.contrib.auth.urls')),
    path('add/employee/', views.add_employee),
    path('add/employee/done/',views.add_employee_submit, name='add_employee_submit'),
    path('adminuser_login/',views.adminuser_login, name='adminuser_login'),
    path('adminuser_logout/',views.adminuser_logout, name='adminuser_logout'),
    path('employee/',views.read_empinfo, name='empinfo'),
    # re_path(r'^update/employee/(?P<key>\d+)?/?$',views.update_employee),
    path('update/employee/<int:emp_id>/', views.update_employee, name='update'),
    path('delete/employee/<int:emp_id>/', views.delete_employee_rec, name='delete'),
    
]

#Update the page title
admin.site.site_header='Group 5 Administration Page'
admin.site.site_title='Food Waste Audit Tool'