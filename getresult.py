import requests
import json
student_email = x
student_pass = password

url_login = "http://agr.p.alexu.edu.eg/Results/Student/Account/CheckLogin"
data_login = {
    "Email": "abdelrhman.hosany017@alexu.edu.eg",
    "Password": "Puk20664",
    "X-Requested-With": "XMLHttpRequest"
}
headers_login = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "91",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "agr.p.alexu.edu.eg",
    "Origin": "http://agr.p.alexu.edu.eg",
    "Referer": "http://agr.p.alexu.edu.eg/Results/Student/Account",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

r_login = requests.post(url_login, data=data_login, headers=headers_login)

login_cookie =  'ASP.NET_SessionId=' + r_login.cookies['ASP.NET_SessionId']


url = "http://agr.p.alexu.edu.eg/Results/Student/Result/GetResults"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": login_cookie,
    "Host": "agr.p.alexu.edu.eg",
    "Referer": "http://agr.p.alexu.edu.eg/Results/Student/Result/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
}

resp = requests.get(url, headers=headers)

fetch_data = resp.json()

first_dig = fetch_data.get('data')

for every_subject in first_dig:
	esm_elmada = every_subject.get('SubjectName')
	rkm_subject = every_subject.get('SubjectID')
	data_id = every_subject.get('ID')
	dragrak = every_subject.get('DegreeSymbol')
	do_survey= every_subject.get('HasAnsweredSurvey')
	add_db = students.insert().values(SubjectName=esm_elmada, SubjectID=rkm_subject, ID=data_id, DegreeSymbol=dragark, HasAnsweredSurvey=do_survey)
	# that's for one subject what about 7?????
	conn = engine.connect()
	result = conn.execute(add_db)