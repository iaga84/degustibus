# Generated by Django 3.0.6 on 2020-06-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0007_auto_20200518_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='format',
            field=models.CharField(choices=[('da-leggere', 'Da leggere'), ('audio', 'Audio'), ('cartaceo', 'Cartaceo'), ('ebook', 'E-Book')], max_length=1024),
        ),
        migrations.AlterField(
            model_name='book',
            name='suggested_by',
            field=models.CharField(blank=True, choices=[('ale', 'Ale'), ('audible', 'Audible'), ('amici', 'Amici'), ('autonoma', 'Ricerca autonoma'), ('autore-piaciuto', 'Autore piaciuto'), ('caso', 'Il Caso'), ('circolo', 'Il Circolo di lettura'), ('post', 'Il Post'), ('venerdi', 'Il Venerdi'), ('facebook', 'Facebook'), ('internazionale', "L'Internazionale"), ('lettore-piaciuto', 'Lettore piaciuto'), ('murgia', 'Michela Murgia'), ('pinterest', 'Pinterest'), ('reddit', 'Reddit'), ('tv', 'TV')], max_length=1024, null=True),
        ),
    ]
