# Generated by Django 3.2.6 on 2021-10-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='intro',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
