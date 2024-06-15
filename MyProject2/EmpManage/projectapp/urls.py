from django.contrib import admin
from django.urls import path, include 
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('contact/',views.contact, name='contact'),
    path('register/',views.register, name='register'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('index/',views.index, name='index'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('filter_emp/<int:emp_id>',views.filter_emp),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>',views.remove_emp),
    path('update_emp', views.update_emp, name='update_emp'),
    path('update_emp1/<int:emp_id>',views.update_emp1),
    path('edit/<int:emp_id>',views.edit),
    path('view_emp', views.view_emp, name='view_emp'),
    # path('accounts/', include('django.contrib.auth.urls')),
    
]