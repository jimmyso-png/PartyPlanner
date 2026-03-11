# src/backend/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Evento

def login_view(request):
    """
    Controlador que maneja la autenticación de usuarios (Caso de Prueba CP01).
    Valida credenciales seguras contra la base de datos PostgreSQL.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirección exitosa al dashboard como se ve en el pantallazo
            return redirect('dashboard_exito')
        else:
            messages.error(request, 'Credenciales inválidas. Intente nuevamente.')
            return render(request, 'auth/login.html')
            
    return render(request, 'auth/login.html')


@login_required(login_url='/login/')
def dashboard_exito(request):
    """
    Renderiza la vista principal del usuario una vez el login es exitoso.
    Obtiene los próximos eventos directamente desde la base de datos.
    """
    # Consulta a la BD: Obtener el evento más cercano del usuario activo
    proximo_evento = Evento.objects.filter(organizador=request.user, estado='ACTIVO').order_by('fecha').first()
    
    # Contexto de datos que se enviará al archivo dashboard.html
    context = {
        'nombre_usuario': request.user.first_name,  # Ejemplo: "Ana"
        'apellido_usuario': request.user.last_name, # Ejemplo: "López"
        'proximo_evento': proximo_evento,           # Ejemplo: "Cumpleaños de Sofía"
    }
    
    return render(request, 'frontend/dashboard.html', context)
