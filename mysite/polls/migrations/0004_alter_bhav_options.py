# Generated by Django 4.2.4 on 2023-08-31 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_bhav_id_alter_bhav_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bhav',
            options={'ordering': ('code', 'name', 'open', 'high', 'low', 'close')},
        ),
    ]
