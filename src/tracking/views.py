from django.shortcuts import render
import logging

from elasticsearch import Elasticsearch

from .models import Book

ES = Elasticsearch(['degustibus-elasticsearch:9200'])
DOCUMENTS_INDEX = 'degustibus'


def initialize_index():
    body_documents = {
        "settings": {
            "number_of_shards": 5
        },
        "mappings": {
            "_source": {
                "enabled": True
            },
            "properties": {
                "title": {"type": "keyword"},
                "author_name": {"type": "keyword"},
                "author_gender": {"type": "keyword"},
                "author_country": {"type": "keyword"},
                "author_date_of_birth": {"type": "date"},
                "author_date_of_death": {"type": "date"},
                "language": {"type": "keyword"},
                "geographical_setting": {"type": "keyword"},
                "genre": {"type": "keyword"},
                "sub_genre": {"type": "keyword"},
                "translator": {"type": "keyword"},
                "reader": {"type": "keyword"},
                "publisher": {"type": "keyword"},
                "collection": {"type": "keyword"},
                "publish_year": {"type": "date", "format": "yyyy"},
                "pages": {"type": "integer"},
                "original_language": {"type": "keyword"},
                "original_title": {"type": "keyword"},
                "rating": {"type": "float"},
                "read_start_date": {"type": "date"},
                "read_end_date": {"type": "date"},
                "suggested_by": {"type": "keyword"},
                "source": {"type": "keyword"},
                "suggested_date": {"type": "date"},
                "format": {"type": "keyword"},
                "format_details": {"type": "keyword"},
                "reading_time": {"type": "float"},
            }
        }
    }
    ES.indices.create(index=DOCUMENTS_INDEX, body=body_documents, ignore=400)


def reset_index():
    ES.indices.delete(index=DOCUMENTS_INDEX, ignore=404)
    initialize_index()


def home(request):
    return render(request, 'index.html', {
    })


def refresh_elastic(request):
    reset_index()
    for book in Book.objects.all():
        record = {
            "title": book.title,
            "author_name": str(book.author),
            "author_gender": book.author.gender if book.author else None,
            "author_country": book.author.country.code if book.author and book.author.country else None,
            "author_date_of_birth": book.author.date_of_birth if book.author else None,
            "author_date_of_death": book.author.date_of_death if book.author else None,
            "language": book.language.name if book.language else None,
            "geographical_setting": book.geographical_setting.code if book.geographical_setting else None,
            "genre": book.genre.name if book.genre else None,
            "sub_genre": book.sub_genre.name if book.sub_genre else None,
            "translator": str(book.translator) if book.translator else None,
            "reader": str(book.reader) if book.reader else None,
            "publisher": book.publisher.name if book.publisher else None,
            "collection": book.collection.name if book.collection else None,
            "publish_year": book.publish_year,
            "pages": book.pages,
            "original_language": book.original_language.name if book.original_language else None,
            "original_title": book.original_title,
            "rating": book.rating,
            "read_start_date": book.read_start_date,
            "read_end_date": book.read_end_date,
            "suggested_by": book.suggested_by,
            "source": book.source.name if book.source else None,
            "suggested_date": book.suggested_date,
            "format": book.format,
            "format_details": book.format_details.name if book.format_details else None,
            "reading_time": book.reading_time,
        }

        ES.index(index=DOCUMENTS_INDEX, body=record)

    logging.warning("ELASTIC REFRESHED")
    return render(request, 'index.html', {
    })
