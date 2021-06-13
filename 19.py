import requests
import json
import datetime

def get_request(pr_date):
    rurl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=%s' % (pr_date)
    r = requests.get(rurl)


    if r.status_code == 200:
        cowin_data = r.json()
        vaccinationDoneByTime = cowin_data.get('vaccinationDoneByTime')
        print("vaccinationDoneByTime")
        print(vaccinationDoneByTime[-1])

        last7DaysRegistration = cowin_data.get('last7DaysRegistration')
        print("final member of last7DaysRegistration")
        print(last7DaysRegistration[-1])

        last30DaysAefi = cowin_data.get('last30DaysAefi')
        print("final member of last30DaysAefi")
        print(last30DaysAefi[-1])

        last5daySessionStatus = cowin_data.get('last5daySessionStatus')
        print("final member of last5daySessionStatus")
        print(last5daySessionStatus[-1])



def main(): 
    present_date = datetime.date.today()
    print(present_date)
    get_request(present_date)

main()
