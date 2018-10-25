from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import redirect

from .models import HyperlinkModel


class HyperlinkCreateView(CreateView):
    """Display a simple for for creating new Hyperlink records"""

    template_name = 'compressor/create.html'
    model = HyperlinkModel
    fields = ['original']

    def form_valid(self, form):
        hyperlink = form.save()
        return redirect('compressor:info', internal=hyperlink.internal)


class HyperlinkInfoView(TemplateView):
    """Display info about the particular Hyperlink"""

    template_name = 'compressor/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['internal'] = kwargs.get('internal')
        return context


def redirect_view(request, **kwargs):
    """Redirect any internal Hyperlink URL to the original and record a view"""

    internal = kwargs.get('internal')
    original = HyperlinkModel.objects.filter(internal=internal).first().original
    # TODO: increment the view count by one
    return redirect(original)
