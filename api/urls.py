from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FinancialRecordViewSet, dashboard_summary

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'records', FinancialRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', dashboard_summary),
]