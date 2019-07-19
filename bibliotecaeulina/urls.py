from django.urls import path
from .views import home,livro,acervo,cadastro_livro,update_livro,delete_livro,list_users,\
    cadastro_professor, cadastro_aluno, cadastro_leitor


urlpatterns = [
    path('', home, name="index"),
    path('acervo', acervo, name="ver_acervo"),
    path('livro/<int:id>/', livro, name="buscar_livro"),
    path('cadastro_livro', cadastro_livro, name='new'),
    path('update/<int:id>/', update_livro, name='update_livro'),
    path('delete/<int:id>/', delete_livro, name='delete_livro'),
    path('users', list_users, name='list_users'),
    path('cadastro_aluno', cadastro_aluno, name='cadastro_aluno'),
    path('cadastro_leitor', cadastro_leitor, name='cadastro_leitor'),
    path('cadastro_professor', cadastro_professor, name='cadastro_professor')
]