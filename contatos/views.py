# Em comentarios: Outra forma para erro 404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

def index(request):

#   contatos = Contato.objects.all() # mostra sem ordem especifica
    contatos = Contato.objects.order_by('-id').filter(
        mostrar = True
    )
    
    paginator = Paginator(contatos, 5) # Show 'n' contacts per page.
    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)

    return render(request, 'contatos/index.html', {
        'contatos': contatos        
    })

def ver_contato(request, contato_id):
#    try:
#        contato = Contato.objects.get(id=contato_id)
        contato = get_object_or_404(Contato, id=contato_id)

        if not contato.mostrar:
            raise Http404()
        
        return render(request, 'contatos/ver_contato.html', {
            'contato': contato        
        })
#    except Contato.DoesNotExist as e:
#        raise Http404()

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio.' 
        )
        return redirect('index')
    
    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains = termo) | Q(telefone__icontains = termo)
    )
    
    paginator = Paginator(contatos, 5) # Show 'n' contacts per page.
    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos        
    })
