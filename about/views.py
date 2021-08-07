from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'about.html'


class AboutContactView(TemplateView):
    template_name = 'contact.html'