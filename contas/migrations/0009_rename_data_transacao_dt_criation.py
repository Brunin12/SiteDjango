# Generated by Django 4.2.3 on 2023-07-17 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0008_alter_transacao_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transacao',
            old_name='data',
            new_name='dt_criation',
        ),
    ]
