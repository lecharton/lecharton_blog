from django.shortcuts import render


from .forms import ApplicationForm
from .models import Links, AdditionalLinks


def contact(request):
    if request.method != 'POST':
        form = ApplicationForm()
        return render(
            request, 'contact.html',
            {
                'form': form,
                'main_title': 'Контакты'
            }
        )

    form = ApplicationForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            "contact.html",
            {'form': form, 'main_title': 'Контакты'})

    application = form.save(commit=False)
    application.save()

    return render(
        request,
        "contact.html",
        {
            'message': 'Спасибо! Я отвечу вам в течении пары дней.',
            'main_title': 'Контакты'
        }
    )


def links(request):
    links = Links.objects.all()
    additional_links = AdditionalLinks.objects.all()

    return render(
        request,
        'taplink.html',
        { 'links': links, 'additional_links': additional_links }
    )