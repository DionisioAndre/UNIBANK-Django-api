from django.urls import path
from minha_app.views import get_contas,criarConta,deletarConta,ContaById

urlpatterns = [
    path('get/all', get_contas, name='get_contas'),
    path('criar', criarConta, name='criar conta'),
    path('deletar/<int:conta_id>/', deletarConta, name='deletar conta'),
    path('get/byid/<int:pk>/',ContaById.as_view() ,name='conta-by-id'),
]
 