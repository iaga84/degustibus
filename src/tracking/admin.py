from django.contrib import admin

# Register your models here.
from django_admin_listfilter_dropdown.filters import DropdownFilter

from .models import Person, Book, Language, Genre, Publisher, Prize, Collection, FormatDetail, Attachment, Source


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created_on', 'updated_on']


@admin.register(Person)
class PersonAdmin(BaseAdmin):
    list_filter = (
        ('country', DropdownFilter),
        ('gender', DropdownFilter),
    )


@admin.register(Book)
class BookAdmin(BaseAdmin):
    list_display = ['title', 'author', 'publish_year', 'rating', 'read_end_date', 'format', 'publisher']
    list_filter = (
        ('author__country', DropdownFilter),
        ('author__gender', DropdownFilter),
        ('geographical_setting', DropdownFilter),
        ('format', DropdownFilter),
        ('publisher__name', DropdownFilter),
    )
    date_hierarchy = 'read_end_date'
    ordering = ['-read_end_date', 'title']


@admin.register(Language)
class LanguageAdmin(BaseAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(BaseAdmin):
    pass


@admin.register(FormatDetail)
class FormatDetailAdmin(BaseAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(BaseAdmin):
    pass


@admin.register(Source)
class SourceAdmin(BaseAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(BaseAdmin):
    pass


@admin.register(Prize)
class PrizeAdmin(BaseAdmin):
    pass


@admin.register(Attachment)
class AttachmentAdmin(BaseAdmin):
    fields = ['image_tag']
    readonly_fields = ['image_tag']
