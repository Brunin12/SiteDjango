# Generated by Django 4.2.3 on 2023-07-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0009_rename_data_transacao_dt_criation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='dt_criation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
