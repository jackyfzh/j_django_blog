# Generated by Django 2.2 on 2020-06-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0003_auto_20200630_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='act',
            name='title',
            field=models.CharField(default='动态', max_length=500),
        ),
    ]
