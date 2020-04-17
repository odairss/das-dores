from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="index"),

    path('usuarios', views.list_usuarios, name='list_usuarios'),
    path('usuario/<int:idusuario>/', views.usuario, name='buscar_usuario'),
    path('update_usuario/<int:idusuario>/', views.update_usuario, name='update_usuario'),
    path('delete_usuario/<int:idusuario>/',views.delete_usuario, name='delete_usuario'),
    path('cadastro_usuario', views.cadastro_usuario, name='cadastro_usuario'),

    path('clientes', views.list_clientes, name='list_clientes'),
    path('cliente/<int:idcliente>/', views.cliente, name='buscar_cliente'),
    path('update_cliente/<int:idcliente>/', views.update_cliente, name='update_cliente'),
    path('delete_cliente/<int:idcliente>/',views.delete_cliente, name='delete_cliente'),
    path('cadastro_cliente', views.cadastro_cliente, name='cadastro_cliente'),
    path('cliente/<int:idcliente>/historico',views.historico,name='historico'),

    path('cadastro_livro', views.cadastro_livro, name='new'),
    path('update_livro/<int:idlivro>/', views.update_livro, name='update_livro'),
    path('delete_livro/<int:idlivro>/', views.delete_livro, name='delete_livro'),
    path('acervo', views.acervo, name="ver_acervo"),
    path('livro/<int:idlivro>/', views.livro, name="buscar_livro"),
    path('livro/<int:idlivro>/detalhes/', views.detalhes_livro, name="detalhes_livro"),

    path('cadastro_exemplar', views.cadastro_exemplar, name='cadastro_exemplar'),
    path('update_exemplar/<int:idexemplar>/', views.update_exemplar, name='update_exemplar'),
    path('delete_exemplar/<int:idexemplar>/', views.delete_exemplar, name='delete_exemplar'),
    path('exemplares', views.exemplares, name="exemplares"),
    path('exemplar/<int:idexemplar>/', views.exemplar, name="buscar_exemplar"),
    path('emprestar/exemplar/<int:idexemplar>/', views.emprestar_exemplar, name="emprestar_exemplar"),

    path('autores', views.list_autores, name='list_autores'),
    path('autor/<int:idautor>/', views.autor, name='buscar_autor'),
    path('update_autor/<int:idautor>/', views.update_autor, name='update_autor'),
    path('delete_autor/<int:idautor>/',views.delete_autor, name='delete_autor'),
    path('cadastro_autor', views.cadastro_autor, name='cadastro_autor'),

    path('emprestimos', views.list_emprestimos, name='list_emprestimos'),
    path('emprestimo/<int:idemprestimo>/', views.emprestimo, name='buscar_emprestimo'),
    path('update_emprestimo/<int:idemprestimo>/', views.update_emprestimo, name='update_emprestimo'),
    path('delete_emprestimo/<int:idemprestimo>/',views.delete_emprestimo, name='delete_emprestimo'),
    path('cadastro_emprestimo', views.cadastro_emprestimo, name='cadastro_emprestimo'),
    path('emprestimo/devolver/<int:idemprestimo>/', views.devolver, name='devolver'),

    path('login',views.login_user,name="login"),
#    path('submit',views.submit,name="submit"),
    path('logout',views.logout_user,name='logout'),
#    path('teste',views.teste,name='teste'),
#    path('testelogin',views.testelogin,name='testelogin')
]