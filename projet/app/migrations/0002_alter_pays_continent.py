# Generated by Django 4.2.2 on 2023-06-16 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pays',
            name='continent',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pays', to='app.continent'),
            preserve_default=False,
        ),
    ]
