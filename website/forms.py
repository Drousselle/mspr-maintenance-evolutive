from django import forms


class UploadFileForm(forms.Form):
    docfile = forms.FileField(label="Selectionnez un fichier .csv")
