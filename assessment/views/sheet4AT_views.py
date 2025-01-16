import logging

from django.urls import reverse_lazy
from django.views.generic import FormView

from assessment.forms.sheet4AT_forms import ATForm


class AT4View(FormView):
    template_name = "assessment/AT4.html"
    form_class = ATForm
    success_url = reverse_lazy("assessment:success")

    def form_valid(self, form):
        # Calls the custom send method
        logging.info(12)
        form.send()
        return super().form_valid(form)
