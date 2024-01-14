# Generated by Django 3.2.8 on 2024-01-13 09:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('messageID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=100)),
                ('status', models.CharField(choices=[('RESOLVED', 'RESOLVED'), ('UNRESOLVED', 'UNRESOLVED')], default='UNRESOLVED', max_length=30)),
            ],
        ),
    ]