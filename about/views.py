from django.shortcuts import render


from .models import Links, AdditionalLinks


def links(request):
    links = Links.objects.all()
    additional_links = AdditionalLinks.objects.all()

    return render(
        request,
        'taplink.html',
        { 'links': links, 'additional_links': additional_links }
    )