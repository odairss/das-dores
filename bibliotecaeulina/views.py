from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Livro, Pessoa
from .forms import LivroForms, ProfessorForms, AlunoForms, LeitorForms

# Create your views here.
def home(request):
    return render(request,'biblioteca.html')

def acervo(request):
    acervo = Livro.objects.all()
    return render(request,'acervo.html',{'acervo': acervo})

def livro(request,id):
    livro = Livro.objects.get(id=id)
    #book = livro.objects.delete(id=id)
    #bookin = livro.objects.update(id=id)
    return render(request,'livro.html',{'livro': livro})

def cadastro_livro(request):
    form = LivroForms(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('ver_acervo')
    else:
        form = LivroForms()
    return render(request,'livro-form.html',{'form': form})

def cadastro_aluno(request):
    form = AlunoForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_users')
    else:
        form = AlunoForms()
    return render(request, 'aluno-form.html', {'form': form})

def cadastro_leitor(request):
    form = LeitorForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_users')
    else:
        form = LeitorForms()
    return render(request, 'leitor-form.html', {'form': form})

def cadastro_professor(request):
    form = ProfessorForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_users')
    else:
        form = ProfessorForms()
    return render(request,'professor-form.html', {'form': form})

def update_livro(request,id):
    livro = Livro.objects.get(id=id)
    form = LivroForms(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('ver_acervo')
    return render(request,'livro-form.html',{'form': form,'livro': livro})

def delete_livro(request, id):
    livro = Livro.objects.get(id=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('ver_acervo')
    return render(request,'livro-delete-confirm.html',{'livro':livro})


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

def list_users(request):
    users = Pessoa.objects.all()
    return render(request,'list_users.html',{'users':users})

