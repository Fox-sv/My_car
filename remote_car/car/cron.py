from .models import Date_inspection, Date_oil, Date_insurance, About_my_car
from django.core.mail import send_mail
import datetime, telebot


api_token = '1489652904:AAEmYk2ztLnXX59vGKqLzmgROo44BNdxnlY'
bot = telebot.TeleBot(api_token)
chatId = 539951695


def share_date_oil():
    date_format = "%Y-%m-%d"
    change_km = round(About_my_car.objects.all().last().total_mileage - Date_oil.objects.all().last().km_oil, 2)
    date_oil = Date_oil.objects.all().last().date_oil
    datetime_object = datetime.datetime.strptime(str(date_oil), date_format)
    if datetime.datetime.today().year % 4 == 0:
        days = 366
    else:
        days = 365
    date_oil_change = datetime_object + datetime.timedelta(days=days)
    if datetime.datetime.today() >= date_oil_change or change_km > 9000:
        message = f'Необходимо заменить масло. После последней замены мала вы проехали {change_km} км'
        send_mail('Замена масла!', message, 'queryfordjango@gmail.com', ['Liahovkost@gmail.com'], fail_silently=False)
        bot.send_message(chatId, text=message)


def share_date_inspection():
    date_format = "%Y-%m-%d"
    inspection = Date_inspection.objects.all().last()
    datetime_object = datetime.datetime.strptime(str(inspection), date_format)
    if datetime.datetime.today().year % 4 == 0:
        days = 366
    else:
        days = 365
    date_inspection_change = datetime_object + datetime.timedelta(days=days-30)
    if datetime.datetime.today() >= date_inspection_change:
        new_date_inspection = date_inspection_change + datetime.timedelta(days=30)
        delta_date_inspection = new_date_inspection.date() - datetime.datetime.today().date()
        message = f'Необходимо пройти ТЕХОСМОТР в течении {delta_date_inspection.days} дней. Срок окончания техосмотра: {new_date_inspection.date()}'
        send_mail('Пройти ТЕХОСМОТР!', message, 'queryfordjango@gmail.com', ['Liahovkost@gmail.com'], fail_silently=False)
        bot.send_message(chatId, text=message)


def share_date_insurance():
    date_format = "%Y-%m-%d"
    insurance = Date_insurance.objects.all().last()
    datetime_object = datetime.datetime.strptime(str(insurance), date_format)
    if datetime.datetime.today().year % 4 == 0:
        days = 366
    else:
        days = 365
    date_insurance_change = datetime_object + datetime.timedelta(days=days-30)
    if datetime.datetime.today() >= date_insurance_change:
        new_date_insurance = date_insurance_change + datetime.timedelta(days=30)
        delta_date_insurance = new_date_insurance.date() - datetime.datetime.today().date()
        message = f'Необходимо продлить СТРАХОВКУ в течении {delta_date_insurance.days} дней. Срок окончания страховки: {new_date_insurance.date()}'
        send_mail('Продлить СТРАХОВКУ!', message, 'queryfordjango@gmail.com', ['Liahovkost@gmail.com'], fail_silently=False)
        bot.send_message(chatId, text=message)
