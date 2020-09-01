from django.shortcuts import render
from django.db.models import Count
from django_countries import countries

from .models import Book, Person


def home(request):
    filter = request.GET.get('filter', None)
    if filter is not None and filter.lower() == 'audio':
        base_queryset = Book.objects.filter(format='audio')
        queryset_author_nationality = Person.objects.filter(author_books__format='audio').distinct().values('country').annotate(Count('country', distinct=True)).order_by('-country__count')
        queryset_author_gender = Person.objects.filter(author_books__format='audio').distinct().values('gender').annotate(Count('gender', distinct=True)).order_by('-gender__count')
    elif filter is not None:
        base_queryset = Book.objects.exclude(format='audio')
        queryset_author_nationality = Person.objects.all().exclude(author_books__isnull=True).exclude(author_books__format='audio').distinct().values('country').annotate(Count('country')).order_by('-country__count')
        queryset_author_gender = Person.objects.all().exclude(author_books__isnull=True).exclude(author_books__format='audio').distinct().values('gender').annotate(Count('gender')).order_by('-gender__count')
    else:
        base_queryset = Book.objects.all()
        queryset_author_nationality = Person.objects.all().exclude(author_books__isnull=True).values('country').annotate(Count('country')).order_by('-country__count')
        queryset_author_gender = Person.objects.all().exclude(author_books__isnull=True).values('gender').annotate(Count('gender')).order_by('-gender__count')
    queryset_books_by_geographical_setting = base_queryset.values('geographical_setting').annotate(Count('geographical_setting')).order_by('-geographical_setting__count')
    books_by_geographical_setting_labels = []
    books_by_geographical_setting_data = []
    for record in queryset_books_by_geographical_setting:
        try:
            books_by_geographical_setting_labels.append(dict(countries)[record['geographical_setting']])
            books_by_geographical_setting_data.append(record['geographical_setting__count'])
        except KeyError:
            pass

    queryset_books_by_author_nationality = base_queryset.values('author__country').annotate(Count('author__country')).order_by('-author__country__count')
    tmp_books_by_author_nationality_labels = []
    tmp_books_by_author_nationality_data = []
    for record in queryset_books_by_author_nationality:
        tmp_books_by_author_nationality_labels.append(dict(countries)[record['author__country']])
        tmp_books_by_author_nationality_data.append(record['author__country__count'])

    author_nationality_labels = []
    author_nationality_data = []
    for record in queryset_author_nationality:
        author_nationality_labels.append(dict(countries)[record['country']])
        author_nationality_data.append(record['country__count'])
    books_by_author_nationality_labels = sorted(tmp_books_by_author_nationality_labels, key=lambda x: author_nationality_labels.index(x))
    books_by_author_nationality_data = [tmp_books_by_author_nationality_data[tmp_books_by_author_nationality_labels.index(x)] for x in author_nationality_labels]

    queryset_books_by_author_gender = base_queryset.values('author__gender').annotate(Count('author__gender')).order_by('-author__gender__count')
    tmp_books_by_author_gender_labels = []
    tmp_books_by_author_gender_data = []
    for record in queryset_books_by_author_gender:
        tmp_books_by_author_gender_labels.append(record['author__gender'])
        tmp_books_by_author_gender_data.append(record['author__gender__count'])


    author_gender_labels = []
    author_gender_data = []
    for record in queryset_author_gender:
        author_gender_labels.append(record['gender'])
        author_gender_data.append(record['gender__count'])
    books_by_author_gender_labels = sorted(tmp_books_by_author_gender_labels, key=lambda x: author_gender_labels.index(x))
    books_by_author_gender_data = [tmp_books_by_author_gender_data[tmp_books_by_author_gender_labels.index(x)] for x in author_gender_labels]

    queryset_books_by_author_gender_by_year_male = Book.objects.filter(read_end_date__isnull=False, author__gender='uomo').values('read_end_date__year').annotate(Count('id')).order_by('read_end_date__year')
    queryset_books_by_author_gender_by_year_female = Book.objects.filter(read_end_date__isnull=False, author__gender='donna').values('read_end_date__year').annotate(Count('id')).order_by('read_end_date__year')
    queryset_books_by_year = Book.objects.filter(read_end_date__isnull=False).values('read_end_date__year').annotate(Count('id')).order_by('read_end_date__year')

    books_by_year_labels = [str(x['read_end_date__year']) for x in queryset_books_by_year]
    books_by_author_gender_by_year_male_data = []
    for record in queryset_books_by_author_gender_by_year_male:
        books_by_author_gender_by_year_male_data.append(record['id__count'])
    books_by_author_gender_by_year_female_data = []
    for record in queryset_books_by_author_gender_by_year_female:
        books_by_author_gender_by_year_female_data.append(record['id__count'])

    print(books_by_year_labels)
    print(books_by_author_gender_by_year_male_data)
    print(books_by_author_gender_by_year_female_data)

    return render(request, 'index.html', {
        'books_by_geographical_setting_labels': books_by_geographical_setting_labels,
        'books_by_geographical_setting_data': books_by_geographical_setting_data,
        'books_by_author_nationality_labels': books_by_author_nationality_labels,
        'books_by_author_nationality_data': books_by_author_nationality_data,
        'author_nationality_labels': author_nationality_labels,
        'author_nationality_data': author_nationality_data,
        'books_by_author_gender_labels': books_by_author_gender_labels,
        'books_by_author_gender_data': books_by_author_gender_data,
        'author_gender_labels': author_gender_labels,
        'author_gender_data': author_gender_data,
        'books_by_year_labels': books_by_year_labels,
        'books_by_author_gender_by_year_male_data': books_by_author_gender_by_year_male_data,
        'books_by_author_gender_by_year_female_data': books_by_author_gender_by_year_female_data,

    })
