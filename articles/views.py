from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, Comment
from .forms import CommentForm
# LoginRequiredMixin is Django build in mixin which is if a user want to CRUD operation then the user have to login


class ArticleCreateView(LoginRequiredMixin,CreateView): # to restrict view access to only logged in usere,django has this mixin, in function based view django has @login_required
    model = models.Article
    template_name = 'article_new.html' # all generic view returns the template again and again for that reason django has TemplateResponseMixin
    fields = ['title', 'body', ] # we don't need to create author field,because user is automatically author of his post
    login_url = 'login'  # if unauthorized user try to create a post then it redirect to login page(django build in,which name is login),normally it redirect to accounts/login but we have to override using login_url

    def form_valid(self, form): # set the author of a post is current user
        # this method customize the class based create view and set the author of a post is current user.for find out this type of code google it or stackoverflow
        form.instance.author = self.request.user # the author field of form is current user
        return super().form_valid(form)  # return the author from valid form


class ArticleListView(LoginRequiredMixin, ListView): # loginrequiredmixin means if the user see the posts then the user have to login
    model = models.Article
    template_name = 'article_list.html' # return object_list (build in) and detailview return objects (build in)
    login_url = 'login'  # if unauthorized user wants to access the listview then the url redirect to login url


class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login' # override build in login url which is 'accounts/login' instead of.we using users/login which url name is 'login'


class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Article
    fields = ['title','body', ] # we use title and body field for update,updateview has no author,because once we create a author than we can't upate the author
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list') # here use reverse_lazy because after the delete then redirect this url
    login_url = 'login'

'''
def post_detail(request,my_id):
    article = get_object_or_404(Article, id=my_id)
    # List of active comments for this post
    comments = article.comments.filter(active=True) # here comments is the all instances of comment model which one define on comment model
    new_comment = None

    if request.method == 'POST':
        # A comment was posted,then take the comment form
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # new_comment is the instance of commentForm which using Comment model,after posting a new comment then take the comment on post attribute
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm() # in get method,show a empty form
    return render(request,
                  'article_detail_2.html',
                  {'article': article,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})



'''
