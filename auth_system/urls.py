from django.urls import path
from .views import Index,DashboardPage, Register, Login, logoutuser,person_create_view,load_cources

urlpatterns = [
    path('', Index, name="index"),
    path('dashboard/', DashboardPage, name="dashboard-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
    path('add/', person_create_view, name='person_add'),
    path('ajax/load-cources/', load_cources, name='ajax_load_cources'), # AJAX
]