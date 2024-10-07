from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from django.contrib.postgres.fields import DateTimeRangeField, ArrayField, HStoreField, CICharField

from django.db import models
from localflavor.us.models import USStateField

class Event(models.Model):
    name = models.CharField(max_length =255)
    duration = DateTimeRangeField()

    def __str__(self):
        return self.name
class Address(models.Model):
    state = USStateField()
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
    name = models.CharField(max_length=30)
    notes = GenericRelation('Note')

    def __str__(self):
        return self.name


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare, through='Kit',
                                    through_fields=('machine', 'spare'))
    notes = GenericRelation('Note')

    def __str__(self):
        return self.name


class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.machine} ({self.spare}): {self.count} шт.'


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field='content_type',
        fk_field='object_id',
    )
