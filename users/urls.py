from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(),name='signup'),
    # users/login, users/logout, users/password_change, users/password_change/done, users/password_reset, users/password_reset/done these url don't need to create,django automatically build this url

]