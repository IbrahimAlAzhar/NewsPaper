from django.db import models
from django.contrib.auth.models import AbstractUser
# in django doc extends from AbstractbaseUser


class CustomUser(AbstractUser):
    # Custom user is basically a copy of the default user model,only update is age field
    # here inherit from abstract class so there are so many attribute in database,default abstract user has many attributes for sign up
    age = models.PositiveIntegerField(default=0) # this age attribute shows only admin site not form site
