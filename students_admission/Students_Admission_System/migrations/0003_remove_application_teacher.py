# Generated by Django 3.0.5 on 2023-05-15 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Students_Admission_System', '0002_auto_20230507_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='teacher',
        ),
    ]
