# Generated by Django 4.0 on 2021-12-25 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admins', '0006_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_at', models.DateTimeField()),
                ('correct_question_ids', models.CharField(max_length=255)),
                ('complete_terminate', models.BooleanField(default=False)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.paper')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
