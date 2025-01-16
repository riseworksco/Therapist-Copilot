from django.urls import reverse_lazy
from django.views.generic import FormView

from assessment.forms.sheetPHQ_forms import PHQForm


class PHQView(FormView):
    template_name = "assessment/PHQ-9.html"
    form_class = PHQForm
    success_url = reverse_lazy("assessment:success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" in context:
            # Manually add each question field to the context
            context["questions"] = [
                context["form"][f"question{i}"] for i in range(1, 11)
            ]
        return context

    def form_valid(self, form):
        form.send()  # Send your email
        return super().form_valid(form)  # Redirect to success_url
