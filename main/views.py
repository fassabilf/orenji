from django.shortcuts import render, redirect   # Tambahkan import redirect
from main.forms import OrenjiEntryForm         # Ganti MoodEntryForm dengan OrenjiEntryForm
from main.models import OrenjiEntry            # Ganti MoodEntry dengan OrenjiEntry

from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    form = OrenjiEntryForm(request.POST or None)  # Tambahkan ini untuk menangani form di halaman utama

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_main')  # Redirect ke halaman utama setelah produk ditambahkan

    orenji_entries = OrenjiEntry.objects.all()
    context = {'orenji_entries': orenji_entries, 'form': form}  # Kirim form ke template
    return render(request, 'main.html', context)


def create_orenji_entry(request):
    form = OrenjiEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')  # Sesuaikan dengan URL halaman yang ingin dituju setelah submit

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