from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm       # <<<

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news':news, 'category':category}) #<<< позиционный аргумент (словарь) использовали после именованного, что запрещается, поэтому второй аргумент превращаем в позиционный

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)  #<<< забрали все данные из формы
        if form.is_valid():            #<<< прошла ли форма валидацию?
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()    #<<< форма, связанная с данными
            return redirect(news)      #<<< ссылка на только что созданный объект
    else:
        form = NewsForm()     #<<< простая, не связнанная с данными форма
    return render(request, 'news/add_news.html', {'form': form})


