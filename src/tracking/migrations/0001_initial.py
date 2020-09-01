# Generated by Django 3.0.6 on 2020-05-18 12:30

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=1024)),
                ('last_name', models.CharField(max_length=1024)),
                ('gender', models.CharField(choices=[('uomo', 'Uomo'), ('donna', 'Donna'), ('altro', 'Altro')], max_length=1024)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1024)),
                ('publish_year', models.IntegerField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('read_start_date', models.DateField(blank=True, null=True)),
                ('read_end_date', models.DateField(blank=True, null=True)),
                ('suggested_by', models.CharField(blank=True, choices=[('autonoma', 'Ricerca autonoma'), ('caso', 'Il Caso'), ('internazionale', "L'Internazionale"), ('post', 'Il Post'), ('venerdi', 'Il Venerdi'), ('murgia', 'La Murgia'), ('pinterest', 'Pinterest'), ('reddit', 'Reddit'), ('facebook', 'Facebook'), ('ale', 'Ale'), ('circolo', 'Il Circolo di lettura'), ('amici', 'Amici'), ('tv', 'TV')], max_length=1024, null=True)),
                ('suggested_date', models.DateField(blank=True, null=True)),
                ('original_title', models.CharField(blank=True, max_length=1024, null=True)),
                ('format', models.CharField(choices=[('cartaceo', 'Cartaceo'), ('ebook', 'E-Book'), ('audio', 'Audio')], max_length=1024)),
                ('format_details', models.CharField(choices=[('kindle', 'Kindle'), ('prestito', 'Prestito'), ('comprato', 'Comprato'), ('biblioteca', 'Biblioteca'), ('altro', 'Altro'), ('audible', 'Audible'), ('alta-voce', 'Ad alta voce'), ('wikiradio', 'Wikiradio'), ('raiplay', 'RaiPlay'), ('mp3', 'MP3'), ('youtube', 'YouTube')], max_length=1024)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('reading_time', models.FloatField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='author_books', to='tracking.Person')),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Collection')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='genre_books', to='tracking.Genre')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='language_books', to='tracking.Language')),
                ('original_language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='original_language_books', to='tracking.Language')),
                ('prizes', models.ManyToManyField(blank=True, null=True, to='tracking.Prize')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Publisher')),
                ('reader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Person')),
                ('sub_genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub_genre_books', to='tracking.Genre')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]