from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),   # GET /api/rooms
    path('rooms/', views.getRooms),   # GET /api/rooms
    path('rooms/<str:pk>', views.getRoom),   # GET /api/rooms

]