from django import forms
from .models import Predict
from .models import UploadFileModel

class PredictForm(forms.ModelForm):
    # Eardrum Image Field
    # File Name Rule : ('d_' or 'c_' or ' ')id_date_.extention
    # ex) /media/c_wg0705_2021-04-01-000000.jpg
    file = forms.FileField() 

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