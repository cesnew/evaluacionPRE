from django.urls import path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static
from .views import BusquedaView


urlpatterns = [
    path('', views.index, name = "index"),
    path('login', views.startsession, name = "signin"),
    path('signup/', views.signup, name = "signup"),
    path('logout/', views.endsession, name="logout"),
    path('cargar', views.cargar_persona, name='cargar_persona'),
    path('lista_personas', views.Lista, name='lista_personas'),
    path('obtener_pdf/<int:pdf_id>/', views.obtener_pdf, name='obtener_pdf'),
    path('evaluacion', views.evaluacion, name='evaluacion'),
    path('buscar/', BusquedaView.as_view(), name='buscar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)