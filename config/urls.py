# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Commentez cette ligne avec un # car vous n'avez pas encore cette application
    # path('operateur/', include('operator.urls')), 
    
    path('controleur/', include('controller.urls')),
   # path('', include('core.urls')),
]