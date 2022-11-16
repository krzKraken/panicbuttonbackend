from rest_framework import serializers
from .models import Equipment


# Convert data in data that we can use and read
class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ("id", "brand", "model", "serial_number", "description",
                  "client", "center", "ubication", "reported", "created_at")
        read_only_fields = ("created_at", )
