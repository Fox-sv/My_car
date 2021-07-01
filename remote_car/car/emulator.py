import json, os.path, datetime
from . import models


def mileage_score():
    now_time = datetime.datetime.now() + datetime.timedelta(hours=3)
    if not os.path.exists('about_car.json'):
        daily_mil = {'total_mileage': 0, 'today': 0, 'fuel': 23, 'fuel_consumption': 0, 'consumption': 0, 'last_fuel': 0}
        with open('about_car.json', "w") as write_file:
            json.dump(daily_mil, write_file)
    else:
        with open('about_car.json', "r") as f:
            daily_mil = json.loads(f.read())
        daily_mil['total_mileage'] += 0.01
        daily_mil['fuel'] -= 0.001
        if daily_mil['fuel'] < 3:
            daily_mil['fuel'] += 20
            daily_mil['consumption'] = daily_mil['total_mileage'] - daily_mil['last_fuel']
            daily_mil['last_fuel'] = daily_mil['total_mileage']
            daily_mil['fuel_consumption'] = 20 / daily_mil['consumption'] * 100
        if now_time.strftime('%H:%M') == datetime.time(0, 0).strftime('%H:%M'):
            daily_mil['today'] = daily_mil['total_mileage']
        with open('about_car.json', 'w+') as fs:
            json.dump(daily_mil, fs)

    if models.Date_oil.objects.all().last().km_oil is None:
        mileage = models.Date_oil.objects.all().last()
        with open('about_car.json', 'r') as f:
            file = json.loads(f.read())
        mileage.km_oil = round(file['total_mileage'], 2)
        mileage.save()

    return daily_mil


