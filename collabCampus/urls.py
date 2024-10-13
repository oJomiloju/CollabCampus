from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('/login',views.login_user, name='login'),
    path('/logout',views.logout_user, name='logout'),
    path('/register', views.register_user, name='register'),
    path('Projects/<int:pk>', views.project_desc, name='Projects'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
]