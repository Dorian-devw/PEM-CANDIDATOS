from rest_framework.routers import DefaultRouter
from .views import CandidatoViewSet, ProyectoViewSet, DenunciaViewSet

router = DefaultRouter()
router.register('candidatos', CandidatoViewSet)
router.register('proyectos', ProyectoViewSet)
router.register('denuncias', DenunciaViewSet)

urlpatterns = router.urls