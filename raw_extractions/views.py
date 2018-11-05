from django.shortcuts import render
from .forms import RawDataForm

# Create your views here.


def raw_data_form(request):
    """view associated to RawDataForm"""
    form = RawDataForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        controller = form.cleaned_data['controller']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
    return render(request, 'raw_extractions/raw_data_form.html', locals())