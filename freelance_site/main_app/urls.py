from . import views
from django.urls import path

urlpatterns = [path('', views.index, name='index'),
               path('executors/', views.executors, name='executors'),
               path('my_orders/', views.my_orders, name='my_orders'),
               path('profile/', views.profile, name='profile'),
               path('logout/', views.logout_view, name='logout'),
               path('find_orders/', views.find_orders, name='find_orders'),
               path('my_works/', views.my_works, name='my_works'),
               path('login/', views.login_view, name='login'),
               path('register/', views.register, name='register'),
               ]
