from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from . import models, forms
from django.db.models import Sum
import datetime, json, random
from .emulator import mileage_score


@login_required(login_url='login')
def start_page(request):
    if datetime.datetime.now().year % 4 == 0:
        days = 366
    else:
        days = 365
    date_format = "%Y-%m-%d"
    time_insurance_ = models.Date_insurance.objects.all().last()
    time_inspection_ = models.Date_inspection.objects.all().last()
    if time_inspection_ is None and time_insurance_ is None:
        insurance_change = ''
        inspection_change = ''
    else:
        datetime_object_insur = datetime.datetime.strptime(str(time_insurance_), date_format)
        datetime_object_insp = datetime.datetime.strptime(str(time_inspection_), date_format)
        insurance_change = (datetime_object_insur + datetime.timedelta(days=days)).strftime(date_format)
        inspection_change = (datetime_object_insp + datetime.timedelta(days=days)).strftime(date_format)
    return render(request, 'car/start_page.html',
                  {'time_insurance': inspection_change, 'time_inspection': insurance_change})


@login_required(login_url='login')
def add_date_oil(request):
    if request.method == 'POST':
        form_oil = forms.DateOilForm(request.POST)
        if form_oil.is_valid():
            new_oil = form_oil.save(commit=False)
            new_oil.responsible_user_id = request.user
            new_oil.save()
            return redirect('car:about_car')
        else:
            return render(request, 'car/add_date_oil.html', {'form_oil': form_oil})
    else:
        form_oil = forms.DateOilForm()
        return render(request, 'car/add_date_oil.html', {'form_oil': form_oil})


@login_required(login_url='login')
def add_date_inspection(request):
    if request.method == 'POST':
        form_inspection = forms.DateInspectionForm(request.POST)
        if form_inspection.is_valid():
            new_inspection = form_inspection.save(commit=False)
            new_inspection.responsible_user_id = request.user
            new_inspection.save()
            return redirect('car:about_car')
        else:
            return render(request, 'car/add_date_inspection.html', {'form_inspection': form_inspection})
    else:
        form_inspection = forms.DateInspectionForm()
        return render(request, 'car/add_date_inspection.html', {'form_inspection': form_inspection})


@login_required(login_url='login')
def add_date_insurance(request):
    if request.method == 'POST':
        form_insurance = forms.DateInsuranceForm(request.POST)
        if form_insurance.is_valid():
            new_insurance = form_insurance.save(commit=False)
            new_insurance.responsible_user_id = request.user
            new_insurance.save()
            return redirect('car:about_car')
        else:
            return render(request, 'car/add_date_insurance.html', {'form_insurance': form_insurance})
    else:
        form_insurance = forms.DateInsuranceForm()
        return render(request, 'car/add_date_insurance.html', {'form_insurance': form_insurance})


@login_required(login_url='login')
def all_date_oil(request):
    oil = models.Date_oil.objects.all()
    return render(request, 'car/all_date_oil.html', {'oil': oil})


@login_required(login_url='login')
def all_date_inspection(request):
    inspection = models.Date_inspection.objects.all()
    return render(request, 'car/all_date_inspection.html', {'inspection': inspection, })


@login_required(login_url='login')
def all_date_insurance(request):
    insurance = models.Date_insurance.objects.all()
    return render(request, 'car/all_date_insurance.html', {'insurance': insurance})


@login_required(login_url='login')
def delete_date_oil(request, oil_id: int):
    expenses = models.Date_oil.objects.get(id=oil_id)
    expenses.delete()
    return redirect('car:all_date_oil')


@login_required(login_url='login')
def update_date_oil(request, oil_id):
    entry = models.Date_oil.objects.get(id=oil_id)
    form_oil = forms.DateOilForm(request.POST or None, instance=entry)
    if form_oil.is_valid():
        form_oil.save()
        return redirect('car:all_date_oil')
    return render(request, 'car/add_date_oil.html', {'form_oil': form_oil, 'entry': entry})


@login_required(login_url='login')
def delete_date_inspection(request, inspection_id: int):
    expenses = models.Date_inspection.objects.get(id=inspection_id)
    expenses.delete()
    return redirect('car:all_date_inspection')


@login_required(login_url='login')
def update_date_inspection(request, inspection_id):
    entry = models.Date_inspection.objects.get(id=inspection_id)
    form_inspection = forms.DateInspectionForm(request.POST or None, instance=entry)
    if form_inspection.is_valid():
        form_inspection.save()
        return redirect('car:all_date_inspection')
    return render(request, 'car/add_date_inspection.html', {'form_inspection': form_inspection, 'entry': entry})


@login_required(login_url='login')
def delete_date_insurance(request, insurance_id: int):
    expenses = models.Date_insurance.objects.get(id=insurance_id)
    expenses.delete()
    return redirect('car:all_date_insurance')


@login_required(login_url='login')
def update_date_insurance(request, insurance_id: int):
    entry = models.Date_insurance.objects.get(id=insurance_id)
    form_insurance = forms.DateInsuranceForm(request.POST or None, instance=entry)
    if form_insurance.is_valid():
        form_insurance.save()
        return redirect('car:all_date_insurance')
    return render(request, 'car/add_date_insurance.html', {'form_insurance': form_insurance, 'entry': entry})


@login_required(login_url='login')
def expenses_car(request):
    expenses = models.Expenses.objects.all()
    total = expenses.aggregate(Sum('summa'))
    if request.method == 'POST':
        form = forms.NewExpensesForm(request.POST)
        if form.is_valid():
            new_expenses = form.save(commit=False)
            new_expenses.responsible_user_id = request.user
            new_expenses.save()
            return redirect('car:expenses_car')
        else:
            return render(request, 'car/expenses.html', {'form': form, 'expenses': expenses, 'total': total['summa__sum']})
    else:
        form = forms.NewExpensesForm()
        return render(request, 'car/expenses.html', {'form': form, 'expenses': expenses, 'total': total['summa__sum']})


@login_required(login_url='login')
def expenses_details(request, expenses_id: int):
    expenses = models.Expenses.objects.get(id=expenses_id)
    if not expenses:
        raise Exception('No such expenses!')
    return render(request, 'car/full_expenses.html', {'expenses': expenses, })


@login_required(login_url='login')
def delete_expenses(request, expenses_id: int):
    expenses = models.Expenses.objects.get(id=expenses_id)
    expenses.delete()
    entries = models.Expenses.objects.all()
    return redirect('car:expenses_car')


@login_required(login_url='login')
def update_expenses(request, expenses_id):
    entry = models.Expenses.objects.get(id=expenses_id)
    form = forms.NewExpensesForm(request.POST or None, instance=entry)
    flag = True
    if form.is_valid():
        form.save()
        return redirect('car:expenses_car')
    return render(request, 'car/expenses.html', {'form_update': form, 'entry': entry, 'flag': flag})


@login_required(login_url='login')
def about_car(request):
    if models.Date_oil.objects.all().last() is not None:
        date_oil = models.Date_oil.objects.all().last().date_oil
        km_oil = models.Date_oil.objects.all().last().km_oil
        date_insurance = models.Date_insurance.objects.all().last()
        date_inspection = models.Date_inspection.objects.all().last()
        car = models.About_my_car.objects.all().last()
        car.tire_pressure = 2
        car.total_mileage = round(mileage_score()['total_mileage'], 2)
        car.daily_mileage = round(mileage_score()['total_mileage'] - mileage_score()['today'], 2)
        car.fuel = round(mileage_score()['fuel'], 2)
        car.fuel_consumption = round(mileage_score()['fuel_consumption'], 2)
        car.battery_voltage = 12
        car.last_oil = models.Date_oil.objects.all().last()
        car.last_date_insurance = date_insurance
        car.last_date_inspection = date_inspection
        if random.randint(0, 1) == 0:
            door_sent = True
            car.door_status = 'Open'
        else:
            door_sent = False
            car.door_status = 'Close'
        car.save()
        data = {'car': car, 'date_oil': date_oil, 'km_oil': km_oil, 'date_insurance': date_insurance,
                'date_inspection': date_inspection, 'door_sent': door_sent}
    else:
        if models.About_my_car.objects.all().last() is None:
            car = models.About_my_car(total_mileage=0, daily_mileage=0, fuel=0, tire_pressure=0, fuel_consumption=0, battery_voltage=0)
            car.save()
        data = {}
    return render(request, 'car/about_car.html', data)


def contact_us(request):
    sent = False
    if request.method == 'POST':
        form = forms.ShareContactForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            subject = f"{clean_data['name']}"
            body = "Message: \n {message}".format(
                message=clean_data['message'],
            )
            send_mail(subject, body, 'queryfordjango@gmail.com', ['Liahovkost@gmail.com'])
            sent = True
            return render(request, 'car/share_contact.html', {'sent': sent})
    else:
        form = forms.ShareContactForm()
        return render(request, 'car/share_contact.html', {'form': form, 'sent': sent})
