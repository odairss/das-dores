from django import forms
from .models import Livro, Aluno, Leitor, Professor

class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo','autor','paginas','capa','sinopse','editora',
                  'isbn','serie','tema','faixaetaria','ilustracao','quantidade','disponivel']

class ProfessorForms(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome','matricula','datanascimento','endereco','email','senha','celular','turma','turno','funcao']

class AlunoForms(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','nomeresponsavel','datanascimento','endereco','celular','ano','turma','turno']

class LeitorForms(forms.ModelForm):
    class Meta:
        model = Leitor
        fields = ['nome','datanascimento','endereco','email','senha','celular','alunos']