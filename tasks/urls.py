from django.urls import path
from .views import *

urlpatterns = [
   path('',home_page,name = 'home'),
   path('login/',login_page,name='login'),
   path('signup/',signup_page,name= 'signup'),
   path('task/',task_list,name='task_list'),
   path('task/create/',create_task,name='create_task'),
   path('task/update/<int:id>/',update_task,name='update_task'),
   path('task/delete/<int:id>/',delete_task,name = 'delete_task')
]