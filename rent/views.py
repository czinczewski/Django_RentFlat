from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Main Page</h2>"
                        "<h3>Holla</h3>")
