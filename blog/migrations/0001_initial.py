# Generated by Django 4.2 on 2024-12-01 22:37

from django.db import migrations, models
import django.db.models.deletion


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
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('intro', models.TextField()),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=254)),
                ('image', models.ImageField(upload_to='')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('blog_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('highlight', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
