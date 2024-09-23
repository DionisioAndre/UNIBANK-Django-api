from django.urls import path
from minha_app.views import get_perfis,UserCreateView

urlpatterns = [
    path('', get_perfis, name='get_perfis'),
    path('register/', UserCreateView.as_view(), name='user-register'),
]

