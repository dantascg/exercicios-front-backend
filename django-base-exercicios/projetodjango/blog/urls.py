from django.urls import path
from . import views
from .views import profile_view, login_view, cadastro_view, logout_view, recuperar_view, alterarsenha_view, err404_view, err403_view, err500_view

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('logout/', logout_view, name='logout'),
    path('recuperarsenha/', recuperar_view, name='recuperarsenha'),
    path('alterarsenha/', alterarsenha_view, name='alterarsenha'),
    path('404/', err404_view, name='erro404'),
    path('403/', err403_view, name='erro403'),
    path('500/', err500_view, name='erro500'),

]