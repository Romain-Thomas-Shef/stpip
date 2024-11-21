'''
---stpip---
This file contains the code that go scrap the website

@R. Thomas
@Santiago, Chile / Sheffield, UK
@2019--2024
'''


##standard library
from datetime import datetime
import requests

def scrap(package, apikey):
    '''
    This function go scrap pepy.tech

    Parameters
    -----------
    package
            str, name of the pypi package
    apikey
            str, apikey from pepy tech

    Returns
    -------
    total
            int, total number of downloads, all time
    last_month
            int, number of downloads in last month
    last_week
            int, number of downloads in the last week
    last_date
            str, date of the last day the stat was computed
    last_date_down, 
            int, number of downloads during last_date day
    '''

    url = 'https://api.pepy.tech/api/v2/projects/' + package
    headers = {'X-API-Key': apikey}
    response = requests.get(url, headers=headers)
    data = response.json()
    ###In case the repo was not found
    if 'message' in data.keys():
        total = 0
        last_month = 0
        last_week = 0
        last_day = 0
        date = '0 0 0'


    else:
        total = data['total_downloads']
        today = datetime.today()
        last_week = 0
        last_month = 0
        last_day = 0
        for date in (data['downloads']):
            dateformat = datetime.strptime(date, '%Y-%m-%d')
            date_difference = today - dateformat
            if date_difference.days <= 30:
                for n in data['downloads'][date]:
                    last_month += data['downloads'][date][n]
            if date_difference.days <= 7:
                for n in data['downloads'][date]:
                    last_week += data['downloads'][date][n]
            if date_difference.days <= 1:
                for n in data['downloads'][date]:
                    last_day += data['downloads'][date][n]

    return total, last_month, last_week, last_day, date



