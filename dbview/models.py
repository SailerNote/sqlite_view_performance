from django.db import models


# Create your models here.

class CashFlow(models.Model):
    company_from = models.CharField(max_length=63, default='from')
    company_to = models.CharField(max_length=63, default='to')
    date = models.DateField(null=True)
    p1 = models.FloatField(default=0)

    class Meta:
        ordering = ['date']


class TempWeek(models.Model):
    company_from = models.CharField(max_length=63, default='from')
    company_to = models.CharField(max_length=63, default='to')
    sum = models.FloatField()

    class Meta:
        managed = False
        db_table = "temp_week"


class TempDate(models.Model):
    company_from = models.CharField(max_length=63, default='from')
    company_to = models.CharField(max_length=63, default='to')
    sum = models.FloatField()

    class Meta:
        managed = False
        db_table = "temp_date"
