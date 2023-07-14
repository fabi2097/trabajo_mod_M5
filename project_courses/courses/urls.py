from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')
router.register('lessons', LessonViewSet, basename='lesson')
router.register('subscriptions', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
]
