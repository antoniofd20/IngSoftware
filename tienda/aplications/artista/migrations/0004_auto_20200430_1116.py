# Generated by Django 3.0.5 on 2020-04-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0003_auto_20200430_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='last_name',
            field=models.CharField(blank=True, max_length=15, verbose_name='Apellido'),
        ),
    ]