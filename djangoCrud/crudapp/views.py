from django.shortcuts import render, redirect, get_object_or_404
from .models import contact
from .form import contactForm
from django.views.generic import ListView, DetailView


# Create your views here.

class IndexView(ListView):
    template_name = 'crudapp/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return contact.objects.all()

class ContactDetailView(DetailView):
    model = contact
    template_name = 'crudapp/contact-detail.html'

def create(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = contactForm()

    return render(request,'crudapp/create.html',{'form': form})


def edit(request, pk, template_name='crudapp/edit.html'):
    contact = get_object_or_404(contact, pk=pk)
    form = contactForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    contact = get_object_or_404(contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})