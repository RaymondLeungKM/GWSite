# Generated by Django 2.2 on 2020-05-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GWHK', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobopenings',
            name='jobPDF',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
