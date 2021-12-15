from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            permissions = [IsAuthenticated]
        elif self.action in ["destroy", "update", "partial_update"]:
            permissions = [IsAuthenticated]
        else:
            permissions = []
        return [permission() for permission in permissions]
