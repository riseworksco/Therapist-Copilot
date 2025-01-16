"""Music_Therapy_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path

from assessment.views import (
    AAQ2View,
    AT4View,
    CAM1View,
    GAD7View,
    NeurologicScreeningEvaluationView,
    PHQ9View,
    PrePostView,
    PsychoemotionalScreeningEvaluationView,
    RASView,
    StompSuccessView,
    StompView,
)

from . import views
from .views.sheetAAQII_views import AAQIIView
from .views.sheetCAM1_views import CAMView
from .views.sheetGAD_views import GADView
from .views.sheetPHQ_views import PHQView

# import patient_management
app_name = "assessment"

urlpatterns = [
    # path('stomp/', views.stomp, name='stomp'),
    re_path(r"^$", views.index),
    re_path(r"^download/$", views.render_pdf),
    path("", views.index, name="index"),
    path("stomp/", StompView.as_view(), name="stomp"),
    path("success/", StompSuccessView.as_view(), name="success"),
    path(
        "neurologic_screening_evaluation/",
        NeurologicScreeningEvaluationView.as_view(),
        name="Neurologic_Screening_Evaluation",
    ),
    path("pre_post_tests/", PrePostView.as_view(), name="pre_post_tests"),
    path(
        "Psychoemotional_Screening_Evaluation/",
        PsychoemotionalScreeningEvaluationView.as_view(),
        name="Psychoemotional_Screening_Evaluation",
    ),
    path("pdf/", views.some_view, name="pdf"),
    path("AT4/", AT4View.as_view(), name="AT4"),
    path("AAQII/", AAQ2View.as_view(), name="AAQII"),
    path("CAM/", CAM1View.as_view(), name="CAM"),
    path("GAD7/", GAD7View.as_view(), name="GAD7"),
    path("PHQ9/", PHQ9View.as_view(), name="PHQ9"),
    path("RAS/", RASView.as_view(), name="RAS"),
    path("sheet4AT/", AT4View.as_view(), name="sheet4AT"),
    path("AAQII/", AAQIIView.as_view(), name="AAQII"),
    path("sheetCAM1/", CAMView.as_view(), name="CAM1"),
    path("GAD/", GADView.as_view(), name="GAD"),
    path("PHQ/", PHQView.as_view(), name="PHQ"),
    path("RAS/", RASView.as_view(), name="RAS")
]
