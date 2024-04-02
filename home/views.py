from django.shortcuts import render, redirect
from .models import Cliente
from .forms.form import MeuFormulario

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {'clientes': get_all()})

def get_all():
    return Cliente.objects.all()

def delete_one(request, id):
    Cliente.objects.get(id=id).delete()
    return redirect(index)

def handle_form(request, id=None):
    if(request.method == 'GET'):
        return handle_page(request, id)

    elif( request.method == 'POST'):


       return handle_req(request)


def handle_page(req, id):

    if(id):
        cliente = Cliente.objects.get(id=id)
        formulario = MeuFormulario(initial={'genero': cliente.genero, 'estado': cliente.estado})
        return render(req, 'pages/novo.html', {'form': formulario, 'cliente': cliente})

    else:
        return render(req, 'pages/novo.html', {'form': MeuFormulario()})

def handle_req(req):

    if (req.POST.get('id')):
        cliente = Cliente.objects.get(id=req.POST.get('id'))
        cliente.nome= req.POST.get('nome')
        cliente.dtNasc= req.POST.get('dtNasc')
        cliente.email= req.POST.get('email')
        cliente.genero =  req.POST.get('genero')
        cliente.telefone= req.POST.get('telefone')
        cliente.estado =  req.POST.get('estado')

    else:
        cliente = Cliente(
        nome= req.POST.get('nome')
        ,dtNasc= req.POST.get('dtNasc')
        ,email= req.POST.get('email')
        ,genero =  req.POST.get('genero')
        ,telefone= req.POST.get('telefone')
        ,estado =  req.POST.get('estado'))


    cliente.save()
    return redirect(index)


def search(request):

    busca =  request.GET['search']
    clientes = Cliente.objects.filter(nome__icontains=busca)
    return render(request, 'pages/index.html', {'clientes': clientes})

def gerarDadosFicticios(request):
    clientes = [
       {
           "nome": "João Silva",
           "dtNasc": "1985-03-15",
           "email": "joao.silva@email.com",
           "telefone": "(11) 98765-4321",
           "estado": "SP",
           "genero": "Masculino"
       },
       {
           "nome": "Maria Santos",
           "dtNasc": "1990-08-22",
           "email": "maria.santos@email.com",
           "telefone": "(21) 98765-1234",
           "estado": "RJ",
           "genero": "Feminino"
       },
       {
           "nome": "André Oliveira",
           "dtNasc": "1982-11-10",
           "email": "andre.oliveira@email.com",
           "telefone": "(31) 99876-5432",
           "estado": "MG",
           "genero": "Masculino"
       },
         {
           "nome": "Carla Ferreira",
           "dtNasc": "1993-05-20",
           "email": "carla.ferreira@email.com",
           "telefone": "(62) 98765-4321",
           "estado": "GO",
           "genero": "Feminino"
       },
       {
           "nome": "Rafael Almeida",
           "dtNasc": "1980-11-08",
           "email": "rafael.almeida@email.com",
           "telefone": "(27) 99876-5432",
           "estado": "ES",
           "genero": "Masculino"
       },
       {
           "nome": "Lúcia Oliveira",
           "dtNasc": "1977-09-12",
           "email": "lucia.oliveira@email.com",
           "telefone": "(85) 98765-1234",
           "estado": "CE",
           "genero": "Feminino"
       },
       {
           "nome": "Gustavo Santos",
           "dtNasc": "1998-02-28",
           "email": "gustavo.santos@email.com",
           "telefone": "(48) 99876-9876",
           "estado": "SC",
           "genero": "Masculino"
       },
       {
           "nome": "Camila Rodrigues",
           "dtNasc": "1991-07-03",
           "email": "camila.rodrigues@email.com",
           "telefone": "(31) 98765-5678",
           "estado": "MG",
           "genero": "Feminino"
       },{
        "nome": "Ana Oliveira",
        "dtNasc": "1988-04-18",
        "email": "ana.oliveira@email.com",
        "telefone": "(11) 98765-4321",
        "estado": "SP",
        "genero": "Feminino"
        },
    {
        "nome": "Pedro Santos",
        "dtNasc": "1995-09-05",
        "email": "pedro.santos@email.com",
        "telefone": "(21) 98765-1234",
        "estado": "RJ",
        "genero": "Masculino"
    },
    {
        "nome": "Mariana Silva",
        "dtNasc": "1983-12-30",
        "email": "mariana.silva@email.com",
        "telefone": "(31) 99876-5432",
        "estado": "MG",
        "genero": "Feminino"
    },
    {
        "nome": "Lucas Almeida",
        "dtNasc": "1992-06-15",
        "email": "lucas.almeida@email.com",
        "telefone": "(62) 98765-4321",
        "estado": "GO",
        "genero": "Masculino"
    },
    {
        "nome": "Isabela Rodrigues",
        "dtNasc": "1981-10-25",
        "email": "isabela.rodrigues@email.com",
        "telefone": "(27) 99876-5432",
        "estado": "ES",
        "genero": "Feminino"
    },
    {
        "nome": "Fernando Costa",
        "dtNasc": "1979-07-20",
        "email": "fernando.costa@email.com",
        "telefone": "(85) 98765-1234",
        "estado": "CE",
        "genero": "Masculino"
    },
    {
        "nome": "Carolina Lima",
        "dtNasc": "1997-03-12",
        "email": "carolina.lima@email.com",
        "telefone": "(48) 99876-9876",
        "estado": "SC",
        "genero": "Feminino"
    },
    {
        "nome": "Ricardo Fernandes",
        "dtNasc": "1990-08-08",
        "email": "ricardo.fernandes@email.com",
        "telefone": "(31) 98765-5678",
        "estado": "MG",
        "genero": "Masculino"
    },
    {
        "nome": "Juliana Pereira",
        "dtNasc": "1986-05-02",
        "email": "juliana.pereira@email.com",
        "telefone": "(11) 98765-4321",
        "estado": "SP",
        "genero": "Feminino"
    },
    {
        "nome": "Diego Souza",
        "dtNasc": "1993-11-17",
        "email": "diego.souza@email.com",
        "telefone": "(21) 98765-1234",
        "estado": "RJ",
        "genero": "Masculino"
    }
    ]
    for dado in clientes:
        Cliente(
        nome= dado['nome']
        ,dtNasc= dado['dtNasc']
        ,email= dado['email']
        ,genero =  dado['genero']
        ,telefone= dado['telefone']
        ,estado =  dado['estado']).save()

    return redirect(index)



