from django.shortcuts import render


def index(request):
    return render(request,'index.xhtml')
    
    # HttpResponse('<h1>Receitas</h1> <h2>Seja Bemvindo!</h2>')


def receita(request):
    return render(request, 'receita.xhtml')
