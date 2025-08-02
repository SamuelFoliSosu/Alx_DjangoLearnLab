from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from api.views import BookList
from api.views import BookViewSet

# Create a router instance
router = DefaultRouter()
# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('books/', BookList.as_view(), name='book-list'),
    # path('api/', include('api.urls'))

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)), # This includes all routes registered with the router
]