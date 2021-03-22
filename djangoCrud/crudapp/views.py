from django.shortcuts import render, redirect, get_object_or_404
from .models import contact
from .forms import contactForm
from django.views.generic import ListView, DetailView


# Create your views here.

class indexView(ListView):
    template_name = 'crudapp/index.html'
    context_object_name = 'contact_list'

    def def get_queryset(self):
        return contact.object.all()

class contactDetailView(DetailView):
    model = contact
    template_name = 'crudapp/contact-detail.html'


def edit(request, pk, template_name='crudapp/edit.html'):
    contact = get_object_or_404(contact, pk=pk)
    form = contactForm(request.POST or None, instance=post)
    if from.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    contact = get_object_or_404(contact, pk=pk)
    if request.method = 'POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})