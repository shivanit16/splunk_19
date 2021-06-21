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

def compute_result(yesterday, dayBeforeYes, _date):
    result = dict(
        date = str(_date),
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

    date_list = ["2021-03-08","2021-03-09","2021-03-10","2021-03-11","2021-03-12","2021-03-13","2021-03-14","2021-03-15","2021-03-16","2021-03-17","2021-03-18","2021-03-19","2021-03-20","2021-03-21","2021-03-22","2021-03-23","2021-03-24","2021-03-25","2021-03-26","2021-03-27","2021-03-28","2021-03-29","2021-03-30","2021-03-31","2021-04-01","2021-04-02","2021-04-03","2021-04-04","2021-04-05","2021-04-06","2021-04-07","2021-04-08","2021-04-09","2021-04-10","2021-04-11","2021-04-12","2021-04-13","2021-04-14","2021-04-15","2021-04-16","2021-04-17","2021-04-18","2021-04-19","2021-04-20","2021-04-21","2021-04-22","2021-04-23","2021-04-24","2021-04-25","2021-04-26","2021-04-27","2021-04-28","2021-04-29","2021-04-30","2021-05-01","2021-05-02","2021-05-03","2021-05-04","2021-05-05","2021-05-06","2021-05-07","2021-05-08","2021-05-09","2021-05-10","2021-05-11","2021-05-12","2021-05-13","2021-05-14","2021-05-15","2021-05-16","2021-05-17","2021-05-18","2021-05-19","2021-05-20","2021-05-21","2021-05-22","2021-05-23","2021-05-24","2021-05-25","2021-05-26","2021-05-27","2021-05-28","2021-05-29","2021-05-30","2021-05-31","2021-06-01","2021-06-02","2021-06-03","2021-06-04","2021-06-05","2021-06-06","2021-06-07","2021-06-08","2021-06-09","2021-06-10","2021-06-11","2021-06-12","2021-06-13","2021-06-14","2021-06-15","2021-06-16","2021-06-17","2021-06-18" ] 
    
    for i in range(1,len(date_list)+1):
        for state_id in range(0,36):
            yesterday, dayBeforeYes = get_request(date_list[i],date_list[i-1], state_id)
            result = json.dumps(compute_result(yesterday, dayBeforeYes, date_list[i]))
            print (result)

main()
