from __future__ import unicode_literals

from django.db import models

# Create your models here.
def betta():
    pass

class Betta1(object):
    pass

class Betta2(Betta1):
    pass

class Gamma(object):
    pass

class Betta3(Betta2, Gamma):
    pass