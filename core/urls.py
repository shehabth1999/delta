from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))
]

# Serve static and media files during development
if settings:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Delta Admin"
admin.site.site_title = "Delta Admin"
admin.site.index_title = "Admin"      