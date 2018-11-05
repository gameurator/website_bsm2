from django import forms
from django.utils import timezone


class RawDataForm(forms.Form):
    choice_list = (("CBC_BSM_A01", 60319), ("CBC_BSM_A02", 60321), ("CBC_BSM_A03", 60323), ("CBC_BSM_A04", 60604), (
        "CBC_BSM_A05", 60626), ("CBC_BSM_A06", 59930), ("CBC_BSM_A08", 60278), ("CBC_BSM_A09", 60659), (
                  "CBC_BSM_A10", 60325))
    controller = forms.ChoiceField(choices=choice_list)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
