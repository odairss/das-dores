#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True, verbose_name='Código')
#    idcliente = models.IntegerField('Id Cliente',primary_key=True,auto_created=True)
    nome = models.CharField('Nome', max_length=200)
    datanascimento = models.DateField('Data de Nascimento',null=True, blank=True)
    endereco = models.TextField('Endereço', max_length=500,null=True, blank=True)
    email = models.EmailField('E-mail',null=True)
    celular = models.CharField('Celular', max_length=50,null=True, blank=True)
    TURNOS = ((u'matutino',u'Matutino'),(u'vespertino',u'Vespertino'),(u'noturno',u'Noturno'))
    turno = models.CharField('Turno',max_length=50, choices=TURNOS, null=True, blank=True)
    ANOS = ((1,u'1º'),(1,u'2º'),(1,u'3º'),(1,u'4º'),(1,u'5º'))
    ano = models.IntegerField('Ano',choices=ANOS,null=True, blank=True)
    TURMAS = ((u'A',u'A'),(u'B',u'B'),(u'C',u'C'),(u'D',u'D'))
    turma = models.CharField('Turma',choices=TURMAS,max_length=20,null=True, blank=True)
    responsavel = models.TextField('Responsável',null=True, blank=True)
    TIPO = ((u'professor',u'Professor'),(u'aluno',u'Aluno'),(u'publico',u'Público'))
    perfil = models.CharField('Perfil',max_length=15, choices=TIPO)
    user = models.CharField('Nome de Usuário', max_length=20)
    senha = models.CharField('Senha', max_length=15)
    multa = models.IntegerField(default=0)
    livrosemprestados = models.IntegerField('Livros Emprestados',default=0,blank=True)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nomeautor = models.CharField('Nome', max_length=100)
    idautor = models.AutoField(primary_key=True, verbose_name='Código')
#    idautor = models.IntegerField('Id Autor',auto_created=True, primary_key=True)
    biografia = models.TextField('Biografia', blank=True)

    def __str__(self):
        return self.nomeautor


class Colecao(models.Model):
    idcolecao = models.AutoField(primary_key=True, verbose_name='Código')
    nome = models.CharField('Nome da Coleção', max_length=300)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    idlivro = models.AutoField(primary_key=True, verbose_name='Código')
#    idlivro = models.IntegerField('Id Livro', auto_created=True, primary_key=True)
    titulo = models.CharField('Título',max_length=200)
    idcolecao = models.ForeignKey(Colecao, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Coleção')
    capa = models.ImageField(upload_to='img/',null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    paginas = models.DecimalField(max_digits=7,decimal_places=0,null=True,blank=True)
    editora = models.CharField('Editora', max_length=200,blank=True)
    isbn = models.CharField('ISBN', max_length=200,null=True,blank=True)
    serie = models.CharField('Série', max_length=200, null=True,blank=True)
    tema = models.CharField(max_length=200,null=True,blank=True)
    faixaetaria = models.IntegerField('Faixa Etária',null=True,blank=True)
    idautor = models.ManyToManyField(Autor)
    sinopse = models.TextField('Sinópse',null=True,blank=True)
    ilustracao = models.CharField('Ilustração', max_length=200,null=True,blank=True)
    SITUATION = ((u'Excelente',u'Excelente'),(u'Ótimo',u'Ótimo'),(u'Bom',u'Bom'),(u'Ruim',u'Ruim'),(u'Péssimo',u'Péssimo'))
    situacao = models.CharField('Situação',max_length=20,choices=SITUATION)

    def __str__(self):
        return self.titulo


class Exemplar(models.Model):
    idexemplar = models.AutoField(primary_key=True, verbose_name='Código')
#    idexemplar = models.IntegerField('Exemplar',auto_created=True,primary_key=True)
    idlivro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name='Livro')
    SITUATION = ((u'Excelente',u'Excelente'),(u'Ótimo',u'Ótimo'),(u'Bom',u'Bom'),(u'Ruim',u'Ruim'),(u'Péssimo',u'Péssimo'))
    situacao = models.CharField('Situação',max_length=20,choices=SITUATION)
    DISPONIVEL = ((True,u'Disponível'),(False,u'Indisponível'))
    status = models.BooleanField('Disponível para Empréstimo', max_length=15, choices=DISPONIVEL)

    def __str__(self):
        return "%s - %s"%(self.idlivro, self.idexemplar)


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True, verbose_name='Código')
#    idusuario = models.IntegerField('Id Usuário',primary_key=True,auto_created=True)
    nomeusuario = models.CharField('Nome', max_length=200)
    datanascimento = models.DateField('Data de Nascimento',null=True,blank=True)
    endereco = models.CharField('Endereço', max_length=500,null=True,blank=True)
    email = models.EmailField('E-mail',null=True,blank=True)
    celular = models.CharField('Celular', max_length=50,null=True,blank=True)
    TIPO = ((u'administrador',u'Administrador'),(u'mediador',u'Mediador de Leitura'))
    perfil = models.CharField('Perfil',max_length=15, choices=TIPO)
    username = models.CharField('Nome de Usuário', max_length=20)
    password = models.CharField('Senha', max_length=15)

    def __str__(self):
        return self.nomeusuario


class Emprestimo(models.Model):
    idemprestimo = models.AutoField(primary_key=True, verbose_name='Código')
#    idemprestimo = models.IntegerField('Id Empréstimo',auto_created=True, primary_key=True)
    idexemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dataemprestimo = models.DateTimeField(auto_now_add=True)
    datadevolucao = models.DateTimeField('Data de Devolução')
    datadevolvido = models.DateTimeField('Data em que foi devolvido', null=True, blank=True)
    diasatrasados = models.IntegerField(default=0)
    devolucao = models.BooleanField('Confirmar devolução', default=False)
    idusuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return "%s"%(self.idexemplar)

