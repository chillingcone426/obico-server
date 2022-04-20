# Generated by Django 2.2.27 on 2022-04-10 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def forwards(apps, schema_editor):
    if schema_editor.connection.vendor == 'postgresql':
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'email', id, '', 't', alert_by_email, notify_on_done and print_notification_by_email, notify_on_canceled and print_notification_by_email, notify_on_filament_change_req and print_notification_by_email, 'f', 'f', now(), now() from app_user;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'discord', id, '{"webhook_url": "' || discord_webhook || '"}', 't', 't', notify_on_done and print_notification_by_discord, notify_on_canceled and print_notification_by_discord, notify_on_filament_change_req and print_notification_by_discord, 'f', 'f', now(), now() from app_user where discord_webhook is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'telegram', id, '{"chat_id": "' || telegram_chat_id || '"}', 't', 't', notify_on_done and print_notification_by_telegram, notify_on_canceled and print_notification_by_telegram, notify_on_filament_change_req and print_notification_by_telegram, 'f', 'f', now(), now() from app_user where telegram_chat_id is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json,  enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'slack', id, '{"access_token": "' || slack_access_token || '"}', 't', 't', 't', 'f', 't', 'f', 'f', now(), now() from app_user where slack_access_token is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'pushbullet', id, '{"access_token": "' || pushbullet_access_token || '"}', 't', 't', notify_on_done and print_notification_by_pushbullet, notify_on_canceled and print_notification_by_pushbullet, notify_on_filament_change_req and print_notification_by_pushbullet, 'f', 'f', now(), now() from app_user where  pushbullet_access_token is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'pushover', id, '{"user_key": "' || pushover_user_token || '"}', 't', 't', notify_on_done and print_notification_by_pushover, notify_on_canceled and print_notification_by_pushover, notify_on_filament_change_req and print_notification_by_pushover, 'f', 'f', now(), now() from app_user where  pushover_user_token is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'twilio', id, '{"phone_country_code": "' || phone_country_code || '", "phone_number": "' || phone_number || '"}', 't', alert_by_sms, 'f', 'f', 'f', 'f', 'f', now(), now() from app_user where  phone_number is not null and phone_country_code is not null;
            """)

    if schema_editor.connection.vendor == 'sqlite':
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'email', id, '', 't', alert_by_email, notify_on_done and print_notification_by_email, notify_on_canceled and print_notification_by_email, notify_on_filament_change_req and print_notification_by_email, 'f', 'f', date(), date() from app_user;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'discord', id, '{"webhook_url": "' || discord_webhook || '"}', 't', 't', notify_on_done and print_notification_by_discord, notify_on_canceled and print_notification_by_discord, notify_on_filament_change_req and print_notification_by_discord, 'f', 'f', date(), date() from app_user where discord_webhook is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'telegram', id, '{"chat_id": "' || telegram_chat_id || '"}', 't', 't', notify_on_done and print_notification_by_telegram, notify_on_canceled and print_notification_by_telegram, notify_on_filament_change_req and print_notification_by_telegram, 'f', 'f', date(), date() from app_user where telegram_chat_id is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json,  enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'slack', id, '{"access_token": "' || slack_access_token || '"}', 't', 't', 't', 'f', 't', 'f', 'f', date(), date() from app_user where slack_access_token is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'pushbullet', id, '{"access_token": "' || pushbullet_access_token || '"}', 't', 't', notify_on_done and print_notification_by_pushbullet, notify_on_canceled and print_notification_by_pushbullet, notify_on_filament_change_req and print_notification_by_pushbullet, 'f', 'f', date(), date() from app_user where  pushbullet_access_token is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'pushover', id, '{"user_key": "' || pushover_user_token || '"}', 't', 't', notify_on_done and print_notification_by_pushover, notify_on_canceled and print_notification_by_pushover, notify_on_filament_change_req and print_notification_by_pushover, 'f', 'f', date(), date() from app_user where  pushover_user_token is not null;
            """)
        schema_editor.execute("""
                insert into app_notificationsetting(name, user_id, config_json, enabled, notify_on_failure_alert, notify_on_print_done, notify_on_print_cancelled, notify_on_filament_change, notify_on_other_print_events, notify_on_heater_status, created_at, updated_at)
                select 'twilio', id, '{"phone_country_code": "' || phone_country_code || '", "phone_number": "' || phone_number || '"}', 't', alert_by_sms, 'f', 'f', 'f', 'f', 'f', date(), date() from app_user where  phone_number is not null and phone_country_code is not null;
            """)

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_auto_20220318_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notification_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='NotificationSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('config_json', models.TextField(blank=True, default='')),
                ('enabled', models.BooleanField(default=True)),
                ('notify_on_failure_alert', models.BooleanField(blank=True, default=True)),
                ('notify_on_print_done', models.BooleanField(blank=True, default=True)),
                ('notify_on_print_cancelled', models.BooleanField(blank=True, default=False)),
                ('notify_on_filament_change', models.BooleanField(blank=True, default=True)),
                ('notify_on_other_print_events', models.BooleanField(blank=True, default=False)),
                ('notify_on_heater_status', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
        migrations.RunPython(forwards, reverse_func),
    ]
