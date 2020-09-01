# Generated by Django 3.0.6 on 2020-05-18 17:12

from django.db import migrations, models
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormatDetail',
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
        migrations.RemoveField(
            model_name='book',
            name='format_details',
        ),
        migrations.AddField(
            model_name='book',
            name='geographical_setting',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]