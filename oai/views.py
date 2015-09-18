# -*- coding: ISO-8859-1 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from oaipmh import server, client, common, metadata, error
from repositories.models import Repository
from oai.server import CLOUAI

# Metadata registry
metadata_registry = metadata.MetadataRegistry()
metadata_registry.registerWriter('oai_dc', server.oai_dc_writer)

# Clouai server

from pprint import pprint
import inspect

# Index page
def index(request, repository_name=None):
	subdomain = request.META['HTTP_HOST'].split('.')[0]

	if repository_name is None:

		if subdomain is None:
			return redirect('/')

		if subdomain == 'www':
			return redirect('/')

		repository_name = subdomain

	# search repository by name
	try:
		repository = Repository.objects.get(name=repository_name)
		clouai = server.Server(CLOUAI(repository.id), metadata_registry)
		verb = str(request.GET.get('verb'))
		metadataPrefix = str(request.GET.get('metadataPrefix'))
		set = str(request.GET.get('set'))
		print inspect.getmembers(clouai, predicate=inspect.ismethod)
		print clouai.__dict__
		print dir(clouai)
		pprint(clouai)
		parameters = request.GET.copy()
		resp = clouai.handleRequest(parameters)
		response = HttpResponse(resp, content_type="text/xml")
		return response
	except Repository.DoesNotExist:
		response = HttpResponse('Error, repository named as "' + str(repository_name) + '" not found.')
		return response

#http://memory.loc.gov/cgi-bin/oai2_0?verb=ListRecords&metadataPrefix=oai_dc&set=mussm