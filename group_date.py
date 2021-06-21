import requests
import json
from datetime import datetime


def get_request(pr_date):
    rurl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=%s' % (pr_date)
    r = requests.get(rurl)


    if r.status_code == 200:
        cowin_data = r.json()

        last7DaysRegistration = cowin_data.get('last7DaysRegistration')
        reg_data = last7DaysRegistration[-1]
        reg_res = dict(index="reg_data", data=reg_data)
        print(json.dumps(reg_res))

        last30DaysAefi = cowin_data.get('last30DaysAefi')
        aefi_data = last30DaysAefi[-1]
        aefi_res = dict(index="aefi_data", data=aefi_data)
        print(json.dumps(aefi_res))

        last5daySessionStatus = cowin_data.get('last5daySessionStatus')
        sess_data = last5daySessionStatus[-1]
        sess_res = dict(index="sess_data", data=sess_data)
        print(json.dumps(sess_res))


def main():
    date_list = ["2021-05-03","2021-05-04","2021-05-05","2021-05-06","2021-05-07","2021-05-08","2021-05-09","2021-05-10","2021-05-11","2021-05-12","2021-05-13","2021-05-14","2021-05-15","2021-05-16","2021-05-17","2021-05-18","2021-05-19","2021-05-20","2021-05-21","2021-05-22","2021-05-23","2021-05-24","2021-05-25","2021-05-26","2021-05-27","2021-05-28","2021-05-29","2021-05-30","2021-05-31","2021-06-01","2021-06-02","2021-06-03","2021-06-04","2021-06-05","2021-06-06","2021-06-07","2021-06-08","2021-06-09","2021-06-10","2021-06-11","2021-06-12"]
    for date in date_list:
        get_request(date)

main()