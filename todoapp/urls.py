from rest_framework.routers import DefaultRouter  
from .views import ToDoViewSet

# Create a new router
router = DefaultRouter()  
router.register(r'todos', ToDoViewSet, basename='todo') 

urlpatterns = router.urls 
