from django.urls import path
from minha_app.views import get_bancos,criarBancos,deletarBanco,put,BancoByNameView,BancoById

urlpatterns = [
    path('get/all',get_bancos, name='get_bancos'),
    path('criar/',criarBancos,name="cradastarBanco"),
    path('deletar/<int:banco_id>/', deletarBanco, name='deletar_banco'),
    path('update/<int:pk>/', put, name='banco-update'),
    path('get/byname/<str:name>/', BancoByNameView.as_view(),name='banco-by-name'),
    path('byid/<int:pk>/', BancoById.as_view(),name='banco-by-id'),
]
