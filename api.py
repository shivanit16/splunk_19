import requests
import json
import datetime

def get_request():
    rurl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=2021-06-15'
    r = requests.get(rurl)

    if r.status_code == 200:
        cowin_data = r.json()
        BeneficiariesGroupBy = cowin_data.get('getBeneficiariesGroupBy')
        data15 = BeneficiariesGroupBy[-1] 
        needed_data15 = BeneficiariesGroupBy[-1]
        del needed_data15['state_id']
        del needed_data15['id']
        del needed_data15['title']
        del needed_data15['today']
        del needed_data15['state_name']
        del needed_data15['total']

    surl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=2021-06-14'
    s = requests.get(surl)

    if s.status_code == 200:
        cowin_data = s.json()
        BeneficiariesGroupBy = cowin_data.get('getBeneficiariesGroupBy')
        data14 = BeneficiariesGroupBy[-1]
        needed_data14 = BeneficiariesGroupBy[-1]
        del needed_data14['state_id']
        del needed_data14['id']
        del needed_data14['title']
        del needed_data14['today']
        del needed_data14['state_name']
        del needed_data14['total']

    # Using dictionary comprehension + keys()
    # Subtraction of dictionaries
    res = {key: needed_data15[key] - needed_data14.get(key, 0) for key in needed_data15.keys()}
    res.update({'state_name': 'Daman and Diu'})
  
    final_result(res)

def final_result(diff):
    rurl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=2021-06-15'
    r = requests.get(rurl)

    if r.status_code == 200:
        cowin_data = r.json()
        BeneficiariesGroupBy = cowin_data.get('getBeneficiariesGroupBy')
        data15 = BeneficiariesGroupBy[-1] 
        data15.update(diff)
        del data15['state_id']
        del data15['id']
        del data15['title']
        del data15['today']
        final_data = data15
        print(final_data)

    
def main(): 
    get_request()

main()