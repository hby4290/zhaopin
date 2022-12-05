# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class M1(models.Model):
    num = models.AutoField(primary_key=True)
    act_date = models.CharField(max_length=20, blank=True, null=True)
    pin = models.CharField(max_length=20, blank=True, null=True)
    act_label = models.IntegerField(blank=True, null=True)
    tried = models.IntegerField(blank=True, null=True)
    is_1st = models.IntegerField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    sku_no = models.IntegerField(blank=True, null=True)
    stage = models.IntegerField(blank=True, null=True)
    open_date = models.CharField(max_length=225, blank=True, null=True)
    begin_date = models.CharField(max_length=225, blank=True, null=True)
    end_real_date = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'M1'


class M2(models.Model):
    num = models.AutoField(primary_key=True)
    date = models.CharField(db_column='Date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pin = models.CharField(max_length=20, blank=True, null=True)
    stage_label = models.IntegerField(blank=True, null=True)
    act_date = models.CharField(max_length=20, blank=True, null=True)
    max_end_date = models.CharField(max_length=20, blank=True, null=True)
    max_end_to_now_day = models.IntegerField(blank=True, null=True)
    tried = models.IntegerField(blank=True, null=True)
    is_1st = models.IntegerField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    stage = models.IntegerField(blank=True, null=True)
    open_date = models.CharField(max_length=225, blank=True, null=True)
    begin_date = models.CharField(max_length=225, blank=True, null=True)
    end_real_date = models.CharField(max_length=225, blank=True, null=True)
    v_end_date = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'M2'


class M3(models.Model):
    num = models.AutoField(primary_key=True)
    date = models.CharField(max_length=20, blank=True, null=True)
    forming_cnt = models.CharField(max_length=255, blank=True, null=True)
    add_1st_form_cnt = models.CharField(max_length=255, blank=True, null=True)
    renew_form_cnt = models.CharField(max_length=225, blank=True, null=True)
    end_form_cnt = models.CharField(max_length=225, blank=True, null=True)
    end_loss_form_cnt = models.CharField(max_length=225, blank=True, null=True)
    loss_renew_form_cnt = models.CharField(db_column='Loss_renew_form_cnt', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'M3'


class PlusUser(models.Model):
    id = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    edu = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=225, blank=True, null=True)
    ave_mon_con = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plus_user'
