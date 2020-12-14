from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

def test_context(request):
    context = {
        'title': 'добро пожаловать',
        'username': 'Vasilisa',
        'products': [
            {'name': 'Пальто', 'price': '14 300 руб.'},
            {'name': 'Блуза', 'price': '7 500 руб.'}
        ],
        'promotion': True,
        'prom_products': [
            {'name': 'Туфли', 'price': '11 200 руб.'}
        ],
    }


    return render(request, 'mainapp/context.html', context)
