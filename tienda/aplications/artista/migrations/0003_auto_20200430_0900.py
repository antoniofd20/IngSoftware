# Generated by Django 3.0.5 on 2020-04-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0002_auto_20200427_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='genero',
            field=models.CharField(choices=[('0', 'Pop'), ('1', 'Rock'), ('2', 'Metal'), ('3', 'Electrónica'), ('4', 'Reggaeton'), ('5', 'Baladas'), ('6', 'Regional mexicano'), ('7', 'Banda'), ('8', 'Cumbia'), ('9', 'Salsa'), ('10', 'Alternativa'), ('11', 'Rap')], max_length=20, verbose_name='Género'),
        ),
    ]
