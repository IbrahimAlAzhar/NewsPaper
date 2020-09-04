from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm


class SignUp(generic.CreateView): # you need create a class for signup where use form,but don't need to create class for login,logout
    form_class = CustomUserCreationForm # the form is inherit from usercreationform(buil in) and add one attribute(age) using meta class
    success_url = reverse_lazy('login') # in class based view we use reverse lazy,
    template_name = 'signup.html'

'''
def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the user object in database
            new_user.save()
            # create a user profile(user is the parameter of profile)
            # CustomUser.objects.create(user=new_user) # here create a user profile object, if i don't register then edit path will not work
            return render(request, 'home.html',
                                    {'new_user': new_user})
    else:
        user_form = CustomUserCreationForm() # when using get method
    return render(request,'register.html',
                          {'user_form': user_form})

'''

