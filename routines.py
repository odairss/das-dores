from datetime import datetime, timedelta, tzinfo, timezone
from bibliotecaeulina.mymodels import Cliente, Emprestimo

def set_multas():
    clientes = Cliente.objects.filter()
    for client in clientes:
        quant = Emprestimo.objects.filter(idcliente=client.idcliente).count()
        if quant > 0:
            emprestimo = Emprestimo.objects.filter(idcliente=client.idcliente).order_by('-datadevolucao')[0]
            print('Emprestimo: ',emprestimo.idemprestimo)
            hoje = datetime.now(timezone.utc) - timedelta(hours=3)
            if (emprestimo.datadevolvido is None) and emprestimo.datadevolucao < hoje:
                print('Tem multa')
                dtdelta = hoje - emprestimo.datadevolucao
                emprestimo.diasatrasados = dtdelta.days
                client.multa = dtdelta.days * 2
            if client.save():
                print('salvou')
            else:
                print('nao salvou')
            if emprestimo.save():
                print('salvou')
            else:
                print('nao salvou')
        else:
            print('Cliente ', client, ' ainda nao realizou emprestimos.')



def gerencia_multas():
    clientes = Cliente.objects.filter()
    for client in clientes:
        quant = Emprestimo.objects.filter(idcliente=client.idcliente,devolucao=True).count()
        if quant > 0:
            emprestimo = Emprestimo.objects.filter(idcliente=client.idcliente, devolucao=True).order_by('-datadevolvido')[0]
            print('Cliente: ',client, ', Dias atrasados: ', emprestimo.diasatrasados,'; ')
            if client.multa > 0:
                hoje = datetime.now(timezone.utc) - timedelta(hours=3)
                timedelta_multa = hoje - emprestimo.datadevolvido
                multa = timedelta_multa.days
                print('Dias para descontar da multa: ', multa)
                client.multa = client.multa - multa
                print('Multa atual de ',client, ' : ', client.multa)
                client.save()
        else:
            print('Cliente: ', client, ' nao tem livros devolvidos ')


gerencia_multas()
set_multas()
