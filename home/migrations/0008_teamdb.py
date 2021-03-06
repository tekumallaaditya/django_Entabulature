# Generated by Django 2.1.2 on 2018-10-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_interiorpicsdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='teamDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=100)),
                ('pic', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'team',
            },
        ),
    ]
