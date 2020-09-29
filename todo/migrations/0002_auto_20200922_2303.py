# Generated by Django 2.2.13 on 2020-09-22 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='images',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(blank=True, choices=[('danger', 'high'), ('info', 'normal'), ('success', 'low')], default='normal', max_length=50, null=True),
        ),
    ]
