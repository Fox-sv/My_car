from django.db import models
from django.contrib.auth.models import User


class Date_oil(models.Model):
    date_oil = models.DateField(verbose_name='Date oil')
    km_oil = models.FloatField(verbose_name='Last Millage', null=True, blank=True)

    def __str__(self):
        return f'Last date change oil: {self.date_oil}'


class Date_insurance(models.Model):
    date_insurance = models.DateField(verbose_name='Date insurance')

    def __str__(self):
        return f'{self.date_insurance}'


class Date_inspection(models.Model):
    date_inspection = models.DateField(verbose_name='Date inspection')

    def __str__(self):
        return f'{self.date_inspection}'


class Expenses(models.Model):
    summa = models.FloatField()
    name = models.CharField(max_length=200)
    notes = models.TextField(max_length=100, verbose_name='Notes', blank=True)
    responsible_user_id = models.ForeignKey(User, verbose_name='Responsible', related_name='car_to_user', null=True,
                                            on_delete=models.SET_NULL)
    date_money = models.DateField(verbose_name='date_money')

    def __str__(self):
        return f'Оплата {self.summa} BYN. DATA {self.date_money}'


class About_my_car(models.Model):
    total_mileage = models.FloatField(verbose_name='Total Mileage')
    daily_mileage = models.FloatField(verbose_name='Daily Mileage')
    fuel = models.FloatField(verbose_name='Fuel')
    tire_pressure = models.FloatField(verbose_name='Tire Pressure')
    fuel_consumption = models.FloatField(verbose_name='Fuel Consumption')
    door_status = models.CharField(max_length=20)
    battery_voltage = models.FloatField(verbose_name='Battery Voltage')
    last_oil = models.ForeignKey(Date_oil, verbose_name='Last Oil', related_name='car_to_date', null=True,
                                            on_delete=models.SET_NULL)
    last_date_insurance = models.ForeignKey(Date_insurance, verbose_name='Last Date Insurance', related_name='date_to_insur', null=True,
                                            on_delete=models.SET_NULL)
    last_date_inspection = models.ForeignKey(Date_inspection, verbose_name='Last Date Inspection', related_name='date_to_insp', null=True,
                                            on_delete=models.SET_NULL)

    def __str__(self):
        return f'About My Car'
