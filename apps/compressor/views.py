from django.views.generic import TemplateView, CreateView
from django.shortcuts import get_object_or_404, redirect, reverse

from .models import HyperlinkModel


class HyperlinkCreateView(CreateView):
    """Display a simple for for creating new Hyperlink records"""

    template_name = 'compressor/create.html'
    model = HyperlinkModel
    fields = ['original']

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(HyperlinkCreateView, self).get_form(form_class)
        form.fields['original'].label = 'Long URL'
        form.fields['original'].widget.attrs['placeholder'] = 'Paste your link here:'
        return form

    def form_valid(self, form):
        hyperlink = form.save()
        return redirect('compressor:info', internal=hyperlink.internal)


class HyperlinkInfoView(TemplateView):
    """Display info about the particular Hyperlink"""

    template_name = 'compressor/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        host = self.request.get_host()  # www.ditto.pink
        internal_id = kwargs.get('internal')  # A1A1A
        context['redirect'] = build_short_redirect_url(host, internal_id)
        return context


def build_short_redirect_url(host, internal_id):
    """Build the redirect URL to display in the template. Strip the leading `www.`"""

    endpoint = reverse('compressor:redirect', kwargs={'internal': internal_id})  # /r/A1A1A
    full_redirect = ''.join([host, endpoint])  # www.ditto.pink/r/A1A1A
    return full_redirect.lstrip('www.')


def redirect_view(request, **kwargs):
    """Redirect any internal Hyperlink URL to the original and record a view"""

    internal = kwargs.get('internal')
    record = get_object_or_404(HyperlinkModel, internal=internal)
    return redirect(record.original, permanent=True)
