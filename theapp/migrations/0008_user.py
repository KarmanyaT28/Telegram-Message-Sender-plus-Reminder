# Generated by Django 3.1.5 on 2021-01-24 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0007_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles')),
            ],
        ),
    ]