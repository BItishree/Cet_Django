# Generated by Django 3.0.7 on 2021-03-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_auto_20210301_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingeventss',
            name='event_name',
            field=models.TextField(),
        ),
    ]
