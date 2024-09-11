Nama : Faiz Assabil Firdaus  
NPM : 2306224354  
Kelas : PBP F

# Tugas 2

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)?

### 1. Membuat sebuah proyek Django baru

```bash
django-admin startproject orenji .
```

### 2. Membuat aplikasi dengan nama `main` pada proyek tersebut

```bash
python manage.py startapp main
```

### 3. Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut

- Kode untuk model `Product` yang dibuat pada `main/models.py`:

```python
from django.db import models

class OrenjiEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    descriptions = models.TextField()
    stock = models.IntegerField()

    @property
    def is_can_buy(self):
        return self.stock > 0
```

### 4. Membuat fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML

- Kode untuk fungsi `show_main` pada `main/views.py`:

```python
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
```

### 5. Membuat template HTML untuk menampilkan informasi

- Kode untuk `main/templates/main.html`:

```html
<h5>Nama Produk: </h5>
<p>{{ product_name }}</p>

<h5>Harganya: </h5>
<p>{{ price }}</p>

<h5>Deskripsi Produk: </h5>
<p>{{ description }}</p>

<h5>Stock: </h5>
<p>{{ stock }}</p>

<h5>Nama Pemilik Produk: </h5>
<p>{{ nama }}</p>

<h5>NPM Pemilik Produk: </h5>
<p>{{ npm }}</p>

<h5>Kelas Pemilik Produk: </h5>
<p>{{ kelas }}</p>
```

### 6. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`

- Kode untuk `orenji/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

### 7. Membuat routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`

- Kode untuk `main/urls.py`:

```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html


![Bagan Request dan Response](bagan.png)

## Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git dalam pengembangan perangkat lunak berfungsi seperti Google Docs dalam mengerjakan PR secara bersama-sama. Git menjadi tempat untuk berkolaborasi dalam pengembangan perangkat lunak, mirip seperti Google Drive atau Google Docs yang berfungsi sebagai wadah penyimpanan dan kolaborasi dokumen. Dengan Git, proyek pengembangan perangkat lunak dapat dikelola dengan lebih baik dan terintegrasi, sehingga memastikan proyek berjalan dengan lancar.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Hal ini dikarenakan Django merupakan framework berbasis Python, yang bahasanya dekat dengan kita dan terkenal mudah dipelajari, terutama bagi pemula. Python sendiri memiliki sintaks yang sederhana dan mudah dipahami, sehingga mempermudah transisi dalam memahami konsep-konsep pengembangan web.

Namun, tidak hanya sekadar mudah dimengerti, Django juga merupakan framework yang sangat kuat dan scalable. Django digunakan pada aplikasi terkenal seperti Instagram, Spotify, dan YouTube, yang menunjukkan bahwa framework ini mampu menangani kebutuhan pengembangan perangkat lunak dalam skala besar dan kompleks. Django juga dilengkapi dengan banyak fitur bawaan seperti sistem otentikasi, manajemen basis data, dan keamanan, yang mempermudah proses pengembangan tanpa harus membangun semuanya dari awal.

## Mengapa model pada Django disebut sebagai ORM?

Selaras dengan arti Object Relational Mapping, yang berfungsi sebagai jembatan antara object-oriented programming dan basis data relasional, model pada Django berfungsi untuk menjembatani antara database dan objek-objek Python. Model Django memungkinkan pengembang untuk bekerja dengan database menggunakan kode Python yang berorientasi objek, sehingga mempermudah manipulasi dan interaksi dengan data tanpa harus menulis query SQL secara langsung.