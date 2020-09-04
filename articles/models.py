from django.db import models
from django.conf import settings
# import settings because here define a model which override basic user model and add some attributes
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,  # author is fk,the pk is user(custom user(users/model),override from abstract user where stores the user)
            on_delete= models.CASCADE, # author is user,which one we create
    )

    def __str__(self):
        return self.title # viewing the model in our admin interface

    def get_absolute_url(self):
        # if we later change the url pattern for the detail page the redirect will still work
        return reverse('article_detail', args=[str(self.id)]) # after creating,updating a post form then redirect to post detail page where requires id,


class Comment(models.Model):
    article = models.ForeignKey(    # many to one relationship (many comments hold in one article,the name of fk is simply the model it links to)
            Article,  # here using follow a relationship backward for each article look up related comment models
            on_delete=models.CASCADE, # we can use 'article_set' to access all instances of the model instead of here we
            related_name='comments')   # define 'comments' explicitly to add a related name attribute (for take all instances of comment means all comments of a post)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, # here define the custom user model(which override base user model) which is author
        on_delete=models.CASCADE,
    )
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.comment  # viewing the comment in admin interface using dunder function

    def _get_absolute_url(self):
        return reverse('article_list') # after create comment then return to article_list url(page)(basically this method has other functions too)

'''
when you take the migrations then you have to define the app name like "python manage.py makemigrations articles" 
if we did not specify an app,the both apps changes would be incorporated in the same migrations file which makes it harder, to debug errors
keep each migration as small and contained as possible.
'''