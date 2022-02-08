# Generated by Django 4.0.1 on 2022-02-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('nascimento', models.DateField()),
                ('saldo', models.FloatField(default=0, editable=False)),
            ],
        ),
    ]
