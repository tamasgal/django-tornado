from django.http import HttpResponse


def hello(request):
    """A test view to assure django is responsing."""
    return HttpResponse("Hello from django")
