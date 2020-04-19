from django import forms
from .mymodels import Livro, Exemplar, Autor,Cliente, Usuario, Emprestimo, Colecao


class DateInput(forms.DateInput):
    input_type = 'date'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
    format_key ='%m/%d/%y %H:%M:%S'


class ColecaoForms(forms.ModelForm):
    class Meta:
        model = Colecao
        fields = ['nome']


class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'idcolecao', 'paginas', 'capa', 'sinopse', 'editora',
                  'isbn', 'serie', 'tema', 'faixaetaria', 'ilustracao', 'idautor']


class ExemplarForms(forms.ModelForm):
    class Meta:
        model = Exemplar
        fields = ['idlivro','situacao','status']


class UsuarioForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nomeusuario','datanascimento','endereco','email','celular','perfil','username','password']
        widgets = {'datanascimento':DateInput(attrs={'format':'99/99/9999'})}


class ClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','datanascimento','endereco','email','celular','turno','ano','turma','responsavel','perfil','user','senha','multa','livrosemprestados']
        datawidget = forms.DateInput()
        datawidget.input_type = 'date'
        multawidget = forms.NumberInput()
        multawidget.input_type = 'number'
        livrosemprestadoswidget = forms.NumberInput()
        livrosemprestadoswidget.input_type = 'number'
        widgets = {'datanascimento':datawidget, 'multa':multawidget,'livrosemprestados':livrosemprestadoswidget}


class AutorForms(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nomeautor','biografia']
        labels = {'nomeautor':'Autor', 'biografia': 'Biografia'}


class EmprestimoForms(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['idexemplar','idcliente','datadevolucao','idusuario']
        labels = {'idexemplar': 'Exemplar', 'idcliente': 'Cliente', 'idusuario':'Usuário'}
        date_widget = forms.DateTimeInput()
        date_widget.input_type = 'date'
        widgets = {'datadevolucao':date_widget}


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', max_length=20)
    password = forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username and not password:
            raise forms.ValidationError('Your have to write something!')


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', max_length=20)
    password = forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username and not password:
            raise forms.ValidationError('Your have to write something!')


class SearchBookForm(forms.Form):
    book = forms.CharField(label='Título do Livro', max_length=200)
    def clean(self):
        cleaned_data = super(SearchBookForm, self).clean()
        book = cleaned_data.get('book')
        if not book:
            raise forms.ValidationError('You have to write something!')


class EmprestimoForm(forms.Form):
    idexemplar = forms.CharField(label='Exemplar',widget=forms.NumberInput)
    idclente = forms.CharField(label='Cliente', widget=forms.NumberInput)
    datadevolucao = forms.CharField(label='Data da Devolução', widget=forms.DateInput)
    idusuario = forms.CharField(label='Usuário', widget=forms.NumberInput)
