from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/getbanco/', include('minha_app.urls2.Banco_urls')),
   # path('api/deletarbanco/', include('minha_app.urls2.Banco_urls')),
   # path('api/updatebanco/', include('minha_app.urls2.Banco_urls')),
   # path('api/cadastarbanco/', include('minha_app.urls2.Banco_urls')),
    path('api/conta/', include('minha_app.urls2.Conta_urls')),
    path('api/perfil/', include('minha_app.urls2.Perfil_urls')),
   # path('api/criarUser/', include('minha_app.urls2.Perfil_urls')),
    
     
]
