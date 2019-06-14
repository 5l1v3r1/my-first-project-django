from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *
from django.db.models import Q
from django.http import JsonResponse


def index_view(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        articles = Article.objects.order_by("name")[0:15]
        contacts = Contacts.objects.get(id=1)
        politics = PoliticsAndСonfidentiality.objects.all()
        context = {
            'categories': categories,
            'contacts': contacts,
            'politics': politics,
            'articles': articles,
        }
        return render(request, 'account/index.html', context)
    else:
        return render(request, 'blog/index.html', {})


def category_view_article(request, category_slug):
    articles = Article.objects.filter(category=str(category_slug))
    categories = Category.objects.all()
    contacts = Contacts.objects.get(id=1)
    politics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'categories': categories,
        'contacts': contacts,
        'politics': politics,
        'articles': articles,
    }
    return render(request, 'account/category_article_list.html', context)


def category_create(request):
    categories = Category.objects.all()
    contacts = Contacts.objects.get(id=1)
    politics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'categories': categories,
        'contacts': contacts,
        'politics': politics,
    }
    return render(request, 'account/create_category.html', context)


def category_save(request):
    if request.method == 'POST':
        category = Category()
        category.name = request.POST.get('name')
        category.slug = request.POST.get('slug')
        category.save()
        return redirect('/account/')


def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'category': category,
    }
    return render(request, 'account/edit_category.html', context)


def update_category(request, category_id):
    if request.method == 'POST':
        category = Category.objects.get(id=category_id)
        category.name = request.POST.get('name')
        category.slug = request.POST.get('slug')
        category.save()
    return redirect('/account/')


def category_delete(request, category_id):
    Category.objects.get(id=category_id).delete()
    return redirect('/account/')


def save_article(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            if 'prev_img' in request.FILES:
                form.prev_img = request.FILES['prev_img']
            form.name = request.POST.get('name')
            form.slug = request.POST.get('slug')
            form.prev_text = request.POST.get('prev_text')
            if 'detail_img' in request.FILES:
                form.detail_img = request.FILES['detail_img']
            form.detail_text = request.POST.get('detail_text')
            form.tags = request.POST.get('tags')
            form.category = request.POST.get('category')
            form.save()
        return redirect('/account/')


def create_article(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'account/create_article.html', context)


def delete_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.delete()
        return_path = request.META.get('HTTP_REFERER', '/')
        return redirect(return_path)
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    categories = Category.objects.all()
    contacts = Contacts.objects.get(id=1)
    politics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'categories': categories,
        'contacts': contacts,
        'politics': politics,
        'article': article,
    }
    return render(request, 'account/edit_article.html', context)


def update_article(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(id=article_id)
        article.name = request.POST.get('name')
        article.slug = request.POST.get('slug')
        article.prev_text = request.POST.get('prev_text')
        article.detail_text = request.POST.get('detail_text')
        article.tags = request.POST.get('tags')
        article.category = request.POST.get('category')
        article.save()
    return redirect('/account/')


def search_in_articles(request):
    articles = Article.objects.filter(
        Q(name__iregex=request.GET.get('search')) | Q(detail_text__iregex=request.GET.get('search')) | Q(
            prev_text__iregex=request.GET.get('search')))
    categories = Category.objects.all()
    contacts = Contacts.objects.get(id=1)
    politics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'categories': categories,
        'contacts': contacts,
        'politics': politics,
        'articles': articles,
    }
    return render(request, 'account/index.html', context)


def contacts_edit(request):
    contact = Contacts.objects.get(id=1)
    categories = Category.objects.all()
    contacts = Contacts.objects.get(id=1)
    politics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'categories': categories,
        'contacts': contacts,
        'politics': politics,
        'contact': contact
    }
    return render(request, 'account/edit_contacts.html', context)


def contacts_update(request, contacts_id):
    try:
        if request.method == 'POST':
            contact = Contacts.objects.get(id=contacts_id)
            contact.head = request.POST.get('head')
            contact.coordin_map = request.POST.get('coordin_map')
            contact.city = request.POST.get('city')
            contact.phone1 = request.POST.get('phone1')
            contact.phone2 = request.POST.get('phone2')
            contact.email = request.POST.get('email')
            contact.save()
            return redirect('/account/')
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def static_information_edit(request, info_id):
    try:
        static = PoliticsAndСonfidentiality.objects.get(id=info_id)
        categories = Category.objects.all()
        contacts = Contacts.objects.get(id=1)
        politics = PoliticsAndСonfidentiality.objects.all()
        context = {
            'categories': categories,
            'contacts': contacts,
            'politics': politics,
            'static': static,
        }
        return render(request, 'account/edit_static_info.html', context)
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def static_information_update(request, info_id):
    try:
        if request.method == 'POST':
            static = PoliticsAndСonfidentiality.objects.get(id=info_id)
            static.head = request.POST.get('head')
            static.description = request.POST.get('description')
            static.save()
            return redirect('/account/')
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def reviews_list(request):
    reviews_list = Reviews.objects.all()
    categories = Category.objects.all()
    contacts = Contacts.objects.get(id=1)
    politics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'categories': categories,
        'contacts': contacts,
        'politics': politics,
        'reviews': reviews_list,
    }
    return render(request, 'account/reviews_list.html', context)


def review_create(request):
    categories = Category.objects.all()
    contacts = Contacts.objects.get(id=1)
    politics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'categories': categories,
        'contacts': contacts,
        'politics': politics,
        'reviews': reviews_list,
    }
    return render(request, 'account/create_review.html', context)


def review_edit(request, review_id):
    try:
        review = Reviews.objects.get(id=review_id)
        categories = Category.objects.all()
        contacts = Contacts.objects.get(id=1)
        politics = PoliticsAndСonfidentiality.objects.all()
        context = {
            'categories': categories,
            'contacts': contacts,
            'politics': politics,
            'review': review,
        }
        return render(request, 'account/edit_review.html', context)
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def review_update(request, review_id):
    try:
        if request.is_ajax():
            if request.POST.get('email') != '':
                review = Reviews.objects.get(id=review_id)
                review.name = request.POST.get('name')
                review.email = request.POST.get('email')
                review.text = request.POST.get('text')
                if request.POST.get('anonym') == 'true':
                    review.anonym = True
                else:
                    review.anonym = False
                review.save()
                return JsonResponse({'success': 'success'})
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def review_delete(request, review_id):
    try:
        review = Reviews.objects.get(id=review_id).delete()
        return redirect('/account/reviews/')
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def review_save(request):
    try:
        if request.is_ajax():
            if request.POST.get('email') != '':
                review = Reviews()
                review.name = request.POST.get('name')
                review.email = request.POST.get('email')
                review.text = request.POST.get('text')
                if request.POST.get('anonym') == 'true':
                    review.anonym = True
                else:
                    review.anonym = False
                review.save()
                return JsonResponse({'success': 'success'})
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def main_slider_list(request):
    sliders = MainSlider.objects.all()
    categories = Category.objects.all()
    contacts = Contacts.objects.get(id=1)
    politics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'categories': categories,
        'contacts': contacts,
        'politics': politics,
        'sliders': sliders,
    }
    return render(request, 'account/sliders_list.html', context)


def main_slider_create(request):
    categories = Category.objects.all()
    contacts = Contacts.objects.get(id=1)
    politics = PoliticsAndСonfidentiality.objects.all()
    context = {
        'categories': categories,
        'contacts': contacts,
        'politics': politics,
    }
    return render(request, 'account/main_sliders_create.html', context)


def main_slider_save(request):
    if request.method == 'POST':
        form = CreateSliderForm(request.POST, request.FILES)
        if form.is_valid():
            if 'img' in request.FILES:
                form.img = request.FILES['img']
            form.name = request.POST.get('name')
            form.href = request.POST.get('href')
            form.save()
            return redirect('/account/main-slider/')
        else:
            return HttpResponseNotFound("<h2>Ошибка при сохранении</h2>")


def main_slider_edit(request, slider_id):
    try:
        slide = MainSlider.objects.get(id=slider_id)
        categories = Category.objects.all()
        contacts = Contacts.objects.get(id=1)
        politics = PoliticsAndСonfidentiality.objects.all()
        context = {
            'categories': categories,
            'contacts': contacts,
            'politics': politics,
            'slide': slide,
        }
        return render(request, 'account/main_sliders_edit.html', context)
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def main_slider_update(request, slider_id):
    if request.method == 'POST':
        form = MainSlider.objects.get(id=slider_id)
        if 'img' in request.FILES:
            form.img = request.FILES['img']
        form.name = request.POST.get('name')
        form.href = request.POST.get('href')
        form.save()
        return redirect('/account/main-slider/')
    else:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def main_slider_delete(request, slider_id):
    try:
        slide = MainSlider.objects.get(id=slider_id).delete()
        return redirect('/account/reviews/')
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def main_page_edit(request):
    try:
        mpage = MainPage.objects.get(id=1)
        categories = Category.objects.all()
        contacts = Contacts.objects.get(id=1)
        politics = PoliticsAndСonfidentiality.objects.all()
        context = {
            'categories': categories,
            'contacts': contacts,
            'politics': politics,
            'mpage': mpage,
        }
        return render(request, 'account/main_page.html', context)
    except:
        return HttpResponseNotFound("<h2>Page not found</h2>")


def main_page_update(request, mpage_id):
   if request.method == 'POST':
       try:
            mpage = MainPage.objects.get(id=mpage_id)
            mpage.name = request.POST.get('name')
            mpage.text = request.POST.get('text')
            mpage.save()
            return redirect('/account/')
       except:
           return HttpResponseNotFound("<h2>Ошибка при сохранении</h2>")