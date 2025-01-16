from django.urls import reverse_lazy
from django.views.generic import FormView

from assessment.forms.sheetCAM1_forms import CAMForm


class CAMView(FormView):
    template_name = "assessment/CAM.html"
    form_class = CAMForm
    success_url = reverse_lazy("assessment:success")

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
