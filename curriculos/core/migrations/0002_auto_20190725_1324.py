# Generated by Django 2.2.3 on 2019-07-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Imagem'),
        ),
    ]
