# Generated by Django 2.2 on 2020-05-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GWHK', '0002_jobopenings_jobpdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='pressRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField()),
                ('published_date', models.DateField()),
            ],
        ),
    ]
