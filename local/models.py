from django.db import models

# Create your models here.
'''
grade: 'Green',
    name: '전수민',
    id: 'jeon(오후)',
    mail: 'jeon@gmail.com',
    address: '서울시 노원구 동일로 174길 27',
    number: '010-0000-0000',
    latest: '2022.11.07',
    date: '2022.10.24',
    '''
class Test_model(models.Model):
    grade = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50 , null=False)
    userid = models.CharField(max_length=50, null=True)
    mail = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=50, null=True)
    latest = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)

