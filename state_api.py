import requests
import json
import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')


def get_request(pr1,pr2, state_id):
    rurl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=%s' % (pr1)
    r = requests.get(rurl)

    if r.status_code == 200:
        cowin_data = r.json()
        BeneficiariesGroupBy = cowin_data.get('getBeneficiariesGroupBy')
        yesterday = BeneficiariesGroupBy[state_id] 

    surl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=%s' % (pr2)
    s = requests.get(surl)

    if s.status_code == 200:
        cowin_data = s.json()
        BeneficiariesGroupBy = cowin_data.get('getBeneficiariesGroupBy')
        daybefore_yes = BeneficiariesGroupBy[state_id]

    return yesterday, daybefore_yes

def compute_result(yesterday, dayBeforeYes):
    result = dict(
        state = yesterday['state_name'], 
        total_cum = yesterday['total'], 
        total = yesterday['total'] - dayBeforeYes['total'],
        partial_vaccninated= yesterday['partial_vaccinated'] - dayBeforeYes['partial_vaccinated'],
        total_vaccinated = yesterday['totally_vaccinated'] - dayBeforeYes['totally_vaccinated'] )
    return result

    
def main(): 
    Current_Date_Formatted = datetime.datetime.now(IST).strftime ('%Y-%m-%d') # format the date to ddmmyyyy
    
    Previous_Date1 = datetime.datetime.now(IST) - datetime.timedelta(days=1)
    Previous_Date_Formatted1 = Previous_Date1.strftime ('%Y-%m-%d') # format the date to ddmmyyyy

    Previous_Date2 = datetime.datetime.now(IST) - datetime.timedelta(days=2)
    Previous_Date_Formatted2 = Previous_Date2.strftime ('%Y-%m-%d') # format the date to ddmmyyyy


    for state_id in range(0,36):
        yesterday, dayBeforeYes = get_request(Previous_Date_Formatted1,Previous_Date_Formatted2, state_id)
        result = compute_result(yesterday, dayBeforeYes)
        print (result)


main()
