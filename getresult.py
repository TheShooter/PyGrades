import requests
#take parameters and pass it to local variables then process other steps ( connect to server and get new cookie )
#get the new cookie and make a request to GetResult and retrieve the data)
student_email = x
student_pass = password

url_login = "http://agr.p.alexu.edu.eg/Results/Student/Account/CheckLogin"
data_login = {
    "Email": student_email,
    "Password": student_pass,
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

response_login = requests.post(url_login, data=data_login, headers=headers_login)

login_cookie =  'ASP.NET_SessionId=' + response_login.cookies['ASP.NET_SessionId']


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

for every_subject in first_dig: #insert the data to the database in Students table
        esm_elmada = every_subject.get('SubjectName')
        rkm_subject = every_subject.get('SubjectID')
        data_id = every_subject.get('ID')
        dragrak = every_subject.get('DegreeSymbol')
        do_survey= every_subject.get('HasAnsweredSurvey')

        if rkm_subject == 7880:
            add_db = db.insert(Students).values(Extension=dragark, SubjectID1=rkm_subject, ID_one=data_id)
            conn = engine.connect()
            result = conn.execute(add_db)

        elif rkm_subject == 7881:
            add_db = db.insert(Students).values(Dairy=dragark, SubjectID2=rkm_subject, ID_two=data_id)
            conn = engine.connect()
            result = conn.execute(add_db)

        elif rkm_subject == 7882:
            add_db = db.insert(Students).values(Vegetables=dragark, SubjectID3=rkm_subject, ID_three=data_id)
            conn = engine.connect()
            result = conn.execute(add_db)

        elif rkm_subject == 313:
            add_db = db.insert(Students).values(Floriculture=dragark, SubjectID4=rkm_subject, ID_four=data_id)
            conn = engine.connect()
            result = conn.execute(add_db)

        elif rkm_subject == 7883:
            add_db = db.insert(Students).values(FoodScience=dragark, SubjectID5=rkm_subject, ID_five=data_id)
            conn = engine.connect()
            result = conn.execute(add_db)

        elif rkm_subject == 7884:
            add_db = db.insert(Students).values(Pomology=dragark, SubjectID6=rkm_subject, ID_six=data_id)
            conn = engine.connect()
            result = conn.execute(add_db)

        elif rkm_subject == 7885:
            add_db = db.insert(Students).values(Computer=dragark, SubjectID7=rkm_subject, ID_seven=data_id,)
            conn = engine.connect()
            result = conn.execute(add_db)


