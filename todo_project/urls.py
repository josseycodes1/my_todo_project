from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin URL
    path('api/', include('todoapp.urls')),  # Include the URLs from the 'todo' app under the /api/ path
]
