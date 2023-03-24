from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from bfbox import settings

urlpatterns = [
                  path('', include('dashboard.urls')),
                  path('clients/', include('clients.urls')),
                  path('appointments/', include('appointments.urls')),
                  path('templates_manager/', include('templates_manager.urls')),
                  path('reports_manager/', include('reports_manager.urls')),
                  path('accounts/', include('accounts.urls')),

                  #  path('admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
