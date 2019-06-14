from django.core import serializers
from django.db.models import Q
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.shortcuts import render
from account.models import *


# Create your views here.
def index_view(request):
    auth = False
    if request.user.is_authenticated:
        auth = True

    categories = Category.objects.all()
    sliders = MainSlider.objects.all()
    mpage = MainPage.objects.get(id=1)
    statics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'auth': auth,
        'categories': categories,
        'sliders': sliders,
        'mpage': mpage,
        'statics': statics,
    }
    return render(request, 'blog/index.html', context)


def list_artcles(request, category_slug):
    categories = Category.objects.all()
    auth = False
    if request.user.is_authenticated:
        auth = True

    category = Category.objects.get(slug=category_slug)
    articles = Article.objects.filter(category=category_slug)
    context = {
        'auth': auth,
        'categories': categories,
        'category': category,
        'articles': articles,
    }
    return render(request, 'blog/templates_article/article_list.html', context)


def detail_article(request, category_slug, article_slug):
    categories = Category.objects.all()
    auth = False
    if request.user.is_authenticated:
        auth = True

    try:
        article = Article.objects.get(slug=article_slug)
        category = Category.objects.get(slug=category_slug)
        context = {
            'auth': auth,
            'categories': categories,
            'category': category,
            'article': article,
        }
        return render(request, 'blog/templates_article/article_detail.html', context)
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def search_article(request):
    if request.is_ajax():
        if request.GET.get('search') != '':
            articles = Article.objects.filter(
                Q(name__iregex=request.GET.get('search')) | Q(prev_text__iregex=request.GET.get('search'))).order_by(
                'category')[:10]
            serialize = serializers.serialize('json', articles)
            return HttpResponse(serialize, content_type="application/json")
    else:
        if request.GET.get('search') != '':
            articles = Article.objects.filter(
                Q(name__iregex=request.GET.get('search')) | Q(prev_text__iregex=request.GET.get('search')))
            categories = Category.objects.all()
            auth = False
            if request.user.is_authenticated:
                auth = True
            context = {
                'auth': auth,
                'categories': categories,
                'articles': articles,
            }
            return render(request, 'blog/templates_article/search_page.html', context)

        else:
            return render(request, 'blog/templates_article/search_page.html',
                          {'error': 'По вашему запросу ничего не найдено'})


def reviews_list(request):
    list = Reviews.objects.all()
    categories = Category.objects.all()
    auth = False
    if request.user.is_authenticated:
        auth = True
    context = {
        'auth': auth,
        'categories': categories,
        'reviews': list,
    }
    return render(request, 'blog/templates_article/reviews_list.html', context)


def review_new(request):
    if request.method == 'POST':
        try:
            if request.POST.get('email'):
                review = Reviews()
                if 'anonym' in request.POST:
                    if request.POST.get('anonym') == 'on':
                        review.name = 'Анонимно'
                        review.anonym = True
                else:
                    review.name = request.POST.get('name')
                    review.anonym = False
                review.text = request.POST.get('text')
                review.email = request.POST.get('email')
                review.save()

                ob = Reviews.objects.all()
                serialize = serializers.serialize('json', ob)
                return HttpResponse(serialize, content_type="application/json")
        except:
            return JsonResponse({'error': 'error'})


def contacts_view(request):
    contacts = Contacts.objects.get(id=1)
    categories = Category.objects.all()
    auth = False
    if request.user.is_authenticated:
        auth = True
    context = {
        'auth': auth,
        'categories': categories,
        'contacts': contacts,
    }
    return render(request, 'blog/templates_article/contacts.html', context)
