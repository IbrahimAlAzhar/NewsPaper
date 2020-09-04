from django.contrib import admin
from . import models
# applying these for that reason see and modify all our related articles and comments in one place

'''
# for stack inline where all comments shows below in the article
class CommentInline(admin.StackedInline):
    model = models.Comment  # comments model stacked in line
'''


class CommentInline(admin.TabularInline): # for all comments inside a article shows in admin page in a tabular shape(less space required)
    model = models.Comment  # all fields for each model(comment) are displayed on the same line for using Tabularline


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,  # inlining the commentInline model with the name of ArticleAdmin
    ]

# store ArticleAdmin(inline 'model comment') within the article admin
# here register the ArticleAdmin inside the Article model for inline commenting
admin.site.register(models.Article, ArticleAdmin) # register the ArticleAdmin (include comment model) inside the Article admin,then display the creating comment option inside the Article
admin.site.register(models.Comment) # as usual comment admin in here
