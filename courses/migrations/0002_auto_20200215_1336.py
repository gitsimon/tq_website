# Generated by Django 2.2 on 2020-02-15 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_squashed_0071_offering_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='parent_style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='courses.Style'),
        ),
    ]
