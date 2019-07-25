# Generated by Django 2.2.3 on 2019-07-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Desrição')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de Inicio')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='Imagem')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criando em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Curriculo',
                'verbose_name_plural': 'Curriculos',
                'ordering': ['name'],
            },
        ),
    ]
