from django import forms
from .models import Livro, Autor,Cliente, Usuario, Emprestimo

class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo','paginas','capa','sinopse','editora',
                  'isbn','serie','tema','faixaetaria','ilustracao','quantidade','idautor','disponivel']

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nomeusuario','datanascimento','endereco','email','celular','perfil','username','password']

class ClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','datanascimento','endereco','email','celular','turno','ano','turma','responsavel','perfil','user','senha']


class AutorForms(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nomeautor','biografia']

class EmprestimoForms(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['idlivro','idcliente','datadevolucao','idusuario']