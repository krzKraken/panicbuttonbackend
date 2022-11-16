from .models import Equipment
from rest_framework import viewsets, permissions
from .serializers import EquipmentSerializer


# viewset configures the permissions and the users that can see the data
class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    # permissions_classes = [permissions.IsAuthenticated]
    permissions_classes = [permissions.AllowAny]
    serializer_class = EquipmentSerializer