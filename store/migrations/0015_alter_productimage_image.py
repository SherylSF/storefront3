# Generated by Django 4.2.14 on 2024-07-15 13:29

from django.db import migrations, models
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='store/images', validators=[store.validators.validate_file_size]),
        ),
    ]
