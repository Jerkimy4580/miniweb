from django.shortcuts import render, redirect
from .forms import ContactoForm
from .models import Contacto

def home(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactoForm()

    contactos = Contacto.objects.all()
    return render(request, "home.html", {"form": form, "contactos": contactos})
