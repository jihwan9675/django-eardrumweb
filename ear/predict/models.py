
from django.db import models
from user.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Predict(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='사용자')
    result = models.CharField(max_length=32, verbose_name='진단결과')
    predict_date = models.DateTimeField(auto_now_add=True, verbose_name='진단날짜')
    image = models.ImageField(null=True)
    count = models.IntegerField()
    accuracy = models.DecimalField(max_digits=100, decimal_places=3)

    def __str__(self):
        return str(self.user) + ' ' + str(self.result)

    class Meta:
        db_table = 'predict'
        verbose_name = '진단'
        verbose_name_plural = '진단'


class UploadFileModel(models.Model):
    file = models.FileField(null=True)

    def __str__(self):
        return str(self.file)
