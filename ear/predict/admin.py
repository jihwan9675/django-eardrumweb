from django.contrib import admin
from .models import UploadFileModel, Predict


class PredictAdmin(admin.ModelAdmin):
    list_display = ('user', 'result', 'predict_date',
                    'image', 'count', 'accuracy')


class UploadAdmin(admin.ModelAdmin):
    list_display = ('file',)


admin.site.register(UploadFileModel, UploadAdmin)
admin.site.register(Predict, PredictAdmin)
