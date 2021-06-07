from django.core.validators import FileExtensionValidator
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d'])
