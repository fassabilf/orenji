
Nama : Faiz Assabil Firdaus  
NPM : 2306224354  
Kelas : PBP F

# List of Contents
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)
- [Tugas 5](#tugas-5)

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

# Tugas 3

## **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Sama halnya seperti interaksi antar orang, kita akan menyimpan dan memberikan informasi yang penting. Maka dari itu, dalam sebuah platform, diperlukan adanya interaksi informasi tersebut, yang mencakup proses menyimpan dan mengirim data. Data delivery memungkinkan informasi tersebut dapat berpindah dari satu tempat ke tempat lain dengan aman dan efisien.

---

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik karena strukturnya yang sederhana dan mirip dengan dictionary pada Python, sehingga lebih mudah dibaca dan ditulis oleh manusia serta lebih efisien dalam proses pengiriman data. JSON menggunakan format berbasis teks yang ringan, dengan key-value pairs yang membuatnya lebih ringkas dibandingkan XML, yang memiliki banyak tag pembuka dan penutup. Selain itu, JSON lebih mudah diparse oleh browser dan aplikasi modern. Oleh karena itu, JSON lebih populer dibandingkan XML karena lebih praktis dan mudah digunakan dalam pengembangan web dan aplikasi modern.

**Struktur JSON:**

```json
{
    "product_name": "Orenji Juice",
    "price": 15000,
    "stock": 20
}
```

**Struktur XML:**

```xml
<product>
    <product_name>Orenji Juice</product_name>
    <price>15000</price>
    <stock>20</stock>
</product>
```

---

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang diinputkan melalui form sesuai dengan aturan dan validasi yang telah ditetapkan pada model atau form itu sendiri. Method ini akan mengembalikan nilai `True` jika semua data yang diisi valid, dan `False` jika ada data yang tidak sesuai. Kita membutuhkan method ini untuk memastikan data yang dikirimkan oleh pengguna adalah valid sebelum disimpan ke database atau diproses lebih lanjut oleh aplikasi.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` diperlukan saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang bisa memanfaatkan sesi pengguna yang sah untuk melakukan permintaan berbahaya tanpa sepengetahuan mereka. Jika `csrf_token` tidak ditambahkan, aplikasi menjadi rentan terhadap serangan ini, dan penyerang bisa melakukan tindakan berbahaya seperti perubahan data atau transaksi secara ilegal dengan menggunakan identitas pengguna. Tanpa token ini, aplikasi tidak dapat membedakan permintaan yang sah dari pengguna atau yang dimanipulasi oleh pihak ketiga.

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**

1. **Membuat `forms.py` di folder `main` untuk membuat form produk (`OrenjiEntryForm`)**

    ```python
    from django import forms
    from .models import OrenjiEntry

    class OrenjiEntryForm(forms.ModelForm):
        class Meta:
            model = OrenjiEntry
            fields = ['product_name', 'price', 'descriptions', 'stock']
    ```

2. **Membuat fungsi `create_orenji_entry` di `views.py` untuk menambahkan produk**

    ```python
    from django.shortcuts import render, redirect
    from .forms import OrenjiEntryForm

    def create_orenji_entry(request):
        form = OrenjiEntryForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, 'create_orenji_entry.html', context)
    ```

3. **Membuat `create_orenji_entry.html` di folder `templates/main` untuk menampilkan form produk**

    ```html
    <h1>Add New Product Entry</h1>

    <form method="POST">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></

td>
          <td>
            <input type="submit" value="Add Product" />
          </td>
        </tr>
      </table>
    </form>
    ```

4. **Menambahkan `csrf_token` pada form di `create_orenji_entry.html` untuk mencegah serangan CSRF**

5. **Menambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` di `views.py` untuk menampilkan data dalam format XML dan JSON**

    ```python
    from django.http import HttpResponse
    from django.core import serializers

    def show_xml(request):
        data = OrenjiEntry.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = OrenjiEntry.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = OrenjiEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = OrenjiEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

6. **Membuat `urls.py` di folder `main` untuk melakukan routing**

    ```python
    from django.urls import path
    from main.views import show_main, create_orenji_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('add-product/', create_orenji_entry, name='add_product'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

---

## Screenshot hasil menggunakan Postman:

- Show XML: ![./assets/postman_xml](./assets/postman_xml.png)
- Show JSON: ![./assets/postman_json](./assets/postman_json.png)
- Show XML by ID: ![./assets/postman_xml_id](./assets/postman_xml_id.png)
- Show JSON by ID: ![./assets/postman_json_id](./assets/postman_json_id.png)

# Tugas 3

## Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?

### Perbedaan:
1. **HttpResponseRedirect()**: 
   `HttpResponseRedirect()` adalah objek response yang mengarahkan pengguna ke URL lain. Saat kita memanggil fungsi ini, kita harus memberikan URL tujuan sebagai argumen, misalnya:

   ```python
   return HttpResponseRedirect('/some-url/')
   ```

   **Contoh penggunaan**:
   ```python
   from django.http import HttpResponseRedirect
   def my_view(request):
       return HttpResponseRedirect('/another-url/')
   ```

2. **redirect()**:
   `redirect()` adalah shortcut di Django yang mempermudah pengalihan pengguna ke URL atau view tertentu. Kita dapat menggunakan nama URL atau memberikan instance model sebagai argumen, dan Django akan otomatis mencari URL tujuan yang tepat.

   **Contoh penggunaan**:
   ```python
   from django.shortcuts import redirect
   def my_view(request):
       return redirect('url_name')
   ```

   **Kesimpulan**:
   - `HttpResponseRedirect()` hanya menerima URL sebagai argumen.
   - `redirect()` lebih fleksibel, karena dapat menerima nama URL, objek model, atau bahkan string URL, sehingga lebih umum digunakan dalam aplikasi Django.

## Jelaskan cara kerja penghubungan model `Product` dengan `User`!

### Penghubungan Model:
Penghubungan antara `Product` dan `User` dilakukan melalui relasi `ForeignKey`. Ini memungkinkan setiap entri produk (`Product`) terhubung dengan pengguna (`User`) yang membuatnya.

### Cara Kerja:
1. **Tambahkan `ForeignKey` ke Model**: 
   Di model `Product`, tambahkan field `user` yang mengacu pada model `User` dengan `ForeignKey`. Hal ini menciptakan relasi satu ke banyak antara `User` dan `Product`.

   **Contoh Implementasi**:
   ```python
   from django.contrib.auth.models import User
   from django.db import models
   from django.contrib.auth.models import User
   
   class OrenjiEntry(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
   ```

2. **Cara Kerja**:
   - Saat pengguna membuat OrenjiEntry (yang berisi produk), produk tersebut akan disimpan dengan referensi ke pengguna yang sedang login (`request.user`).
   - Dengan demikian, setiap produk dihubungkan dengan pengguna tertentu, memungkinkan pengambilan data produk yang terkait dengan pengguna tersebut.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

### Authentication vs Authorization:
1. **Authentication (Otentikasi)**:
   - Otentikasi adalah proses memverifikasi identitas pengguna, biasanya melalui username dan password. Saat pengguna login, sistem memastikan apakah identitas pengguna benar dan sesuai.

   **Di Django**:
   - Proses otentikasi diimplementasikan menggunakan fungsi `authenticate()` dan `login()`. Django menyediakan form otentikasi standar yang memverifikasi kredensial pengguna.
   
2. **Authorization (Otorisasi)**:
   - Otorisasi adalah proses menentukan apa yang boleh dilakukan oleh pengguna setelah mereka terotentikasi. Setelah pengguna berhasil login, sistem menentukan hak akses mereka ke sumber daya tertentu.

   **Di Django**:
   - Django mengelola otorisasi melalui permissions dan decorators seperti `@login_required` untuk membatasi akses halaman hanya bagi pengguna yang sudah login.
   
### Saat Pengguna Login:
- Django akan melakukan **authentication** dengan memeriksa username dan password melalui `authenticate()`. Jika valid, Django akan menciptakan session untuk pengguna dan menyimpan informasi login mereka menggunakan `login()`.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

### Cara Django Mengingat Pengguna:
- Django menggunakan **session** dan **cookies** untuk mengingat pengguna yang login. Setelah pengguna berhasil login, Django akan membuat session ID yang unik dan menyimpannya di browser pengguna dalam bentuk **cookie** bernama `sessionid`. Di server, session ini digunakan untuk melacak status login pengguna.

### Kegunaan Lain dari Cookies:
Selain mengingat pengguna yang login, cookies juga dapat digunakan untuk:
1. **Melacak preferensi pengguna** (seperti tema atau pengaturan bahasa).
2. **Menyimpan data sementara** yang diperlukan antar halaman.
3. **Membuat pengalaman pengguna lebih personal** dengan menyimpan informasi tertentu secara lokal di browser.

### Keamanan Cookies:
Tidak semua cookies aman digunakan. Cookies dapat digunakan untuk:
- **Session hijacking** jika session cookies tidak dilindungi dengan benar.
- Untuk menjaga keamanan cookies, Django menyediakan fitur seperti:
  - **`HttpOnly`**: Membatasi akses ke cookie melalui JavaScript, mencegah serangan XSS (Cross-Site Scripting).
  - **`Secure`**: Mengirim cookies hanya melalui HTTPS, menjaga keamanan cookies saat ditransmisikan.
  - **`CSRF Token`**: Melindungi aplikasi dari serangan CSRF dengan memvalidasi permintaan POST melalui token.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

### Langkah-langkah Implementasi Checklist:

1. **Membuat Form Registrasi, Login, dan Logout**:
   - Membuat fungsi `register_user()`, `login_user()`, dan `logout_user()` di `views.py` untuk menangani proses registrasi, login, dan logout pengguna. Saya juga menggunakan `UserCreationForm` untuk mempermudah pembuatan akun.

2. **Membuat Akun Pengguna dan Dummy Data**:
   - Saya menambahkan dua akun pengguna dan membuat tiga entri produk untuk masing-masing akun. Data produk disimpan menggunakan form `OrenjiEntryForm`.

3. **Menghubungkan Model `OrenjiEntry` dengan `User`**:
   - Saya menambahkan `ForeignKey` pada model `OrenjiEntry` untuk menghubungkannya dengan model `User`, memastikan bahwa setiap produk yang dibuat oleh pengguna memiliki referensi ke pengguna tersebut.

4. **Menampilkan Informasi Pengguna yang Login**:
   - Saya menggunakan `request.user.username` di `views.py` untuk menampilkan informasi pengguna yang sedang login di halaman utama (`main.html`), serta menambahkan cookie `last_login` untuk menampilkan kapan terakhir kali pengguna login.

5. **Menggunakan Cookies untuk Menyimpan Last Login**:
   - Pada saat login, saya menggunakan `response.set_cookie()` untuk menyimpan waktu terakhir kali pengguna login di cookie `last_login` dan menampilkannya di halaman utama.

Berikut adalah penjelasan yang lebih lengkap dan rapi untuk README.md yang mencakup jawaban atas pertanyaan-pertanyaan yang kamu ajukan:

---

# Tugas 5

## **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

Dalam CSS, urutan prioritas pengambilan selector disebut **Specificity**. Berikut adalah urutan prioritas yang menentukan selector mana yang akan diterapkan pada elemen:

1. **Inline Styles**: Gaya yang ditulis langsung di elemen HTML memiliki prioritas tertinggi. Contoh:
   ```html
   <p style="color: red;">Text</p>
   ```

2. **ID Selector**: Selector yang menggunakan ID memiliki prioritas lebih tinggi daripada class atau tag. Contoh:
   ```css
   #header {
       color: blue;
   }
   ```

3. **Class, Pseudo-class, dan Attribute Selectors**: Selector ini memiliki prioritas lebih rendah daripada ID, tetapi lebih tinggi daripada selector elemen. Contoh:
   ```css
   .header {
       color: green;
   }
   ```

4. **Tag/Element Selector**: Selector ini memiliki prioritas terendah. Contoh:
   ```css
   p {
       color: black;
   }
   ```

Jika ada konflik antara selector, yang memiliki spesifikitas lebih tinggi akan diambil. Jika spesifikasinya sama, selector yang ditulis terakhir akan digunakan.

---

## **Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

**Responsive design** adalah pendekatan desain web yang memastikan tampilan halaman web dapat beradaptasi dengan baik di berbagai ukuran layar, mulai dari desktop hingga perangkat seluler. Responsive design sangat penting karena:

- **Pengguna beragam perangkat**: Saat ini, pengguna mengakses web dari berbagai perangkat seperti ponsel, tablet, dan desktop, sehingga tampilan harus konsisten dan mudah digunakan di berbagai ukuran layar.
- **SEO (Search Engine Optimization)**: Google memberikan preferensi lebih tinggi pada situs web yang mobile-friendly dalam peringkat pencariannya.
- **Pengalaman pengguna**: Desain yang responsif memberikan pengalaman pengguna yang optimal, yang berpotensi meningkatkan tingkat konversi dan interaksi pengguna.

### Contoh:
- **Sudah menerapkan responsive design**: **Instagram**, yang menyesuaikan layout secara otomatis pada berbagai ukuran layar.
- **Belum menerapkan responsive design**: **Situs-situs lama** atau situs web yang tidak dioptimalkan, seperti beberapa situs pemerintahan, yang tidak dirancang untuk tampilan mobile-friendly.

---

## **Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

- **Margin**: Jarak di luar elemen yang mengatur ruang antara elemen tersebut dan elemen lainnya di luar kotaknya. **Margin** tidak memiliki warna dan bersifat transparan.
   ```css
   .element {
       margin: 20px;
   }
   ```

- **Border**: Garis yang mengelilingi elemen, berada di antara padding dan margin. **Border** memiliki warna dan dapat diatur ketebalannya.
   ```css
   .element {
       border: 2px solid black;
   }
   ```

- **Padding**: Ruang di dalam elemen antara konten dan batas elemen (border). **Padding** bersifat transparan dan mengatur jarak di dalam elemen itu sendiri.
   ```css
   .element {
       padding: 15px;
   }
   ```

Secara singkat, **padding** mengatur jarak dalam elemen, **border** berada di sekitar elemen, dan **margin** mengatur jarak antara elemen dengan elemen lainnya.

---

## **Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

### **Flexbox**:
**Flexbox** (Flexible Box) adalah metode tata letak yang digunakan untuk mengatur dan menyelaraskan item dalam satu dimensi (baris atau kolom). Flexbox berguna untuk membuat tata letak yang responsif dan adaptif.

Contoh Flexbox:
```css
.container {
    display: flex;
    justify-content: space-between; /* Mengatur jarak antar item */
    align-items: center; /* Menyelaraskan item secara vertikal */
}
```

### **Grid Layout**:
**CSS Grid** adalah sistem tata letak dua dimensi yang memungkinkan untuk mendefinisikan struktur grid dan menempatkan elemen di baris dan kolom. Grid sangat berguna untuk membuat tata letak kompleks yang melibatkan banyak baris dan kolom.

Contoh CSS Grid:
```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; /* Membuat 3 kolom dengan ukuran yang sama */
    grid-template-rows: auto; /* Baris akan otomatis disesuaikan */
}
```

**Kegunaan**:
- **Flexbox**: Lebih cocok untuk tata letak satu dimensi (baris atau kolom).
- **Grid Layout**: Lebih cocok untuk tata letak dua dimensi yang kompleks (baris dan kolom).

---

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**

1. **Menambahkan Fungsi Hapus dan Edit Produk**:
   - Saya menambahkan dua view baru, yaitu `edit_orenji_entry()` dan `delete_orenji_entry()` untuk mengelola fungsi edit dan hapus produk.
   - URL pattern diperbarui untuk mendukung UUID sebagai identifier produk.

2. **Kustomisasi Tampilan dengan CSS**:
   - Saya menambahkan Bootstrap ke proyek untuk mempercepat pengembangan layout responsif.
   - Menggunakan Flexbox dan Grid Layout untuk mengatur tata letak produk, membuat tampilan lebih dinamis di perangkat mobile.

3. **Kustomisasi Halaman Login, Register, dan Tambah Produk**:
   - Saya memperbarui template HTML untuk halaman login, register, dan tambah produk dengan menggunakan Bootstrap dan custom CSS agar tampilannya lebih menarik dan user-friendly.

4. **Menambahkan Responsive Design pada Daftar Produk**:
   - Menggunakan card Bootstrap dan Flexbox untuk menampilkan produk dalam layout yang responsif.
   - Jika tidak ada produk yang tersedia, saya menampilkan gambar placeholder dan pesan yang menjelaskan bahwa tidak ada produk terdaftar.

5. **Menambahkan Tombol Edit dan Hapus di Card Produk**:
   - Setiap produk memiliki tombol **Edit** dan **Delete**. Tombol ini akan membuka halaman edit atau menghapus produk terkait setelah dikonfirmasi.

6. **Membuat Navbar yang Responsif**:
   - Saya menambahkan navbar responsif dengan Bootstrap, sehingga menyesuaikan tampilannya di berbagai ukuran layar.

---
