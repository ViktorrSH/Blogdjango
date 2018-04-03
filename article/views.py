from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def basic_one(request):
    view = "basic_one"
    html = "<html><body><h1>This is %s view</h1></body></html>" % view
    return HttpResponse(html)

def template_one(request):
    view = "template_one"
    html = get_template("firstview.html").render({
        'name': view,
    })
    return HttpResponse(html)

'''prostoy vivod informacii v views'''

def template_two_simple(request):
    name = "template_two_simple"
    return render_to_response('firstview.html', {'name': name})

def ind(request):
    return render_to_response('ars.html', {'articles': Article.objects.all()})

def art(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id = article_id), 'comments': Comments.objects.filter(comments_article_id= article_id)})


def like(request, article_id):
    try:
        a = Article.objects.get(id=article_id, article_likes=700)
        a.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('')



