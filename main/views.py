from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Event, SocialAction 
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib import messages

# View PRINCIPAL que exibe a página e lida com o formulário
def index(request):
    print("=== INICIANDO VIEW INDEX ===")
    
   
    if request.method == 'POST':
        print("=== MÉTODO POST DETECTADO ===")
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            print("=== FORMULÁRIO VÁLIDO ===")
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message_content = contact_form.cleaned_data['message']
            
            
            full_message = f"""
            Nova mensagem de contato do site:
            
            Nome: {name}
            Email: {email}
            Assunto: {subject}
            
            Mensagem:
            {message_content}
            
            ---
            Enviado através do site Igreja Doravante
            """
            
            try:
                print("=== ENVIANDO EMAIL REAL ===")
                
                
                send_mail(
                    subject=f'CONTATO SITE: {subject}',
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['igreadoravante@email.com'],  
                    fail_silently=False,
                )
                
                print("=== EMAIL ENVIADO COM SUCESSO ===")
                messages.success(request, '✅ Sua mensagem foi enviada com sucesso! Em breve entraremos em contato.')
                return redirect('main:index')
            
            except Exception as e:
                print(f"=== ERRO NO ENVIO: {e} ===")
                messages.error(request, '❌ Ocorreu um erro ao tentar enviar sua mensagem. Tente novamente mais tarde.')
                
        else:
            print("=== FORMULÁRIO INVÁLIDO ===")
            messages.error(request, '⚠️ Por favor, corrija os erros destacados no formulário.')

    else: 
        # Requisição GET (carregamento inicial da página)
        print("=== MÉTODO GET - FORMULÁRIO VAZIO ===")
        contact_form = ContactForm()
    
    # BUSCAR DADOS DO BANCO
    try:
        events_list = Event.objects.all().order_by('-date')
        actions_list = SocialAction.objects.all().order_by('-date')
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        events_list = []
        actions_list = []

    context = {
        'contact_form': contact_form,
        'events': events_list,   
        'actions': actions_list,
    }
    
    return render(request, 'main/index.html', context)


def action_detail(request, pk): 
    action = get_object_or_404(SocialAction, pk=pk)
    context = {
        'action': action
    }
    return render(request, 'main/action_detail.html', context)

# Nova View: event_detail
def event_detail(request, pk): # pk (Primary Key) é o ID do objeto
    """
    Renderiza a página de detalhes de um evento específico.
    """
    event = get_object_or_404(Event, pk=pk)
    context = {
        'event': event 
    }
    return render(request, 'main/event_detail.html', context)