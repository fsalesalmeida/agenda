# Generated by Django 3.0.5 on 2020-04-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/'),
        ),
    ]
