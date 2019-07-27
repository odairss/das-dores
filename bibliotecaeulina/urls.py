from django.urls import path
from .views import login_user, submit,logout_user, home,livro,acervo,cadastro_livro,update_livro, update_usuario,\
    list_usuarios,cadastro_usuario, usuario,delete_livro, delete_usuario,teste,testelogin, list_autores,autor,update_autor,\
    delete_autor,cadastro_autor, list_emprestimos, emprestimo, update_emprestimo, delete_emprestimo, cadastro_emprestimo,\
    list_clientes,cliente,update_cliente,delete_cliente,cadastro_cliente


urlpatterns = [
    path('', home, name="index"),

    path('usuarios', list_usuarios, name='list_usuarios'),
    path('usuario/<int:idusuario>/', usuario, name='buscar_usuario'),
    path('update_usuario/<int:idusuario>/', update_usuario, name='update_usuario'),
    path('delete_usuario/<int:idusuario>/',delete_usuario, name='delete_usuario'),
    path('cadastro_usuario', cadastro_usuario, name='cadastro_usuario'),

    path('clientes', list_clientes, name='list_clientes'),
    path('cliente/<int:idcliente>/', cliente, name='buscar_cliente'),
    path('update_cliente/<int:idcliente>/', update_cliente, name='update_cliente'),
    path('delete_cliente/<int:idcliente>/',delete_cliente, name='delete_cliente'),
    path('cadastro_cliente', cadastro_cliente, name='cadastro_cliente'),

    path('cadastro_livro', cadastro_livro, name='new'),
    path('update_livro/<int:idlivro>/', update_livro, name='update_livro'),
    path('delete_livro/<int:idlivro>/', delete_livro, name='delete_livro'),
    path('acervo', acervo, name="ver_acervo"),
    path('livro/<int:idlivro>/', livro, name="buscar_livro"),

    path('autores', list_autores, name='list_autores'),
    path('autor/<int:idautor>/', autor, name='buscar_autor'),
    path('update_autor/<int:idautor>/', update_autor, name='update_autor'),
    path('delete_autor/<int:idautor>/',delete_autor, name='delete_autor'),
    path('cadastro_autor', cadastro_autor, name='cadastro_autor'),

    path('emprestimos', list_emprestimos, name='list_emprestimos'),
    path('emprestimo/<int:idemprestimo>/', emprestimo, name='buscar_emprestimo'),
    path('update_emprestimo/<int:idemprestimo>/', update_emprestimo, name='update_emprestimo'),
    path('delete_emprestimo/<int:idemprestimo>/',delete_emprestimo, name='delete_emprestimo'),
    path('cadastro_emprestimo', cadastro_emprestimo, name='cadastro_emprestimo'),

    path('login',login_user,name="login"),
    path('submit',submit,name="submit"),
    path('logout',logout_user,name='logout'),
    path('teste',teste,name='teste'),
    path('testelogin',testelogin,name='testelogin')
]