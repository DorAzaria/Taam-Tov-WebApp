# Generated by Django 3.2.6 on 2021-08-28 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('recipes', '0003_recipe_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
