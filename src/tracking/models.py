import uuid

from django.db import models
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField

GENDER_CHOICES = [
    ('altro', 'Altro'),
    ('donna', 'Donna'),
    ('uomo', 'Uomo'),
]

BOOK_FORMAT_CHOICES = [
    ('da-leggere', 'Da leggere'),
    ('audio', 'Audio'),
    ('cartaceo', 'Cartaceo'),
    ('ebook', 'E-Book'),
]

SOURCE_CHOICES = [
    ('ale', 'Ale'),
    ('audible', 'Audible'),
    ('amici', 'Amici'),
    ('autonoma', 'Ricerca autonoma'),
    ('autore-piaciuto', 'Autore piaciuto'),
    ('caso', 'Il Caso'),
    ('circolo', 'Il Circolo di lettura'),
    ('post', 'Il Post'),
    ('venerdi', 'Il Venerdi'),
    ('facebook', 'Facebook'),
    ('internazionale', 'L\'Internazionale'),
    ('lettore-piaciuto', 'Lettore piaciuto'),
    ('murgia', 'Michela Murgia'),
    ('pinterest', 'Pinterest'),
    ('reddit', 'Reddit'),
    ('tv', 'TV'),
]


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(BaseModel):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class FormatDetail(BaseModel):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Language(BaseModel):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Publisher(BaseModel):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Collection(BaseModel):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Source(BaseModel):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Prize(BaseModel):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Person(BaseModel):
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    gender = models.CharField(max_length=1024, choices=GENDER_CHOICES)
    country = CountryField()
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('first_name',)


class Attachment(models.Model):
    image = models.ImageField(upload_to='uploads/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'


class Book(BaseModel):
    title = models.CharField(max_length=1024)
    author = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='author_books')
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, related_name='language_books')
    illustrator = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='illustrator_books', null=True, blank=True)
    geographical_setting = CountryField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, related_name='genre_books', null=True, blank=True)
    sub_genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, related_name='sub_genre_books', null=True, blank=True)
    translator = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='translator_books', null=True, blank=True)
    reader = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='reader_books', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, null=True, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.DO_NOTHING, null=True, blank=True)
    publish_year = models.IntegerField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    original_language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, related_name='original_language_books', null=True, blank=True)
    original_title = models.CharField(max_length=1024, null=True, blank=True)
    prizes = models.ManyToManyField(Prize, blank=True)
    rating = models.FloatField(null=True, blank=True)
    read_start_date = models.DateField(null=True, blank=True)
    read_end_date = models.DateField(null=True, blank=True)
    suggested_by = models.CharField(max_length=1024, choices=SOURCE_CHOICES, null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING, null=True, blank=True)
    suggested_date = models.DateField(null=True, blank=True)
    format = models.CharField(max_length=1024, choices=BOOK_FORMAT_CHOICES)
    format_details = models.ForeignKey(FormatDetail, on_delete=models.DO_NOTHING, related_name='original_language_books', null=True, blank=True)
    reading_time = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    attachments = models.ManyToManyField(Attachment, blank=True)


    def __str__(self):
        return '{} ({}, {})'.format(self.title, self.author, self.publish_year)

    @property
    def geographical_setting_name(self):
        return self.geographical_setting.name

    class Meta:
        ordering = ('title',)
