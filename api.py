import requests
import json
import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')


def get_request(pr1,pr2):
    rurl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=%s' % (pr1)
    r = requests.get(rurl)

    if r.status_code == 200:
        cowin_data = r.json()
        BeneficiariesGroupBy = cowin_data.get('getBeneficiariesGroupBy')
        yesterday = BeneficiariesGroupBy[30] 
        print(yesterday)
        needed_data2 = BeneficiariesGroupBy[30]
        del needed_data2['state_id']
        del needed_data2['id']
        del needed_data2['title']
        del needed_data2['today']
        del needed_data2['state_name']
        del needed_data2['total']

    surl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=%s' % (pr2)
    s = requests.get(surl)

    if s.status_code == 200:
        cowin_data = s.json()
        BeneficiariesGroupBy = cowin_data.get('getBeneficiariesGroupBy')
        daybefore_yes = BeneficiariesGroupBy[30]
        print(daybefore_yes)
        needed_data1 = BeneficiariesGroupBy[30]
        del needed_data1['state_id']
        del needed_data1['id']
        del needed_data1['title']
        del needed_data1['today']
        del needed_data1['state_name']
        del needed_data1['total']

    # Using dictionary comprehension + keys()
    # Subtraction of dictionaries
    res = {key: needed_data2[key] - needed_data1.get(key, 0) for key in needed_data2.keys()}
  
    final_result(res,pr1)

def final_result(diff,pr):
    rurl = 'https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=&district_id=&date=%s' % (pr)
    r = requests.get(rurl)

    if r.status_code == 200:
        cowin_data = r.json()
        BeneficiariesGroupBy = cowin_data.get('getBeneficiariesGroupBy')
        data2 = BeneficiariesGroupBy[30] 
        data2.update(diff)
        del data2['state_id']
        del data2['id']
        del data2['title']
        del data2['today']
        final_data = data2
        print(final_data)

    
def main(): 
    Current_Date_Formatted = datetime.datetime.now(IST).strftime ('%Y-%m-%d') # format the date to ddmmyyyy
    print ('Current Date: ' + str(Current_Date_Formatted))
    
    Previous_Date1 = datetime.datetime.now(IST) - datetime.timedelta(days=1)
    Previous_Date_Formatted1 = Previous_Date1.strftime ('%Y-%m-%d') # format the date to ddmmyyyy
    print ('Previous Date1: ' + str(Previous_Date_Formatted1))

    Previous_Date2 = datetime.datetime.now(IST) - datetime.timedelta(days=2)
    Previous_Date_Formatted2 = Previous_Date2.strftime ('%Y-%m-%d') # format the date to ddmmyyyy
    print ('Previous Date2: ' + str(Previous_Date_Formatted2))



    get_request(Previous_Date_Formatted1,Previous_Date_Formatted2)


main()
