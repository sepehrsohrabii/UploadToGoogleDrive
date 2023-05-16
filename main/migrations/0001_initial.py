# Generated by Django 3.1 on 2023-05-15 18:45

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sample_name', models.CharField(max_length=200)),
                ('sample_data', models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='test/')),
            ],
        ),
    ]
