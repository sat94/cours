from django.contrib import admin
from django.urls import path
#IMPORTER les deux fichier suivant
from django.conf.urls.static import static
from main import settings

from .views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
