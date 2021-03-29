import os, datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.generic.edit import FormView
from django.core import serializers
from .forms import PredictForm
from PIL import Image
from .apps import predictmodel, PredictConfig
import tensorflow as tf
from .forms import UploadFileForm
from .models import Predict, UploadFileModel
from user.models import User
from decimal import Decimal

class PredictView(FormView):
    template_name = 'predict.html'
    form_class = PredictForm

    def get(self, request, *args, **kwargs): # GET Method (preidct/)
        form = self.form_class(request, initial=self.initial)
        return render(request, self.template_name, {'form':form,'username':request.session.get('user')})

    def post(self, request, *args, **kwargs): # POST Method (preidct/)
        # rename 'request.FILES'
        # Ex) xxxx.jpg -> UserId-2021-03-01.jpg
        request.FILES['file'].name = self.create_file_name(request.session.get('user'), request.FILES['file'].name)
        form = UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            # Predict ... result = [Disease Name, Count of Detected Instance, Accuracy]
            result = PredictConfig.just.predict(image_path=request.FILES['file'].name)
            # Save Model into Predict Table.
            predict = Predict(
                user = User.objects.get(userid=request.session.get('user')),
                result = result[0],
                image = request.FILES['file'].name,
                count = result[1], 
                accuracy = float(result[2])
            )
            predict.save()
        data = serializers.serialize("json", [predict]) # Model -> JSON

        return JsonResponse(data,safe=False)

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
        
    def create_file_name(self, id, filename):
        extension = os.path.splitext(filename)[-1].lower() # split Extenstion name 
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d-%H%M%S')

        # Ex) UserId-2021-03-22.jpeg
        return id + '-' + nowDate + extension

