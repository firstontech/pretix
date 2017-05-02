# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-02 09:04
from __future__ import unicode_literals

import django.db.migrations.operations.special
import django.db.models.deletion
import i18nfield.fields
from django.db import migrations, models

import pretix.base.models.base


def migrate_global_settings(apps, schema_editor):
    GlobalSetting = apps.get_model('pretixbase', 'GlobalSetting')
    GlobalSettingsObject_SettingsStore = apps.get_model('pretixbase', 'GlobalSettingsObject_SettingsStore')

    l = []
    for s in GlobalSetting.objects.all():
        l.append(GlobalSettingsObject_SettingsStore(key=s.key, value=s.value))

    GlobalSettingsObject_SettingsStore.objects.bulk_create(l)


class Migration(migrations.Migration):

    replaces = [('pretixbase', '0051_auto_20170206_2027'), ('pretixbase', '0052_auto_20170324_1506'), ('pretixbase', '0053_auto_20170409_1651'), ('pretixbase', '0054_auto_20170413_1050'), ('pretixbase', '0055_auto_20170413_1537'), ('pretixbase', '0056_auto_20170414_1044'), ('pretixbase', '0057_auto_20170501_2116')]

    dependencies = [
        ('pretixbase', '0050_orderposition_positionid_squashed_0061_event_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaitingListEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='On waiting list since')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail address')),
                ('locale', models.CharField(default='en', max_length=190)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waitinglistentries', to='pretixbase.Event', verbose_name='Event')),
                ('item', models.ForeignKey(help_text='The product the user waits for.', on_delete=django.db.models.deletion.CASCADE, related_name='waitinglistentries', to='pretixbase.Item', verbose_name='Product')),
                ('variation', models.ForeignKey(blank=True, help_text='The variation of the product selected above.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waitinglistentries', to='pretixbase.ItemVariation', verbose_name='Product variation')),
                ('voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Voucher', verbose_name='Assigned voucher')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name_plural': 'Waiting list entries',
                'verbose_name': 'Waiting list entry',
            },
            bases=(models.Model, pretix.base.models.base.LoggingMixin),
        ),
        migrations.AlterField(
            model_name='cachedcombinedticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('invoice_no',)},
        ),
        migrations.AlterModelOptions(
            name='orderposition',
            options={'ordering': ('positionid', 'id'), 'verbose_name': 'Order position', 'verbose_name_plural': 'Order positions'},
        ),
        migrations.AddField(
            model_name='item',
            name='max_per_order',
            field=models.IntegerField(blank=True, help_text='This product can only be bought at most this times within one order. If you keep the field empty or set it to 0, there is no special limit for this product. The limit for the maximum number of items in the whole order applies regardless.', null=True, verbose_name='Maximum times per order'),
        ),
        migrations.AlterField(
            model_name='item',
            name='allow_cancel',
            field=models.BooleanField(default=True, help_text='If this is active and the general event settings allo wit, orders containing this product can be canceled by the user until the order is paid for. Users cannot cancel paid orders on their own and you can cancel orders at all times, regardless of this setting', verbose_name='Allow product to be canceled'),
        ),
        migrations.AlterField(
            model_name='item',
            name='default_price',
            field=models.DecimalField(decimal_places=2, help_text='If this product has multiple variations, you can set different prices for each of the variations. If a variation does not have a special price or if you do not have variations, this price will be used.', max_digits=7, null=True, verbose_name='Default price'),
        ),
        migrations.RenameModel(
            old_name='EventSetting',
            new_name='Event_SettingsStore',
        ),
        migrations.RenameModel(
            old_name='OrganizerSetting',
            new_name='Organizer_SettingsStore',
        ),
        migrations.CreateModel(
            name='GlobalSettingsObject_SettingsStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=255)),
                ('value', models.TextField()),
            ],
        ),
        migrations.RunPython(
            code=migrate_global_settings,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
        migrations.DeleteModel(
            name='GlobalSetting',
        ),
        migrations.AlterField(
            model_name='event_settingsstore',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_settings_objects', to='pretixbase.Event'),
        ),
        migrations.AlterField(
            model_name='organizer_settingsstore',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_settings_objects', to='pretixbase.Organizer'),
        ),
        migrations.AddField(
            model_name='item',
            name='min_per_order',
            field=models.IntegerField(blank=True, help_text='This product can only be bought if it is added to the cart at least this many times. If you keep the field empty or set it to 0, there is no special limit for this product.', null=True, verbose_name='Minimum amount per order'),
        ),
        migrations.AlterField(
            model_name='event',
            name='currency',
            field=models.CharField(choices=[('AED', 'AED - UAE Dirham'), ('AFN', 'AFN - Afghani'), ('ALL', 'ALL - Lek'), ('AMD', 'AMD - Armenian Dram'), ('ANG', 'ANG - Netherlands Antillean Guilder'), ('AOA', 'AOA - Kwanza'), ('ARS', 'ARS - Argentine Peso'), ('AUD', 'AUD - Australian Dollar'), ('AWG', 'AWG - Aruban Florin'), ('AZN', 'AZN - Azerbaijanian Manat'), ('BAM', 'BAM - Convertible Mark'), ('BBD', 'BBD - Barbados Dollar'), ('BDT', 'BDT - Taka'), ('BGN', 'BGN - Bulgarian Lev'), ('BHD', 'BHD - Bahraini Dinar'), ('BIF', 'BIF - Burundi Franc'), ('BMD', 'BMD - Bermudian Dollar'), ('BND', 'BND - Brunei Dollar'), ('BOB', 'BOB - Boliviano'), ('BRL', 'BRL - Brazilian Real'), ('BSD', 'BSD - Bahamian Dollar'), ('BTN', 'BTN - Ngultrum'), ('BWP', 'BWP - Pula'), ('BYR', 'BYR - Belarusian Ruble'), ('BZD', 'BZD - Belize Dollar'), ('CAD', 'CAD - Canadian Dollar'), ('CDF', 'CDF - Congolese Franc'), ('CHF', 'CHF - Swiss Franc'), ('CLP', 'CLP - Chilean Peso'), ('CNY', 'CNY - Yuan Renminbi'), ('COP', 'COP - Colombian Peso'), ('CRC', 'CRC - Costa Rican Colon'), ('CUC', 'CUC - Peso Convertible'), ('CUP', 'CUP - Cuban Peso'), ('CVE', 'CVE - Cabo Verde Escudo'), ('CZK', 'CZK - Czech Koruna'), ('DJF', 'DJF - Djibouti Franc'), ('DKK', 'DKK - Danish Krone'), ('DOP', 'DOP - Dominican Peso'), ('DZD', 'DZD - Algerian Dinar'), ('EGP', 'EGP - Egyptian Pound'), ('ERN', 'ERN - Nakfa'), ('ETB', 'ETB - Ethiopian Birr'), ('EUR', 'EUR - Euro'), ('FJD', 'FJD - Fiji Dollar'), ('FKP', 'FKP - Falkland Islands Pound'), ('GBP', 'GBP - Pound Sterling'), ('GEL', 'GEL - Lari'), ('GHS', 'GHS - Ghana Cedi'), ('GIP', 'GIP - Gibraltar Pound'), ('GMD', 'GMD - Dalasi'), ('GNF', 'GNF - Guinea Franc'), ('GTQ', 'GTQ - Quetzal'), ('GYD', 'GYD - Guyana Dollar'), ('HKD', 'HKD - Hong Kong Dollar'), ('HNL', 'HNL - Lempira'), ('HRK', 'HRK - Kuna'), ('HTG', 'HTG - Gourde'), ('HUF', 'HUF - Forint'), ('IDR', 'IDR - Rupiah'), ('ILS', 'ILS - New Israeli Sheqel'), ('INR', 'INR - Indian Rupee'), ('IQD', 'IQD - Iraqi Dinar'), ('IRR', 'IRR - Iranian Rial'), ('ISK', 'ISK - Iceland Krona'), ('JMD', 'JMD - Jamaican Dollar'), ('JOD', 'JOD - Jordanian Dinar'), ('JPY', 'JPY - Yen'), ('KES', 'KES - Kenyan Shilling'), ('KGS', 'KGS - Som'), ('KHR', 'KHR - Riel'), ('KMF', 'KMF - Comoro Franc'), ('KPW', 'KPW - North Korean Won'), ('KRW', 'KRW - Won'), ('KWD', 'KWD - Kuwaiti Dinar'), ('KYD', 'KYD - Cayman Islands Dollar'), ('KZT', 'KZT - Tenge'), ('LAK', 'LAK - Kip'), ('LBP', 'LBP - Lebanese Pound'), ('LKR', 'LKR - Sri Lanka Rupee'), ('LRD', 'LRD - Liberian Dollar'), ('LSL', 'LSL - Loti'), ('LYD', 'LYD - Libyan Dinar'), ('MAD', 'MAD - Moroccan Dirham'), ('MDL', 'MDL - Moldovan Leu'), ('MGA', 'MGA - Malagasy Ariary'), ('MKD', 'MKD - Denar'), ('MMK', 'MMK - Kyat'), ('MNT', 'MNT - Tugrik'), ('MOP', 'MOP - Pataca'), ('MRO', 'MRO - Ouguiya'), ('MUR', 'MUR - Mauritius Rupee'), ('MVR', 'MVR - Rufiyaa'), ('MWK', 'MWK - Malawi Kwacha'), ('MXN', 'MXN - Mexican Peso'), ('MYR', 'MYR - Malaysian Ringgit'), ('MZN', 'MZN - Mozambique Metical'), ('NAD', 'NAD - Namibia Dollar'), ('NGN', 'NGN - Naira'), ('NIO', 'NIO - Cordoba Oro'), ('NOK', 'NOK - Norwegian Krone'), ('NPR', 'NPR - Nepalese Rupee'), ('NZD', 'NZD - New Zealand Dollar'), ('OMR', 'OMR - Rial Omani'), ('PAB', 'PAB - Balboa'), ('PEN', 'PEN - Sol'), ('PGK', 'PGK - Kina'), ('PHP', 'PHP - Philippine Peso'), ('PKR', 'PKR - Pakistan Rupee'), ('PLN', 'PLN - Zloty'), ('PYG', 'PYG - Guarani'), ('QAR', 'QAR - Qatari Rial'), ('RON', 'RON - Romanian Leu'), ('RSD', 'RSD - Serbian Dinar'), ('RUB', 'RUB - Russian Ruble'), ('RWF', 'RWF - Rwanda Franc'), ('SAR', 'SAR - Saudi Riyal'), ('SBD', 'SBD - Solomon Islands Dollar'), ('SCR', 'SCR - Seychelles Rupee'), ('SDG', 'SDG - Sudanese Pound'), ('SEK', 'SEK - Swedish Krona'), ('SGD', 'SGD - Singapore Dollar'), ('SHP', 'SHP - Saint Helena Pound'), ('SLL', 'SLL - Leone'), ('SOS', 'SOS - Somali Shilling'), ('SRD', 'SRD - Surinam Dollar'), ('SSP', 'SSP - South Sudanese Pound'), ('STD', 'STD - Dobra'), ('SVC', 'SVC - El Salvador Colon'), ('SYP', 'SYP - Syrian Pound'), ('SZL', 'SZL - Lilangeni'), ('THB', 'THB - Baht'), ('TJS', 'TJS - Somoni'), ('TMT', 'TMT - Turkmenistan New Manat'), ('TND', 'TND - Tunisian Dinar'), ('TOP', 'TOP - Pa’anga'), ('TRY', 'TRY - Turkish Lira'), ('TTD', 'TTD - Trinidad and Tobago Dollar'), ('TWD', 'TWD - New Taiwan Dollar'), ('TZS', 'TZS - Tanzanian Shilling'), ('UAH', 'UAH - Hryvnia'), ('UGX', 'UGX - Uganda Shilling'), ('USD', 'USD - US Dollar'), ('UYU', 'UYU - Peso Uruguayo'), ('UZS', 'UZS - Uzbekistan Sum'), ('VEF', 'VEF - Bolívar'), ('VND', 'VND - Dong'), ('VUV', 'VUV - Vatu'), ('WST', 'WST - Tala'), ('XAF', 'XAF - CFA Franc BEAC'), ('XAG', 'XAG - Silver'), ('XAU', 'XAU - Gold'), ('XBA', 'XBA - Bond Markets Unit European Composite Unit (EURCO)'), ('XBB', 'XBB - Bond Markets Unit European Monetary Unit (E.M.U.-6)'), ('XBC', 'XBC - Bond Markets Unit European Unit of Account 9 (E.U.A.-9)'), ('XBD', 'XBD - Bond Markets Unit European Unit of Account 17 (E.U.A.-17)'), ('XCD', 'XCD - East Caribbean Dollar'), ('XDR', 'XDR - SDR (Special Drawing Right)'), ('XOF', 'XOF - CFA Franc BCEAO'), ('XPD', 'XPD - Palladium'), ('XPF', 'XPF - CFP Franc'), ('XPT', 'XPT - Platinum'), ('XSU', 'XSU - Sucre'), ('XTS', 'XTS - Codes specifically reserved for testing purposes'), ('XUA', 'XUA - ADB Unit of Account'), ('XXX', 'XXX - The codes assigned for transactions where no currency is involved'), ('YER', 'YER - Yemeni Rial'), ('ZAR', 'ZAR - Rand'), ('ZMW', 'ZMW - Zambian Kwacha'), ('ZWL', 'ZWL - Zimbabwe Dollar')], default='EUR', max_length=10, verbose_name='Default currency'),
        ),
        migrations.AlterField(
            model_name='event_settingsstore',
            name='key',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='max_per_order',
            field=models.IntegerField(blank=True, help_text='This product can only be bought at most this many times within one order. If you keep the field empty or set it to 0, there is no special limit for this product. The limit for the maximum number of items in the whole order applies regardless.', null=True, verbose_name='Maximum amount per order'),
        ),
        migrations.AlterField(
            model_name='organizer_settingsstore',
            name='key',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AddField(
            model_name='cartposition',
            name='attendee_email',
            field=models.EmailField(blank=True, help_text='Empty, if this product is not an admission ticket', max_length=254, null=True, verbose_name='Attendee email'),
        ),
        migrations.AddField(
            model_name='orderposition',
            name='attendee_email',
            field=models.EmailField(blank=True, help_text='Empty, if this product is not an admission ticket', max_length=254, null=True, verbose_name='Attendee email'),
        ),
        migrations.AlterField(
            model_name='event_settingsstore',
            name='key',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='globalsettingsobject_settingsstore',
            name='key',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='organizer_settingsstore',
            name='key',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='ItemAddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_count', models.PositiveIntegerField(default=0, verbose_name='Minimum number')),
                ('max_count', models.PositiveIntegerField(default=1, verbose_name='Maximum number')),
            ],
        ),
        migrations.AddField(
            model_name='cartposition',
            name='addon_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addons', to='pretixbase.CartPosition'),
        ),
        migrations.AddField(
            model_name='itemcategory',
            name='is_addon',
            field=models.BooleanField(default=False, help_text='If selected, the products belonging to this category are not for sale on their own. They can only be bought in combination with a product that has this category configured as a possible source for add-ons.', verbose_name='Products in this category are add-on products'),
        ),
        migrations.AddField(
            model_name='orderposition',
            name='addon_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addons', to='pretixbase.OrderPosition'),
        ),
        migrations.AlterField(
            model_name='item',
            name='free_price',
            field=models.BooleanField(default=False, help_text='If this option is active, your users can choose the price themselves. The price configured above is then interpreted as the minimum price a user has to enter. You could use this e.g. to collect additional donations for your event. This is currently not supported for products that are bought as an add-on to other products.', verbose_name='Free price input'),
        ),
        migrations.AddField(
            model_name='itemaddon',
            name='addon_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addon_to', to='pretixbase.ItemCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='itemaddon',
            name='base_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addons', to='pretixbase.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='itemaddon',
            unique_together=set([('base_item', 'addon_category')]),
        ),
        migrations.AlterModelOptions(
            name='itemaddon',
            options={'ordering': ('position', 'pk')},
        ),
        migrations.AddField(
            model_name='itemaddon',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Position'),
        ),
        migrations.AddField(
            model_name='itemvariation',
            name='description',
            field=i18nfield.fields.I18nTextField(blank=True, help_text='This is shown below the variation name in lists.', null=True, verbose_name='Description'),
        ),
    ]