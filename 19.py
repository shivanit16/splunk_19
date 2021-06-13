import requests
import json
import datetime

def get_request(pr_date):
    rurl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=%s' % (pr_date)
    r = requests.get(rurl)
    if r.status_code == 200:
        d = r.json()
        print(d)

def main(): 
    present_date = datetime.date.today()
    print(present_date)
    get_request(present_date)

main()