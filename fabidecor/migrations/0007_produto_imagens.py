# Generated by Django 4.2.5 on 2023-10-03 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('fabidecor', '0006_alter_produto_tema'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagens',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]
