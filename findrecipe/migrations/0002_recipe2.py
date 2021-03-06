# Generated by Django 3.0.6 on 2020-05-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findrecipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=5000)),
                ('ingredient', models.ManyToManyField(to='findrecipe.Ingredient')),
            ],
        ),
    ]
