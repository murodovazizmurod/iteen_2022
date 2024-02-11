import logging
import calendar
import datetime
from backend import app
from backend.db import Device, db
from flask import render_template, request, redirect


@app.route('/')
def index():
    # Get data from database
    logging.info('User opened main page')
    a = db['devices']
    return render_template('main.html', data=a)


def get_kz():
    # you can get Tenge amount from internet
    #       return float(requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/kzt.json').json()['kzt'])
    # for example static data
    return 510.167607


@app.route('/result', methods=['GET', 'POST'])
def result():
    # If POST method
    if request.method == "POST":
        # Form data
        a = request.form
        results = []
        for i in list(a):
            # if data from devices names
            if i.startswith('exam_m'):
                item = db.get(Device, id=request.form[i])
                # Tenge to dollar
                rasxod = item.cost / get_kz()
                doxod = item.income
                result = doxod - rasxod
                now = datetime.datetime.now()
                count = calendar.monthrange(now.year, now.month)[1]
                data = {
                    # 'time': [rasxod, doxod, result]
                    'hour': [rasxod, doxod, result],
                    'day': [rasxod*24, doxod*24, result*24],
                    'month': [rasxod*24*count, doxod*24*count, result*24*count],
                    'year': [rasxod*24*365, doxod*24*365, result*24*365]
                }
                results.append(data)
        counts = []
        # devices count
        for i in list(a):
            if i.startswith('exam_c'):
                try:
                    counts.append(int(request.form[i]))
                except Exception:
                    counts.append(1)
        for i, (c, e) in enumerate(zip(counts, results)):
            for k in e.keys():
                for index, num in enumerate(results[i][k]):
                    # multiply cost to count
                    results[i][k][index] = num * c
        logging.info('User entered data')
        return render_template('result.html', data=results)
    logging.warning('Method not allowed')
    return redirect('/')
