from django import forms
from .models import Predict
from .models import UploadFileModel

class PredictForm(forms.ModelForm):
    file = forms.FileField() # image field

    def __init__(self, request, *args, **kwargs):
        super(PredictForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['file'].required = False

    class Meta:
        model = UploadFileModel
        fields = ('file',)

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False