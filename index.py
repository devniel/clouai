# -*- coding: ISO-8859-1 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Index page

def index(request):

	#subdomain = request.META['HTTP_HOST'].split('.')[0]

	#if subdomain is not None and subdomain != 'www' and subdomain != 'localhost' and subdomain != 'clouai':
	#	return redirect('/oai?verb=ListRecords&metadataPrefix=oai_dc')
	
	if request.user.is_authenticated():
		return render(request,"index.html")
	else:
		return render(request,"landing.html")