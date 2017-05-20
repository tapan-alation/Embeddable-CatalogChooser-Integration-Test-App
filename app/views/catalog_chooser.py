from django.views.generic import TemplateView


class CatalogChooserView(TemplateView):
    template_name = 'catalog_chooser.html'