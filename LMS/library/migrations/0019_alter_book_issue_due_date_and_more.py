# Generated by Django 5.0.6 on 2024-05-25 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_auto_20220910_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 2, 17, 56, 21, 301246), help_text='Date the book is due to'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book_number',
            field=models.PositiveIntegerField(help_text='Book number for books of the save kind', null=True),
        ),
    ]
