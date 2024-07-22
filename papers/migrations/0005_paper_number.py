# Generated by Django 5.0.7 on 2024-07-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0004_remove_paper_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='number',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]
