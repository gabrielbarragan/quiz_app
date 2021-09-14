# Generated by Django 3.2.6 on 2021-09-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulty',
            field=models.CharField(choices=[('lit', 'lit'), ('med', 'med'), ('high', 'high')], max_length=6),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='required_score_to_pass',
            field=models.IntegerField(help_text='puntaje requerido en %'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='time',
            field=models.IntegerField(help_text='duración en minutos'),
        ),
    ]
