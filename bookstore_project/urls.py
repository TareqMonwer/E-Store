from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # Auth app by django
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('', include('pages.urls')),
]
