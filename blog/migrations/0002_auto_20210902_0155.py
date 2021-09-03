# Generated by Django 3.2.7 on 2021-09-01 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('body', models.TextField()),
                ('data_pub', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
