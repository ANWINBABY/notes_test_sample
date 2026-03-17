from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, register
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('register/', register),
    path('login/', TokenObtainPairView.as_view()),
    path('', include(router.urls)),
]