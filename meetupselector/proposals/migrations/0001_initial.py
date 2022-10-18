# Generated by Django 3.2.16 on 2022-10-18 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('talks', '0005_talk_topics'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(verbose_name='description')),
                ('difficulty', models.CharField(choices=[('E', 'easy'), ('M', 'medium'), ('H', 'hard')], default='E', max_length=1, verbose_name='difficulty')),
                ('language', models.CharField(choices=[('ES_ES', 'spanish'), ('ES_CA', 'catalonian'), ('ES_GL', 'galician'), ('ES_EU', 'basque'), ('ES_GB', 'english'), ('FR_FR', 'french')], default='ES_ES', max_length=5, verbose_name='language')),
                ('done', models.BooleanField(default=False, verbose_name='done')),
                ('liked_by', models.ManyToManyField(related_name='proposal_votes', to=settings.AUTH_USER_MODEL, verbose_name='liked_by')),
                ('proposed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposal', to=settings.AUTH_USER_MODEL)),
                ('talks', models.ManyToManyField(related_name='proposals', to='talks.Talk', verbose_name='talks')),
                ('topics', models.ManyToManyField(related_name='proposals', to='talks.Topic', verbose_name='topics')),
            ],
            options={
                'verbose_name': 'proposal',
                'verbose_name_plural': 'proposals',
            },
        ),
    ]
