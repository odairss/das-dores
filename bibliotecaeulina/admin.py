from django.contrib import admin
from .mymodels import Livro, Usuario, Emprestimo, Cliente

# Register your models here.
admin.site.register(Livro)
admin.site.register(Usuario)
admin.site.register(Emprestimo)
admin.site.register(Cliente)