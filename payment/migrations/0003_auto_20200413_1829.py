# Generated by Django 2.2.11 on 2020-04-13 18:29

from django.db import migrations, models
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20200331_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfinancefile',
            name='file',
            field=models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(bucket_name='tanzquotient-postfinance', custom_domain='tanzquotient-data.s3.amazonaws.com'), upload_to=''),
        ),
    ]
