# Generated by Django 4.0.6 on 2022-08-01 13:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pesapal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=8, null=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, null=True)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiptdate', models.DateTimeField()),
                ('file', models.FileField(max_length=15, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('status', models.CharField(max_length=6, null=True)),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('pin', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='customer',
            name='firstname',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=8, null=True)),
                ('transaction_amount', models.IntegerField(null=True)),
                ('transaction_type', models.CharField(max_length=15, null=True)),
                ('transaction_charge', models.IntegerField(null=True)),
                ('transactiondateandtime', models.DateTimeField(default=datetime.datetime.now)),
                ('Receipt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pesapal.receipt')),
                ('destination_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_b', to='pesapal.account')),
                ('origin_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_a', to='pesapal.account')),
            ],
        ),
        migrations.CreateModel(
            name='Thirdparty',
            fields=[
                ('name', models.CharField(max_length=15, null=True)),
                ('Phone_number', models.CharField(max_length=12, null=True)),
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pesapal.account')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_id', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('points', models.IntegerField(null=True)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pesapal.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_number', models.IntegerField(null=True)),
                ('loan_type', models.CharField(max_length=32, null=True)),
                ('amount', models.BigIntegerField(null=True)),
                ('dateandtime', models.DateTimeField(default=datetime.datetime.now)),
                ('loanbalance', models.IntegerField(null=True)),
                ('loanterm', models.IntegerField(null=True)),
                ('payduedate', models.DateTimeField(default=datetime.datetime.now)),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pesapal.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=15, null=True)),
                ('date_issue', models.DateTimeField(default=datetime.datetime.now)),
                ('card_type', models.CharField(max_length=14, null=True)),
                ('Account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pesapal.account')),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pesapal.wallet')),
            ],
        ),
    ]
