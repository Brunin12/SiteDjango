# Generated by Django 4.2.3 on 2023-07-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_criation', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
