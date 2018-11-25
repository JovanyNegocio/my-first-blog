from django.conf.urls import include, url
from django.contrib import admin

#from django.urls import path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
] #+ static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
