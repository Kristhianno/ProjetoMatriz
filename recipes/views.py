from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Efraim Kristhianno',
    })

def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Efraim Kristhianno',
    })
