from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# here UserCreationForm is django build in form where user sign up a new account
# UserChangeForm is django build in form where admin modify existing users
# here both new forms setting the model to custom user and using default fields by using Meta.fields


class CustomUserCreationForm(UserCreationForm): # the form where there are many build in attributes,inherit from build in UserCreationForm

    class Meta(UserCreationForm.Meta): # meta.fields means default fields(build in)
        model = CustomUser # model is our custom user, inherit from UserCreationForm
        # build in UserCreationForm attribute is username,password for sign up,here we add age in our custom user model and it shows only admin site
        # fields = UserCreationForm.Meta.fields  # we're using meta.fields which is just display username,password
        fields = ('username', 'email') # explicitly said what attributes on sign up,we don't need include password field beacuse it's required


class CustomUserChangeForm(UserChangeForm): # this one is use for change ability of admin

    class Meta:
        model = CustomUser
        # meta fields display build in attributes which one admin can edit(username,pass,email,first name,last name....)
        # fields = UserChangeForm.Meta.fields  # here the fields are which admin can edit(usernam,email,pass,first_name,
        # last_name, is_superuser... many others) which one is come from custom user(inherit from abstract)
        fields = ('username', 'email') # explicitly said which attribute admin can change (not so useful)
