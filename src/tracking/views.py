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
                "title": {"type": "text", "term_vector": "yes"},
                "publish_year": {"type": "keyword"},
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
            "publish_year": book.publish_year
        }

        ES.index(index=DOCUMENTS_INDEX, body=record)

    logging.warning("ELASTIC REFRESHED")
    return render(request, 'index.html', {
    })
