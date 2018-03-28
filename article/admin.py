from django.contrib import admin
from  article.models import Article, Comments
# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2
class ArticleAdmin(admin.ModelAdmin):
    fiels = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInline]
    filtr = ['article_date']

admin.site.register(Article, ArticleAdmin)
