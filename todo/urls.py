from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
app_name = 'todo'  # If using namespaced URLs

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.singleTask, name='singleTask'),  # Added trailing slash
    path('update/<int:id>/', views.updateTask, name='updateTask'),
    path('delete/<int:id>/', views.deleteTask, name='deleteTask'),
    path('register/', views.register, name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    
]
