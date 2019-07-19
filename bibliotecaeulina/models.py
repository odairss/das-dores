from django.db import models

# Create your models here.

class Livro(models.Model):
    DISPONIVEL = ((u'S',u'Sim'),(u'N',u'Não'))
    titulo = models.CharField('Título',max_length=200)
    capa = models.ImageField(upload_to='img/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    paginas = models.DecimalField(max_digits=7,decimal_places=0)
    editora = models.CharField('Editora', max_length=200)
    isbn = models.CharField('ISBN', max_length=200)
    serie = models.CharField('Série', max_length=200)
    tema = models.CharField(max_length=200)
    faixaetaria = models.IntegerField('Faixa Etária')
    id = models.IntegerField(primary_key=True)
    sinopse = models.TextField('Sinópse')
    ilustracao = models.CharField('Ilustração', max_length=200)
    quantidade = models.IntegerField('Quantidade')
    disponivel = models.CharField('Disponível para Empréstimo', max_length=5, choices=DISPONIVEL)
    def __str__(self):
        return self.titulo

class Pessoa(models.Model):
    idpessoa = models.IntegerField('ID', primary_key=True)
    nome = models.CharField('Nome', max_length=200)
    datanascimento = models.DateField('Data de Nascimento')
    endereco = models.CharField('Endereço', max_length=500)
    email = models.EmailField('E-mail')
    celular = models.CharField('Celular', max_length=50)
    senha = models.CharField('Senha', max_length=15)
    def __str__(self):
        return self.nome

class Aluno(Pessoa):
    TURNO = ((u'matutino',u'matutino'),(u'vespertino',u'vespertino'))
    ano = models.IntegerField('Ano')
    turma = models.CharField('Turma', max_length=1)
    turno = models.CharField('Turno', max_length=50, choices=TURNO)
    nomeresponsavel = models.CharField('Responsável', max_length=50)
    def __str__(self):
        return self.nome

class Professor(Pessoa):
    TURNO = ((u'matutino',u'matutino'),(u'vespertino',u'vespertino'))
    matricula = models.IntegerField('Matrícula')
    turma = models.CharField('Turma', name='turma', max_length=1)
    turno = models.CharField('Turno', name='turno', max_length=20, choices=TURNO)
    funcao = models.CharField('Função', name='funcao', max_length=15)
    def __str__(self):
        return self.nome

class Leitor(Pessoa):
    alunos = models.TextField('Alunos')
    def __str__(self):
        return self.nome
