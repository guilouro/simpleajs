from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.generic import ListView
from .models import *



def home(request):
	return render(request, 'index.html')


class ContactList(ListView):
	""" Cria uma lista de todos os contatos """
	template_name = 'contact/contact.html'
	model = Contact
	paginate_by = 1


def get_data(request):
	contato = Contact.objects.all()
	retorno = serializers.serialize("json", contato)
	return HttpResponse(retorno)