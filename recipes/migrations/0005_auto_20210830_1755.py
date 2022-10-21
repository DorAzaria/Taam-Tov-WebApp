# Generated by Django 3.2.6 on 2021-08-30 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('recipes', '0004_recipe_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('owner', 'recipe')},
        ),
    ]
