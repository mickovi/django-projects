from .models import Link
"""
def context_dict(request):
    links = Link.objects.all()
    context = {link.key: link.url for link in links}
    return context
"""

def context_dict(request):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    return context