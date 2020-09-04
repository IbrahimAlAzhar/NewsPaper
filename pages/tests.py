from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomePageTests(SimpleTestCase): # there are 4 template pages,we should test only home page and sigun up(login,logout don't need to test as they are django build in)
    def test_home_page_status_code(self): # the page exist and returns a Http 200 request
        response = self.client.get('/') # get home page url
        self.assertEqual(response.status_code, 200) # send http request or not

    def test_view_url_by_name(self): # the page uses the correct url name in the view,test home page by name
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self): # the proper template is being used or not
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html') # check using home template or not


class SignupPageTests(TestCase): # signup process include with database so you have to use Test case
    username = 'newuser'
    email = 'newuser@email.com' # create dummy username,email for testing

    def test_signup_page_status_code(self): # check the page exits and returns a http 200 status code
        response = self.client.get('/users/signup/') # get the url
        self.assertEqual(response.status_code,200) # checking http request

    def test_view_url_by_name(self): # check the page uses the correct url name in the view
        response = self.client.get(reverse('signup')) # testing url by name
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self): # check the proper template is being used
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self): # verifying when a username and email are posted,they match what is stored on the customuser model
        new_user = get_user_model().objects.create_user(self.username, self.email) # take the username and password which one we created first
        self.assertEqual(get_user_model().objects.all().count(),1) # here we create one dummy user and check this
        self.assertEqual(get_user_model().objects.all()[0].username, self.username) # check the username
        self.assertEqual(get_user_model().objects.all()[0].email, self.email) # check the email of first user which one we created