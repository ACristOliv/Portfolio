from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self):
        context = super(IndexPage, self).get_context_data()
        # context.update({"name": "André"})

        return context

index_page = IndexPage.as_view()
