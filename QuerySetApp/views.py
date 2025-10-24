from django.shortcuts import render
from .models import Book
# Create your views here.

# Основные методы ORM:
# Метод	Назначение	Пример
# all()	Получить все записи	User.objects.all()
# filter()	Отобрать по условию	Article.objects.filter(author="Иван")
# exclude()	Исключить по условию	Article.objects.exclude(published=False)
# get()	Получить одну запись (ошибка, если нет или больше одной)	User.objects.get(id=1)
# order_by()	Сортировка	Article.objects.order_by('-created_at')
# count()	Подсчитать количество	Article.objects.filter(published=True).count()
# first(), last()	Получить первую или последнюю запись	Article.objects.first()
# values()	Вернуть список словарей	User.objects.values('name', 'email')
# distinct()	Убрать дубликаты	User.objects.values('group').distinct()

# 🔹 Условия фильтрации (lookup expressions):
# Lookup	Описание	Пример
# exact	точное совпадение	User.objects.filter(name__exact='Иван')
# iexact	без учёта регистра	User.objects.filter(name__iexact='иван')
# contains	содержит	Article.objects.filter(title__contains='Python')
# icontains	содержит (без регистра)	Article.objects.filter(title__icontains='python')
# gt, gte	больше / больше или равно	Article.objects.filter(views__gte=100)
# lt, lte	меньше / меньше или равно	Article.objects.filter(views__lt=50)
# in	входит в список	User.objects.filter(group__in=['A', 'B'])
# startswith, endswith	начинается/заканчивается	Article.objects.filter(title__startswith='Django')
# isnull	проверка на NULL	Article.objects.filter(description__isnull=True)


def books_view(request):
    expensive_books = Book.objects.filter(price__gt=2000)
    recent_books = Book.objects.filter(year__gt=2010).order_by('year')
    tolstoy_books = Book.objects.filter(author__icontains='Толстой')

    context = {
        'expensive_books': expensive_books,
        'recent_books': recent_books,
        'tolstoy_books': tolstoy_books
    }

    return render(request, 'books.html', context)


def search_view(request):
    query = request.GET.get('author', '')  # получаем значение из формы
    results = []

    if query:
        results = Book.objects.filter(author__icontains=query)  # поиск без учёта регистра

    context = {
        'query': query,
        'results': results
    }
    return render(request, 'search.html', context)
