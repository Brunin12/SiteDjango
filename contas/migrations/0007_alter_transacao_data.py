# Generated by Django 4.2.3 on 2023-07-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0006_remove_transacao_dt_criation_transacao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]