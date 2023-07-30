from django.db import models

# Create your models here.
#회원가입

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class User(models.Model):
    objects = None
    username = models.CharField(max_length=80)
    phonenum = IntegerRangeField(max_value=13)
    password1 = models.CharField(max_length=6)
    password2 = models.CharField(max_length=6)
    birthY = IntegerRangeField(max_value=2100)
    birthM = IntegerRangeField(max_value=12)
    birthD = IntegerRangeField(max_value=32)