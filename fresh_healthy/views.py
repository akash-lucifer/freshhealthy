from django.shortcuts import render
from django.http import HttpResponse;

def static_page_url(request,url):
	return HttpResponse('Hello this static url');