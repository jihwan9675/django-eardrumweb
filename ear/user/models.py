from django.db import models


class User(models.Model):
    userid = models.CharField(max_length=32,
                              verbose_name='아이디')
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=128,
                                verbose_name='비밀번호')
    level = models.CharField(max_length=8, verbose_name='등급', choices=(
        ('admin', 'admin'),
        ('doctor', 'doctor'),
        ('user', 'user')
    ))
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = '회원'
        verbose_name_plural = '회원'
