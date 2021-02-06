from django.conf.urls import url, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)