# Generated by Django 3.1 on 2020-08-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iD', models.CharField(max_length=20)),
                ('real_name', models.CharField(max_length=20)),
                ('tz', models.CharField(max_length=20)),
                ('activity_period', models.DateTimeField()),
            ],
        ),
    ]
