from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_subscription_format'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='format',
            new_name='report_format',
        ),
    ] 