import os, datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import PredictForm
from PIL import Image
from .apps import PredictConfig

class PredictView(FormView):
    template_name = 'predict.html'
    form_class = PredictForm
    
    def form_valid(self, form):
        self.request.session['user'] = form.data.get('userid')
        return super().form_valid(form)

from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        request.FILES['file'].name = makefilename(request.session.get('user'), request.FILES['file'].name)
        if form.is_valid():
            form.save()
            s = PredictConfig.detect_roi(PredictConfig, image_path=request.FILES['file'].name)
            print(s)
            #PredictConfig.predict(PredictConfig, request.FILES['file'].name)
            #image = Image.open('media/' +request.FILES['file'].name)
            #image.show()
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def makefilename(id, filename):
    extension = os.path.splitext(filename)[-1].lower()
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d-%H%M%S')
    return id + '-' + nowDate + extension

