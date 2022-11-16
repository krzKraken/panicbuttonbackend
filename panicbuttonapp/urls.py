from rest_framework import routers
from .api import EquipmentViewSet

router = routers.DefaultRouter()

router.register('api/equipment', EquipmentViewSet, 'equipments')

urlpatterns = router.urls