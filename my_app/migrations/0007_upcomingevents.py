# Generated by Django 3.0.7 on 2021-03-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20210301_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='upcomingevents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_notice', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
    ]
