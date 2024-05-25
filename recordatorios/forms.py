from django import forms
from .models import Recordatorio

class RecordatorioForm(forms.ModelForm):
    class Meta:
        model = Recordatorio
        fields = ['nombre_medicamento', 'hora_alerta', 'comentario']
