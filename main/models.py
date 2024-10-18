from django.db import models

# Create your models here.
class Consumers(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class Agreement(models.Model):
    name = models.CharField( null=True, blank=True)
    number = models.CharField()
    date = models.DateField()
    transmitting_side = models.CharField()

    def __str__(self):
        return self.name

class Plase (models.Model):
    name = models.CharField()
    city = models.CharField()
    id_agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Meters(models.Model):
    number_meter = models.IntegerField()
    name = models.CharField()
    id_plase = models.ForeignKey('Plase', on_delete=models.CASCADE)
    id_consumer = models.ForeignKey(Consumers, on_delete=models.CASCADE)
    auto_collection = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class MeterCoef(models.Model):
    number_meter = models.ForeignKey(Meters, on_delete=models.CASCADE)

class MeterValue(models.Model):
    meter = models.ForeignKey('Meters', on_delete=models.CASCADE)
    value_first = models.FloatField(null=True)
    value_last = models.FloatField(null=True)
    value_fact = models.FloatField(null=True)
    #value_invoice = models.FloatField(null=True)
    date_add = models.DateField(null=True)
    palse = models.ForeignKey('Plase', on_delete=models.CASCADE)
    flag = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id_meter)

class Oil(models.Model):
    date = models.DateField()
    value = models.FloatField()
    flag = models.BooleanField(default=True)