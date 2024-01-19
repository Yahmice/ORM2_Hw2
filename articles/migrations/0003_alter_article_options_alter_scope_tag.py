# Generated by Django 4.2.9 on 2024-01-19 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag'),
        ),
    ]