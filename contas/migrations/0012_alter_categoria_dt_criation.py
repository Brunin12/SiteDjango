# Generated by Django 4.2.3 on 2023-07-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0011_alter_categoria_dt_criation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='dt_criation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
