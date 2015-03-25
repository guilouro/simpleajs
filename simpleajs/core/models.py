# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _



""" List of values for use in choices. """

list_gender = [('M', 'masculino'), ('F', 'feminino')]


class Contact(models.Model):
	gender = models.CharField(_(u'gênero'), max_length=1, choices=list_gender)
	first_name = models.CharField(_('nome'), max_length=50)
	last_name = models.CharField(_('sobrenome'), max_length=50)

	class Meta:
		ordering = ['first_name']
		verbose_name='Novo'
		verbose_name_plural='Novos'

	def __str__(self):
		return self.first_name

