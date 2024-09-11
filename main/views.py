from django.shortcuts import render

def show_main(request):
    identitas = {
        'nama': 'Faiz Assabil Firdaus',
        'npm': '2306224354',
        'kelas': 'F'
    }
    context = {
        'product_name': 'materai 2500',
        'price': 2000,
        'description': 'materai 2500 tapi diskon mahalnya di ongkir',
        'stock': 2
    }

    context.update(identitas)

    return render(request, "main.html", context)
