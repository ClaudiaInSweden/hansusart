# Generated by Django 4.2 on 2024-10-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('width', models.CharField(max_length=254)),
                ('height', models.CharField(max_length=254)),
                ('description', models.CharField(max_length=254)),
                ('highlight', models.BooleanField(default=False)),
                ('sold', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('category', models.ManyToManyField(to='products.category')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]