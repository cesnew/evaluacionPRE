from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'evaluacion',      views.EvaluacionViewSet)
router.register(r'eje',             views.EjeViewSet)
router.register(r'categoria',       views.CategoriaViewSet)
router.register(r'responsable',     views.ResponsableViewSet)
router.register(r'recomendacion',   views.RecomendacionViewSet)
router.register(r'obcervaciones',   views.ObcervacionViewSet)

urlpatterns = [
    path('', include(router.urls))
]