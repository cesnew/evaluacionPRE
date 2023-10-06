from django.http import FileResponse
from django.shortcuts import get_object_or_404, render, redirect
from api.models import Persona
from .forms import PersonaForm, EvaluacionForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request, 'index.html')

# login
def startsession(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
        password=request.POST['password'])

        if user is None:
                return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'username or password incorrect'
            })
        else:
            login(request, user)
            return redirect('lista_personas')

######################################################

# register user
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm 
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # usuario
                login(request, user)
                return redirect('login')
            except:
                # return HttpResponse('el usuario ya existe')
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error' : 'usario ya existe' 
                })
        # return HttpResponse('passwords no coinciden')
        return render(request, 'signup.html', {
            'form': UserCreationForm, 
            'error': 'passwords no coinciden'
    })

#######################################################        
# logout
@login_required
def endsession(request):
    logout(request)
    return redirect('index')
#######################################################        

@login_required
def Lista(request): 
    personas = Persona.objects.all()
    return render(request, 'personas.html', {
        'personas': personas
    })

########################################################

@login_required
def cargar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('lista_personas')   

    else:
        form = PersonaForm()
    return render(request, 'cargar_persona.html', {
        'form': form
    })           

########################################################

def obtener_pdf(request, pdf_id):
    pdf = get_object_or_404(Persona, pk = pdf_id)
    response = FileResponse(pdf.archivo, content_type='application/pdf')
    return response
    


def evaluacion(request):
    if request.method == "POST":
        url = "http://localhost:8000/api/evaluacion/"
        datos ={
            "nombre":       request.POST.get('nombre'),
            "fecha_eva":    request.POST.get('fecha_eva'),
            "fecha_pmyac":  request.POST.get('fecha_pmyac'),
        }
        print(datos)
        response = requests.post(url, json=datos)
        return render(request, 'index.html')     
    else:
        return render(request, 'evaluacion.html')       





class BusquedaView(ListView):
    model = Persona
    template_name = 'resultado_busqueda.html'  # Nombre de tu plantilla HTML
    context_object_name = 'resultados'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Persona.objects.filter(
                Q(nombre__icontains=query) | Q(edad__icontains=query)
            )
        else:
            return Persona.objects.all()
        

def detail(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    # print(pk)
    return render(request, 'detail.html', {'persona': persona})
