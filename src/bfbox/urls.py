from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from bfbox import settings

urlpatterns = [
                  path('clients/', include('clients.urls', namespace='clients')),
                  path('admin/', admin.site.urls),
                  path('', include('dashboard.urls')),
                  path('appointments/', include('appointments.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
