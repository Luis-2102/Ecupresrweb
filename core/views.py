from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Icono
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['iconos'] = Icono.objects.all()  
        return context

@csrf_exempt  # Solo para desarrollo, en producción maneja el CSRF apropiadamente
def contact_form(request):
    if request.method == 'POST':
        try:
            # Obtiene los datos del formulario
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            # Validación básica
            if not all([name, email, subject, message]):
                return JsonResponse({'status': 'error', 'message': 'Todos los campos son requeridos'})
            
            # Construye el mensaje
            email_body = f"""
            Nombre: {name}
            Correo: {email}
            Asunto: {subject}
            
            Mensaje:
            {message}
            """
            
            # Envía el correo
            send_mail(
                subject=f"Nuevo mensaje de contacto: {subject}",
                message=email_body,
                from_email=email,
                recipient_list=['lalomoto21@gmail.com'],
                fail_silently=False,
            )
            
            return JsonResponse({'status': 'success'})
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return render(request, 'contact.html')