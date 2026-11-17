
from rest_framework.viewsets import ModelViewSet
from .models import Equipment
from .serializers import EquipmentSerializer
    
class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.order_by("id")
    serializer_class = EquipmentSerializer
# Create your views here.
