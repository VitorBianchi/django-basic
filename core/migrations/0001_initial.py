# Generated by Django 3.0.4 on 2020-03-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade em Estoque')),
            ],
        ),
    ]
