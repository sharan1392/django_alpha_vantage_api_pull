from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class price(models.Model):

    meta_data = JSONField()
    data_time_series = JSONField()

    class Meta: db_table = "price"
