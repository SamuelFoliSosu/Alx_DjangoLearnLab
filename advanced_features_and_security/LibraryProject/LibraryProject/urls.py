"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django-models/LibraryProject/LibraryProject/urls.py
from django.contrib import admin
from django.urls import path, include # Import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('app/', include('relationship_app.urls')), # Include your app's URLs here
    path('', include('bookshelf.urls')), # Now pointing to bookshelf.urls
    # path('relationship/', include('relationship_app.urls')), # Keep if you have one
    # You can choose any prefix for your app, '/app/' is just an example.
    # e.g., path('library_data/', include('relationship_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)