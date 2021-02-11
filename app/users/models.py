from django.db import models
from django.db.models import base
from django.db.models.fields import CharField, DateField, EmailField, FloatField, IntegerField
from django.db.models.fields.related import ManyToManyField


class PaymentPlan(models.Model):
    name = CharField(max_length=100, null=False, blank=False)
    description = CharField(max_length=255, null=False, blank=False)
    price = FloatField(null=False)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    name = CharField(max_length=100, null=False, blank=False)
    email = EmailField(max_length=150, null=False, blank=False)
    password = CharField(max_length=100, null=False, blank=False)
    date_birth = DateField()
    plan = ManyToManyField(PaymentPlan)

    def __str__(self) -> str:
        return self.name
