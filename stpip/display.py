'''
---stpip---
This file contains the code that display the results

@R. Thomas
@Santiago, Chile
@2019
'''
def full(total, month, week, yest, yest_date, package):
    '''
    Display all the download informations

    Parameters
    ----------
    total
            int, total number of downloads, all time
    month
            int, number of downloads in last month
    day
            int, number of downloads in the last week
    pacakge
            int, name of the package

    '''
    if yest_date == '0 0 0':
        url = f'No package found on pepy.tech with name {package}'

    else:
        url = 'visit https://pepy.tech/project/' + package
    print('\033[1m\n###############################################\033[0m')
    print(f'\033[1m      Download counts for {package} \033[0m')
    print('\033[1m Total all time:' + f'\033[94m {total}\033[0m')
    print('\033[1m Total last 7 days:' + f'\033[94m {week}\033[0m')
    print('\033[1m Total last 30 days:' + f'\033[94m {month}\033[0m')
    print(f'\033[1m last day {yest_date}:' + f'\033[94m {yest}\033[0m')
    print(f'\033[1m--> {url} \033[0;0m')
    print('\033[1m\033[91m##############################################\n\033[0m')
