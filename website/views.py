from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Document
from .forms import UploadFileForm


def file_upload(request):
    message = 'Select a file'
    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('file_upload')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = UploadFileForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'index.html', context)