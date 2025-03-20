from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path("ckeditor/", include("ckeditor_uploader.urls")),  # CKEditor file upload URLs
    path('accounts/', include('allauth.urls')),
    path("user/", include('user.urls')),
    path('lesson/',include('lesson.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)