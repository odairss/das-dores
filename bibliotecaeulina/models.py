from django.db import models

# Create your models here.

class Cliente(models.Model):
    idcliente = models.IntegerField('Id Cliente',primary_key=True,auto_created=True)
    nome = models.CharField('Nome', max_length=200)
    datanascimento = models.DateField('Data de Nascimento',null=True)
    endereco = models.TextField('Endereço', max_length=500,null=True)
    email = models.EmailField('E-mail',null=True)
    celular = models.CharField('Celular', max_length=50,null=True)
    TURNOS = ((u'matutino',u'Matutino'),(u'vespertino',u'Vespertino'),(u'noturno',u'Noturno'))
    turno = models.CharField('Turno',max_length=50, choices=TURNOS, null=True)
    ANOS = ((1,u'1º'),(1,u'2º'),(1,u'3º'),(1,u'4º'),(1,u'5º'))
    ano = models.IntegerField('Ano',choices=ANOS,null=True)
    TURMAS = ((u'A',u'A'),(u'B',u'B'),(u'C',u'C'),(u'D',u'D'))
    turma = models.CharField('Turma',choices=TURMAS,max_length=20,null=True)
    responsavel = models.TextField('Responsável',null=True)
    TIPO = ((u'professor',u'Professor'),(u'aluno',u'Aluno'),(u'publico',u'Público'))
    perfil = models.CharField('Perfil',max_length=15, choices=TIPO)
    user = models.CharField('Nome de Usuário', max_length=20)
    senha = models.CharField('Senha', max_length=15)
    def __str__(self):
        return self.nome

class Autor(models.Model):
    nomeautor = models.CharField('Nome', max_length=100)
    idautor = models.IntegerField('Id Autor',auto_created=True, primary_key=True)
    biografia = models.TextField('Biografia')
    def __str__(self):
        return self.nomeautor

class Livro(models.Model):
    idlivro = models.IntegerField('Id Livro', auto_created=True, primary_key=True)
    titulo = models.CharField('Título',max_length=200)
    capa = models.ImageField(upload_to='img/',null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    paginas = models.DecimalField(max_digits=7,decimal_places=0,null=True)
    editora = models.CharField('Editora', max_length=200)
    isbn = models.CharField('ISBN', max_length=200,null=True)
    serie = models.CharField('Série', max_length=200, null=True)
    tema = models.CharField(max_length=200,null=True)
    faixaetaria = models.IntegerField('Faixa Etária',null=True)
    idautor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    sinopse = models.TextField('Sinópse',null=True)
    ilustracao = models.CharField('Ilustração', max_length=200,null=True)
    quantidade = models.IntegerField('Quantidade')
    DISPONIVEL = ((u'S',u'Disponível'),(u'N',u'Indisponível'))
    disponivel = models.CharField('Disponível para Empréstimo', max_length=5, choices=DISPONIVEL)
    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    idusuario = models.IntegerField('Id Usuário',primary_key=True,auto_created=True)
    nomeusuario = models.CharField('Nome', max_length=200)
    datanascimento = models.DateField('Data de Nascimento',null=True)
    endereco = models.CharField('Endereço', max_length=500,null=True)
    email = models.EmailField('E-mail',null=True)
    celular = models.CharField('Celular', max_length=50,null=True)
    TIPO = ((u'administrador',u'Administrador'),(u'mediador',u'Mediador de Leitura'))
    perfil = models.CharField('Perfil',max_length=15, choices=TIPO)
    username = models.CharField('Nome de Usuário', max_length=20)
    password = models.CharField('Senha', max_length=15)
    def __str__(self):
        return self.nomeusuario

class Emprestimo(models.Model):
    idemprestimo = models.IntegerField('Id Empréstimo',auto_created=True, primary_key=True)
    idlivro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dataemprestimo = models.DateTimeField(auto_now_add=True)
    datadevolucao = models.DateTimeField('Data de Devolução')
    idusuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    def __str__(self):
        return str(self.idemprestimo)

