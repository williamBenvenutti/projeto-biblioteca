# Generated by Django 4.2.1 on 2023-06-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=35)),
                ('cpf', models.CharField(max_length=11)),
                ('idade', models.IntegerField()),
                ('rua', models.CharField(max_length=60)),
                ('bairro', models.CharField(max_length=60)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=50)),
                ('senha', models.CharField(max_length=80)),
            ],
        ),
    ]
