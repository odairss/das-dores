from django.shortcuts import render, redirect
#from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Livro, Autor,Cliente, Usuario, Emprestimo
from .forms import LivroForms, AutorForms, ClienteForms, UsuarioForms, EmprestimoForms


def login_user(request):
    return render(request,'login.html')

@csrf_protect
def submit(request):
    if request.POST:
        usuario = request.POST.get('username')
        senha = request.POST.get('pswd')
        user = authenticate(username=usuario,password=senha)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Usuário ou senha inválido.')
    return redirect('login')

@csrf_protect
def testelogin(request):
    return render(request,'testelogin.html')

@csrf_protect
def teste(request):
    usuario = request.POST.get('usuario')
    pswd = request.POST.get('senha')
    usuarios= Usuario.objects.filter(username=usuario, password=pswd)
    return render(request, 'teste.html',{'usuarios':usuarios})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'biblioteca.html')


#####USUARIOS########

def cadastro_usuario(request):
    form = UsuarioForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_usuarios')
    else:
        form = UsuarioForms()
    return render(request,'usuario-form.html', {'form': form})

def list_usuarios(request):
    usuarios = Usuario.objects.all()
    print(usuarios.query)
    return render(request,'list_usuarios.html',{'usuarios':usuarios})

def update_usuario(request, idusuario):
    usuario = Usuario.objects.get(idusuario=idusuario)
    form = UsuarioForms(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('list_usuarios')
    return render(request, 'usuario-form.html',{'form':form,'usuario':usuario})

def delete_usuario(request,idusuario):
    usuario = Usuario.objects.get(idusuario=idusuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('list_usuarios')
    return render(request, 'usuario-delete-confirm.html',{'usuario':usuario})

def usuario(request,idusuario):
    usuario = Usuario.objects.get(idusuario=idusuario)
    return render(request,'usuario.html',{'usuario': usuario})

#######LIVROS#########

def cadastro_livro(request):
    form = LivroForms(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('ver_acervo')
    else:
        form = LivroForms()
    return render(request,'livro-form.html',{'form': form})


def acervo(request):
    acervo = Livro.objects.all()
    return render(request,'acervo.html',{'acervo': acervo})

def livro(request,idlivro):
    livro = Livro.objects.get(idlivro=idlivro)
    return render(request,'livro.html',{'livro': livro})

def update_livro(request,idlivro):
    livro = Livro.objects.get(idlivro=idlivro)
    form = LivroForms(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('ver_acervo')
    return render(request,'livro-form.html',{'form': form,'livro': livro})

def delete_livro(request, idlivro):
    livro = Livro.objects.get(idlivro=idlivro)
    if request.method == 'POST':
        livro.delete()
        return redirect('ver_acervo')
    return render(request,'livro-delete-confirm.html',{'livro':livro})


#####AUTOR########

def cadastro_autor(request):
    form = AutorForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_autores')
    else:
        form = AutorForms()
    return render(request,'autor-form.html', {'form': form})

def list_autores(request):
    autores = Autor.objects.all()
    return render(request,'list_autores.html',{'autores':autores})

def update_autor(request, idautor):
    autor = Autor.objects.get(idautor=idautor)
    form = AutorForms(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('list_autores')
    return render(request, 'autor-form.html',{'form':form,'autor':autor})

def delete_autor(request,idautor):
    autor = Autor.objects.get(idautor=idautor)
    if request.method == 'POST':
        autor.delete()
        return redirect('list_autores')
    return render(request, 'autor-delete-confirm.html',{'autor':autor})

def autor(request,idautor):
    autor = Autor.objects.get(idautor=idautor)
    return render(request,'autor.html',{'autor': autor})


#####EMPRÉSTIMOS########

def cadastro_emprestimo(request):
    form = EmprestimoForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_emprestimos')
    else:
        form = EmprestimoForms()
    return render(request,'emprestimo-form.html', {'form': form})

#def livro_decrement(idlivro):


def list_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request,'list_emprestimos.html',{'emprestimos':emprestimos})

def update_emprestimo(request, idemprestimo):
    emprestimo = Emprestimo.objects.get(idemprestimo=idemprestimo)
    form = EmprestimoForms(request.POST or None, instance=emprestimo)
    if form.is_valid():
        form.save()
        return redirect('list_emprestimos')
    return render(request, 'emprestimo-form.html',{'form':form,'emprestimo':emprestimo})

def delete_emprestimo(request,idemprestimo):
    emprestimo = Emprestimo.objects.get(idemprestimo=idemprestimo)
    if request.method == 'POST':
        emprestimo.delete()
        return redirect('list_emprestimos')
    return render(request, 'emprestimo-delete-confirm.html',{'emprestimo':emprestimo})

def emprestimo(request,idemprestimo):
    emprestimo = Emprestimo.objects.get(idemprestimo=idemprestimo)
    return render(request,'emprestimo.html',{'emprestimo': emprestimo})

#####CLIENTES########

def cadastro_cliente(request):
    form = ClienteForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_clientes')
    else:
        form = ClienteForms()
    return render(request,'cliente-form.html', {'form': form})

def list_clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'list_clientes.html',{'clientes':clientes})

def update_cliente(request, idcliente):
    cliente = Cliente.objects.get(idcliente=idcliente)
    form = ClienteForms(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('list_clientes')
    return render(request, 'cliente-form.html',{'form':form,'cliente':cliente})

def delete_cliente(request,idcliente):
    cliente = Cliente.objects.get(idcliente=idcliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('list_clientes')
    return render(request, 'cliente-delete-confirm.html',{'cliente':cliente})

def cliente(request,idcliente):
    cliente = Cliente.objects.get(idcliente=idcliente)
    return render(request,'cliente.html',{'cliente': cliente})

#######EXTRAS#######

def simple_upload(request):
    if request.method == 'POST' and request.FILES['my-file']:
        myfile = request.FILES['my-file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploadfile.html',{'uploaded_file_url': uploaded_file_url})
    return render(request,'uploadfile.html')

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




