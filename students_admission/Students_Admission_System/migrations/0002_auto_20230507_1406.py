# Generated by Django 3.0.5 on 2023-05-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students_Admission_System', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='kindergaten',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='application',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
