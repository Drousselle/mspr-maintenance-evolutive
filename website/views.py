from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Document
from .forms import UploadFileForm


def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            newdoc.action_fill_database()

            return redirect('file_upload')

    form = UploadFileForm()

    return render(request, 'index.html', {'documents': Document.objects.all(),
                                          'form': form})