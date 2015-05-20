from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world.\nYou're at the RSSInterpreter Index Page.")

