# Generated by Django 3.1.5 on 2021-01-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0003_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='profiles')),
            ],
        ),
    ]
