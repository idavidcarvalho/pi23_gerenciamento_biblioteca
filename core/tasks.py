from django_q.models import Schedule
from django.utils import timezone
from .models import Emprestimo
from django_q.tasks import schedule

def verificar_atraso(emprestimo_id):
    emprestimo = Emprestimo.objects.get(pk=emprestimo_id)
    emprestimo.verificar_atraso()
    
    # Agendar próxima verificação
    if emprestimo.status == 'em andamento':
        schedule('core.tasks.verificar.atraso', f'{emprestimo.id}', schedule_type=Schedule.ONCE, next_run=timezone.now() + timezone.timedelta(days=1))