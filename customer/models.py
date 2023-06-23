from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


account_type = (
    ('customer','customer'),
    ('barista', 'barista'),
)

class profile(AbstractUser):
    account_type =  models.CharField(max_length=12, choices=account_type, default='customer')
    def __str__(self):
        return self.email