from django.shortcuts import render, redirect
#from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
#from django.contrib import messages #posso até excluir essa importação porque django form já vem com atributos de mensagens de erro.
from django.core.files.storage import FileSystemStorage
from .mymodels import Colecao, Livro, Autor,Cliente, Usuario, Emprestimo, Exemplar
from .forms import ColecaoForms, LivroForms, ExemplarForms, AutorForms, ClienteForms, UsuarioForms, EmprestimoForms, LoginForm,\
SearchBookForm
from datetime import datetime, timedelta, timezone

@csrf_protect
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request,'login.html',{'form':form})
        else:
            form = LoginForm()
            return render(request, 'login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'biblioteca.html')


#####USUARIOS########

@login_required(login_url='login')
def cadastro_usuario(request):
    form = UsuarioForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_usuarios')
    else:
        form = UsuarioForms()
    return render(request,'usuario-form.html', {'form': form})

@login_required(login_url='login')
def list_usuarios(request):
    usuarios = Usuario.objects.order_by("nomeusuario")
    print(usuarios.query)
    return render(request,'list_usuarios.html',{'usuarios':usuarios})

@login_required(login_url='login')
def update_usuario(request, idusuario):
    usuario = Usuario.objects.get(idusuario=idusuario)
    form = UsuarioForms(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('list_usuarios')
    return render(request, 'usuario-form.html',{'form':form,'usuario':usuario})

@login_required(login_url='login')
def delete_usuario(request,idusuario):
    usuario = Usuario.objects.get(idusuario=idusuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('list_usuarios')
    return render(request, 'usuario-delete-confirm.html',{'usuario':usuario})

@login_required(login_url='login')
def usuario(request,idusuario):
    usuario = Usuario.objects.get(idusuario=idusuario)
    return render(request,'usuario.html',{'usuario': usuario})


#######COLEÇÕES#########

@login_required(login_url='login')
def cadastro_colecao(request):
    form = ColecaoForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_colecoes')
    else:
        form = ColecaoForms()
    return render(request, 'colecao-form.html', {'form': form})


@login_required(login_url='login')
def list_colecoes(request):
    colecoes = Colecao.objects.all()
    return render(request, 'colecoes.html', {'colecoes': colecoes})


@login_required(login_url='login')
def colecao(request,idcolecao):
    colecao = Colecao.objects.get(idcolecao=idcolecao)
    return render(request, 'colecao.html', {'colecao': colecao})


@login_required(login_url='login')
def update_colecao(request,idcolecao):
    colecao = Colecao.objects.get(idcolecao=idcolecao)
    form = ColecaoForms(request.POST or None, instance=colecao)
    if form.is_valid():
        form.save()
        return redirect('ver_colecao')
    return render(request, 'colecao-form.html', {'form': form, 'colecao': colecao})


@login_required(login_url='login')
def delete_colecao(request, idcolecao):
    colecao = Colecao.objects.get(idcolecao=idcolecao)
    if request.method == 'POST':
        colecao.delete()
        return redirect('ver_colecao')
    return render(request, 'colecao-delete-confirm.html', {'colecao': colecao})


#######LIVROS#########

@login_required(login_url='login')
def cadastro_livro(request):
    form = LivroForms(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('ver_acervo')
    else:
        form = LivroForms()
    return render(request,'livro-form.html',{'form': form})

@login_required(login_url='login')
def acervo(request):
    if request.method == 'POST':
        book = request.POST.get('book')
        booksfound = Livro.objects.filter(titulo__contains=book).order_by('titulo')
        formBook = SearchBookForm()
        return render(request, 'acervo.html',{'acervo':booksfound,'form':formBook})
    else:
        formBook = SearchBookForm()
        return render(request, 'acervo.html',{'form':formBook})


@login_required(login_url='login')
def livro(request,idlivro):
    livro = Livro.objects.get(idlivro=idlivro)
    return render(request,'livro.html',{'livro': livro})

def detalhes_livro(request, idlivro):
    livro = Livro.objects.get(idlivro=idlivro)
    return render(request, 'detalhes_livro.html',{'livro':livro})

@login_required(login_url='login')
def update_livro(request,idlivro):
    livro = Livro.objects.get(idlivro=idlivro)
    form = LivroForms(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('ver_acervo')
    return render(request,'livro-form.html',{'form': form,'livro': livro})

@login_required(login_url='login')
def delete_livro(request, idlivro):
    livro = Livro.objects.get(idlivro=idlivro)
    if request.method == 'POST':
        livro.delete()
        return redirect('ver_acervo')
    return render(request,'livro-delete-confirm.html',{'livro':livro})

#######EXEMPLARES#########

@login_required(login_url='login')
def cadastro_exemplar(request):
    form = ExemplarForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('exemplares')
    else:
        form = ExemplarForms()
    return render(request,'exemplar-form.html',{'form': form})

@login_required(login_url='login')
def exemplares(request):
    exemplars = Exemplar.objects.all()
    return render(request,'exemplares.html',{'exemplares': exemplars})

@login_required(login_url='login')
def exemplar(request,idexemplar):
    example = Exemplar.objects.get(idexemplar=idexemplar)
    return render(request,'exemplar.html',{'exemplar': example})

@login_required(login_url='login')
def update_exemplar(request,idexemplar):
    example = Exemplar.objects.get(idexemplar=idexemplar)
    form = ExemplarForms(request.POST or None, instance=example)
    if form.is_valid():
        form.save()
        return redirect('exemplares')
    return render(request,'exemplar-form.html',{'form': form,'exemplar': example})

@login_required(login_url='login')
def delete_exemplar(request, idexemplar):
    example = Exemplar.objects.get(idexemplar=idexemplar)
    if request.method == 'POST':
        example.delete()
        return redirect('exemplares')
    return render(request,'exemplar-delete-confirm.html',{'exemplar':example})

def  emprestar_exemplar(request, idexemplar):
    example = Exemplar.objects.get(idexemplar=idexemplar)
    all_clientes = Cliente.objects.all()
    clientes = []
    for client in all_clientes:
        if client.multa <= 0 and client.livrosemprestados < 1:
            clientes.append(client)
    hoje = datetime.now(timezone.utc) - timedelta(hours=3)
    datadevolver = hoje + timedelta(days=1)
    return render(request, 'emprestar-exemplar-form.html',{'clientes':clientes, 'exemplar':example, 'datadevolver':datadevolver.__format__("%d/%m/%Y %H:%M:%S")})


#####AUTOR########

@login_required(login_url='login')
def cadastro_autor(request):
    form = AutorForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_autores')
    else:
        form = AutorForms()
    return render(request,'autor-form.html', {'form': form})

@login_required(login_url='login')
def list_autores(request):
    autores = Autor.objects.order_by("nomeautor")
    return render(request,'list_autores.html',{'autores':autores})

@login_required(login_url='login')
def update_autor(request, idautor):
    autor = Autor.objects.get(idautor=idautor)
    form = AutorForms(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('list_autores')
    return render(request, 'autor-form.html',{'form':form,'autor':autor})

@login_required(login_url='login')
def delete_autor(request,idautor):
    autor = Autor.objects.get(idautor=idautor)
    if request.method == 'POST':
        autor.delete()
        return redirect('list_autores')
    return render(request, 'autor-delete-confirm.html',{'autor':autor})

@login_required(login_url='login')
def autor(request,idautor):
    autor = Autor.objects.get(idautor=idautor)
    return render(request,'autor.html',{'autor': autor})


#####EMPRÉSTIMOS########

@login_required(login_url='login')
def cadastro_emprestimo(request):
    form = EmprestimoForms(request.POST)
    if form.is_valid():
        idexemplar = request.POST.get('idexemplar')
        example = Exemplar.objects.get(idexemplar=idexemplar)
        idcliente = request.POST.get('idcliente')
        client = Cliente.objects.get(idcliente=idcliente)
        client.livrosemprestados = client.livrosemprestados + 1
        example.status = False
        example.save()
        client.save()
        form.save()
        return redirect('list_emprestimos')
    else:
        form = EmprestimoForms()
    return render(request,'emprestimo-form.html', {'form': form})

@login_required(login_url='login')
def list_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(devolucao=False)
    return render(request,'list_emprestimos.html',{'emprestimos':emprestimos})

@login_required(login_url='login')
def update_emprestimo(request, idemprestimo):
    emprestimo = Emprestimo.objects.get(idemprestimo=idemprestimo)
    form = EmprestimoForms(request.POST or None, instance=emprestimo)
    if form.is_valid():
        form.save()
        return redirect('list_emprestimos')
    return render(request, 'emprestimo-form.html',{'form':form,'emprestimo':emprestimo})

@login_required(login_url='login')
def delete_emprestimo(request,idemprestimo):
    emprestimo = Emprestimo.objects.get(idemprestimo=idemprestimo)
    if request.method == 'POST':
        exemplar = emprestimo.idexemplar
        exemplar.status = True
        exemplar.save()
        emprestimo.delete()
        return redirect('list_emprestimos')
    return render(request, 'emprestimo-delete-confirm.html',{'emprestimo':emprestimo})

@login_required(login_url='login')
def emprestimo(request,idemprestimo):
    emprestimo = Emprestimo.objects.get(idemprestimo=idemprestimo)
    return render(request,'emprestimo.html',{'emprestimo': emprestimo})

@login_required(login_url='login')
def devolver(request, idemprestimo):
    emprest = Emprestimo.objects.get(idemprestimo=idemprestimo)
    emprest.devolucao = True
    example = Exemplar.objects.get(idexemplar=emprest.idexemplar.idexemplar)
    client = Cliente.objects.get(idcliente=emprest.idcliente.idcliente)
    client.livrosemprestados = client.livrosemprestados - 1
    example.status = True
    emprest.datadevolvido = datetime.now(timezone.utc) - timedelta(hours=3)
    example.save()
    emprest.save()
    client.save()
    return render(request, 'emprestimo.html',{'emprestimo':emprest})

#####CLIENTES########

@login_required(login_url='login')
def cadastro_cliente(request):
    form = ClienteForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_clientes')
    else:
        form = ClienteForms()
    return render(request,'cliente-form.html', {'form': form})

@login_required(login_url='login')
def list_clientes(request):
    clientes = Cliente.objects.order_by("nome")
    return render(request,'list_clientes.html',{'clientes':clientes})

@login_required(login_url='login')
def update_cliente(request, idcliente):
    cliente = Cliente.objects.get(idcliente=idcliente)
    form = ClienteForms(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('list_clientes')
    return render(request, 'cliente-form.html',{'form':form,'cliente':cliente})

@login_required(login_url='login')
def delete_cliente(request,idcliente):
    cliente = Cliente.objects.get(idcliente=idcliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('list_clientes')
    return render(request, 'cliente-delete-confirm.html',{'cliente':cliente})

@login_required(login_url='login')
def cliente(request,idcliente):
    cliente = Cliente.objects.get(idcliente=idcliente)
    return render(request,'cliente.html',{'cliente': cliente})

def historico(request,idcliente):
    cliente = Cliente.objects.get(idcliente=idcliente)
    emprestimos = Emprestimo.objects.filter(idcliente=idcliente)
    return render(request,'historico-cliente.html',{'cliente': cliente, 'emprestimos':emprestimos})

#######EXTRAS#######
@login_required(login_url='login')
def simple_upload(request):
    if request.method == 'POST' and request.FILES['my-file']:
        myfile = request.FILES['my-file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploadfile.html',{'uploaded_file_url': uploaded_file_url})
    return render(request,'uploadfile.html')

@login_required(login_url='login')
def model_form_upload(request):
    if request.method == 'POST':
        form = LivroForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LivroForms()
    return render(request, 'cadastro_livro.html', {
        'form': form
    })




