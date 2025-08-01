# Generated by Django 5.2.4 on 2025-07-15 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='relationship_app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('library', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='librarian', serialize=False, to='relationship_app.library')),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(related_name='libraries', to='relationship_app.book'),
        ),
    ]
