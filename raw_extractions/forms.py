from django import forms
from datetime import datetime


class RawDataForm(forms.Form):
    choice_list = ((60320, "CBC_BSM_A01"), (60321, "CBC_BSM_A02"), (60323, "CBC_BSM_A03"), (60604, "CBC_BSM_A04"), (
        60626, "CBC_BSM_A05"), (59930, "CBC_BSM_A06"), (60278, "CBC_BSM_A08"), (60659, "CBC_BSM_A09"),
                   (60325, "CBC_BSM_A10"))
    controller = forms.ChoiceField(choices=choice_list)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
