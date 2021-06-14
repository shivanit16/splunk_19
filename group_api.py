import requests
import json
import datetime

def get_request(pr_date):
    rurl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=%s' % (pr_date)
    r = requests.get(rurl)


    if r.status_code == 200:
        cowin_data = r.json()

        last7DaysRegistration = cowin_data.get('last7DaysRegistration')
        print("final member of last7DaysRegistration")
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
    present_date = datetime.date.today()
    get_request(present_date)

main()