from core.views import PacienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/pacientes',PacienteViewSet, basename='paciente')

urlpatterns=router.urls