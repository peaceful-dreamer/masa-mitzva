# Generated by Django 4.1.4 on 2023-01-26 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'תלמיד', 'verbose_name_plural': 'תלמידים'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'מורה', 'verbose_name_plural': 'מורים'},
        ),
    ]