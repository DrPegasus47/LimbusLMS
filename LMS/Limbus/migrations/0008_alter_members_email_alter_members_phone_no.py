# Generated by Django 4.1.3 on 2023-06-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Limbus', '0007_publishers_returnedbooks_book_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='phone_no',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
