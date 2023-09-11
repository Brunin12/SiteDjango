from django.forms import ModelForm, DateTimeInput
from .models import Transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['dt_creation', 'description', 'value', 'notes', 'category']
        labels = {
            'dt_creation': 'Data de Criação',
            'description': 'Descrição',
            'value': 'Valor',
            'notes': 'Notas',
            'category': 'Categoria',
        }
        widgets = {
            'dt_creation': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'notes': DateTimeInput(attrs={'class': 'form-control', 'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super(TransacaoForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['value'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
