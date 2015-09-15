from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
# Create your models here.


class ActiveProfileManager(models.Manager):
    """A model manger limited only to active profiles"""
    def get_queryset(self):
        """Filter the default queryset for active users"""
        query = super(ActiveProfileManager, self).get_queryset()
        return query.filter(user__is_active=True)


@python_2_unicode_compatible
class ParkingProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        null=False
    )

    car_model = models.CharField(max_length=128,
                                 help_text="What is the model of your car?")

    phone_number = models.IntegerField()
    objects = models.Manager()
    active = ActiveProfileManager()


    def __str__(self):
        return self.user.get_full_name() or self.user.username


    def is_active(self):
        return self.user.is_active
