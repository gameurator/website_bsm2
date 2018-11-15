from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import RawDataForm
import requests
import json
from datetime import datetime


# Create your views here.


def raw_data_form(request):
    """view associated with RawDataForm"""
    form = RawDataForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        controller = form.cleaned_data['controller']
        start_date: datetime = form.cleaned_data['start_date']
        end_date: datetime = form.cleaned_data['end_date']
        return redirect(
            "raw_extractions/result/" + controller + "-" + "TotalKWHPositive" + "-" + start_date.strftime(
                '%d.%m.%Y') + "-" + end_date.strftime(
                '%d.%m.%Y'))  # rajouter strftime puis obtenir l'URL et vérifier fction suivante
    return render(request, 'raw_extractions/raw_data_form.html', locals())


def raw_data_present(request: HttpRequest, deviceId: int, name: str, start_date: str,
                     end_date: str) -> HttpResponse:
    """Presenting API result"""
    SLV_URL = "http://citybox2.axione.fr/reports/"
    start_date.replace(".", "/")
    end_date.replace(".", "/")
    api_method = 'getDevicesLogValues'  # function which gets called on SLV server
    api_part = '/api/logging/'  # where the function is on SLV server
    response = requests.post(SLV_URL + api_part + api_method,
                             data={"ser": "json", "from": start_date, "to": end_date, "deviceId": deviceId,
                                   "name": name},
                             auth=("d.mocellin", "Nevers1.1"))
    raw_data_json = response.json()
    raw_data_headers = response.headers
    raw_data_xml = response.text
    raw_data_status_code = response.status_code
    print(response.text)
    return render(request, 'raw_extractions/data_presentation.html',
                  {'raw_data_json': raw_data_json, 'raw_data_xml': raw_data_xml, 'raw_data_headers': raw_data_headers,
                   'raw_data_status_code': raw_data_status_code})
