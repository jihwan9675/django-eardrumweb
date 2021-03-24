from django import forms
from .models import Predict

class PredictForm(forms.Form):
    userid = forms.CharField(error_messages={
        'required': '아이디를 입력해주세요.'
    }, max_length=64,label="아이디")
    password = forms.CharField(error_messages={
        'required':'비밀번호를 입력해주세요.'
    },widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()

from .models import UploadFileModel

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False