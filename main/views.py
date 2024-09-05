from django.shortcuts import render
def show_main(request):
    context = {
        'name' : 'materai 2500',
        'price': 2000,
        'description': 'materai 2500 tapi diskon mahalnya di ongkir',
        'stock' : 2
    }

    return render(request, "main.html", context)
