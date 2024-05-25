from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import Recordatorio
from .forms import RecordatorioForm

def crear_recordatorio(request):
    if request.method == 'POST':
        form = RecordatorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_recordatorios')
    else:
        form = RecordatorioForm()
    return render(request, 'recordatorios/crear_recordatorio.html', {'form': form})

def lista_recordatorios(request):
    recordatorios = Recordatorio.objects.all()
    return render(request, 'recordatorios/lista_recordatorios.html', {'recordatorios': recordatorios})

def obtener_actualizaciones(request):
    ahora = timezone.localtime().time()  # aqui estoy usando timezone.localtime para obtener la hora local
    mensajes = []
    
    # se obtiene todos los recordatorios y verificamos si la hora actual coincide con la hora de alerta.
    recordatorios = Recordatorio.objects.all()
    for recordatorio in recordatorios:
        if recordatorio.hora_alerta.hour == ahora.hour and recordatorio.hora_alerta.minute == ahora.minute:
            mensajes.append(f"Es hora de tomar {recordatorio.nombre_medicamento}")

    if mensajes:
        return JsonResponse({'mensaje': ', '.join(mensajes)})
    else:
        return JsonResponse({'mensaje': ''})
