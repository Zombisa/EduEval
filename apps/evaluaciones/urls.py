from django.urls import path
from .controllers.views import (
    EvaluacionCreateView,
    EvaluacionListView,
    EvaluacionRetrieveView,
    EvaluacionUpdateView,
    EvaluacionDeleteView,
    EvaluacionListAllView,
    NivelDesempenoListView,
)

urlpatterns = [
    path('crear/', EvaluacionCreateView.as_view(), name='crear_evaluacion'),
    path('listar/', EvaluacionListView.as_view(), name='listar_evaluaciones'),
    path('listar-todas/', EvaluacionListAllView.as_view(), name='listar_todas_evaluaciones'),
    path('<int:pk>/', EvaluacionRetrieveView.as_view(), name='detalle_evaluacion'),
    path('actualizar/<int:pk>/', EvaluacionUpdateView.as_view(), name='actualizar_evaluacion'),
    path('eliminar/<int:pk>/', EvaluacionDeleteView.as_view(), name='eliminar_evaluacion'),
    path('obtener/<int:pk>/', EvaluacionRetrieveView.as_view()),
    
    # Niveles de desempeño
    path('niveles-desempeno/', NivelDesempenoListView.as_view(), name='listar_niveles_desempeno'),
]
