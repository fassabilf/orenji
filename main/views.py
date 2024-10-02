from django.shortcuts import render, redirect   # Tambahkan import redirect
from main.forms import OrenjiEntryForm         # Ganti MoodEntryForm dengan OrenjiEntryForm
from main.models import OrenjiEntry            # Ganti MoodEntry dengan OrenjiEntry

from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


@login_required(login_url='/login')
def show_main(request):
    orenji_entries = OrenjiEntry.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP F',
        'npm': '2306224354',
        'orenji_entries': orenji_entries,  # Mengirim data produk yang dimiliki user yang login
        'last_login': request.COOKIES.get('last_login', 'No data available'),  # Mengambil cookies last_login jika ada
    }

    return render(request, "main.html", context)

def create_orenji_entry(request):
    form = OrenjiEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        orenji_entry = form.save(commit=False)
        orenji_entry.user = request.user  # Hubungkan produk dengan pengguna yang sedang login
        orenji_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_orenji_entry.html", context)

def show_xml(request):
    data = OrenjiEntry.objects.all()  # Mengambil semua entri dari model OrenjiEntry
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = OrenjiEntry.objects.all()  # Mengambil semua data dari model OrenjiEntry
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = OrenjiEntry.objects.filter(pk=id)  # Mengambil entri berdasarkan primary key (ID)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = OrenjiEntry.objects.filter(pk=id)  # Mengambil entri berdasarkan primary key (ID)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/login')
def edit_orenji_entry(request, id):
    orenji_entry = get_object_or_404(OrenjiEntry, id=id)
    form = OrenjiEntryForm(request.POST or None, instance=orenji_entry)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_main')

    context = {'form': form, 'is_edit': True}
    return render(request, 'create_orenji_entry.html', context)

@login_required(login_url='/login')
def delete_orenji_entry(request, id):
    orenji_entry = get_object_or_404(OrenjiEntry, id=id)
    
    if request.method == "POST":
        orenji_entry.delete()
        return redirect('main:show_main')

    context = {'orenji_entry': orenji_entry}
    return render(request, 'delete_confirmation.html', context)
