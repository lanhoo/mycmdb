# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
            options={
                'verbose_name_plural': '管理员表',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('device_type_id', models.IntegerField(default=1, choices=[(1, '服务器'), (2, '交换机'), (3, '防火墙')])),
                ('device_status_id', models.IntegerField(default=1, choices=[(1, '上架'), (2, '在线'), (3, '离线'), (4, '下架')])),
                ('cabinet_num', models.CharField(max_length=30, null=True, blank=True, verbose_name='机柜号')),
                ('cabinet_order', models.CharField(max_length=30, null=True, blank=True, verbose_name='机柜中序号')),
                ('latest_date', models.DateField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '资产表',
            },
        ),
        migrations.CreateModel(
            name='AssetRecord',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset_obj', models.ForeignKey(to='web.Asset', related_name='ar')),
            ],
            options={
                'verbose_name_plural': '资产记录表',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='业务线')),
            ],
            options={
                'verbose_name_plural': '业务线表',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('slot', models.CharField(max_length=8, verbose_name='插槽位')),
                ('model', models.CharField(max_length=32, verbose_name='磁盘型号')),
                ('capacity', models.FloatField(verbose_name='磁盘容量GB')),
                ('pd_type', models.CharField(max_length=32, verbose_name='磁盘类型')),
            ],
            options={
                'verbose_name_plural': '硬盘表',
            },
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset_obj', models.ForeignKey(to='web.Asset', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': '错误日志表',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='机房')),
                ('floor', models.IntegerField(default=1, verbose_name='楼层')),
            ],
            options={
                'verbose_name_plural': '机房表',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('slot', models.CharField(max_length=32, verbose_name='插槽位')),
                ('manufacturer', models.CharField(max_length=32, null=True, blank=True, verbose_name='制造商')),
                ('model', models.CharField(max_length=64, verbose_name='型号')),
                ('capacity', models.FloatField(null=True, blank=True, verbose_name='容量')),
                ('sn', models.CharField(max_length=64, null=True, blank=True, verbose_name='内存SN号')),
                ('speed', models.CharField(max_length=16, null=True, blank=True, verbose_name='速度')),
            ],
            options={
                'verbose_name_plural': '内存表',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('management_ip', models.CharField(max_length=64, null=True, blank=True, verbose_name='管理IP')),
                ('vlan_ip', models.CharField(max_length=64, null=True, blank=True, verbose_name='VlanIP')),
                ('intranet_ip', models.CharField(max_length=128, null=True, blank=True, verbose_name='内网IP')),
                ('sn', models.CharField(unique=True, max_length=64, verbose_name='SN号')),
                ('manufacture', models.CharField(max_length=128, null=True, blank=True, verbose_name='制造商')),
                ('model', models.CharField(max_length=128, null=True, blank=True, verbose_name='型号')),
                ('port_num', models.SmallIntegerField(null=True, blank=True, verbose_name='端口个数')),
                ('device_detail', models.CharField(max_length=255, null=True, blank=True, verbose_name='设置详细配置')),
                ('asset', models.OneToOneField(to='web.Asset')),
            ],
            options={
                'verbose_name_plural': '网络设备',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='网卡名称')),
                ('hwaddr', models.CharField(max_length=64, verbose_name='网卡mac地址')),
                ('netmask', models.CharField(max_length=64)),
                ('ipaddrs', models.CharField(max_length=256, verbose_name='ip地址')),
                ('up', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '网卡表',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('hostname', models.CharField(unique=True, max_length=128)),
                ('sn', models.CharField(max_length=64, verbose_name='SN号', db_index=True)),
                ('manufacturer', models.CharField(max_length=64, null=True, blank=True, verbose_name='制造商')),
                ('model', models.CharField(max_length=64, null=True, blank=True, verbose_name='型号')),
                ('manage_ip', models.GenericIPAddressField(null=True, blank=True, verbose_name='管理IP')),
                ('os_platform', models.CharField(max_length=16, null=True, blank=True, verbose_name='系统')),
                ('os_version', models.CharField(max_length=16, null=True, blank=True, verbose_name='系统版本')),
                ('cpu_count', models.IntegerField(null=True, blank=True, verbose_name='CPU个数')),
                ('cpu_physical_count', models.IntegerField(null=True, blank=True, verbose_name='CPU物理个数')),
                ('cpu_model', models.CharField(max_length=128, null=True, blank=True, verbose_name='CPU型号')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset', models.OneToOneField(to='web.Asset')),
            ],
            options={
                'verbose_name_plural': '服务器表',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='标签')),
            ],
            options={
                'verbose_name_plural': '标签表',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=32)),
            ],
            options={
                'verbose_name_plural': '用户组表',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=32, verbose_name='座机')),
                ('mobile', models.CharField(max_length=32, verbose_name='手机')),
            ],
            options={
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.AddField(
            model_name='usergroup',
            name='users',
            field=models.ManyToManyField(to='web.UserProfile'),
        ),
        migrations.AddField(
            model_name='nic',
            name='server_obj',
            field=models.ForeignKey(to='web.Server', related_name='nic'),
        ),
        migrations.AddField(
            model_name='memory',
            name='server_obj',
            field=models.ForeignKey(to='web.Server', related_name='memory'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server_obj',
            field=models.ForeignKey(to='web.Server', related_name='disk'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='contact',
            field=models.ForeignKey(to='web.UserGroup', related_name='c', verbose_name='业务联系人'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='manager',
            field=models.ForeignKey(to='web.UserGroup', related_name='m', verbose_name='系统管理员'),
        ),
        migrations.AddField(
            model_name='assetrecord',
            name='creator',
            field=models.ForeignKey(to='web.UserProfile', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(to='web.BusinessUnit', verbose_name='属于的业务线', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(to='web.IDC', verbose_name='IDC机房', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(to='web.Tag'),
        ),
        migrations.AddField(
            model_name='admininfo',
            name='user_info',
            field=models.OneToOneField(to='web.UserProfile'),
        ),
    ]
