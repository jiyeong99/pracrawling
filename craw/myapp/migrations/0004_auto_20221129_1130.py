# Generated by Django 3.2.13 on 2022-11-29 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_data_card_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='card_record',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='benefit',
            name='benefit_content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='benefit',
            name='benefit_detail',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='card_image',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='card_type',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='card_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='fee',
            field=models.TextField(null=True),
        ),
    ]
