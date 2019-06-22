url = "http://agr.p.alexu.edu.eg/Results/Student/Account/CheckLogin"
data = {
    "Email": "abdelrhman.hosany017@alexu.edu.eg",
    "Password": "Puk20664",
    "X-Requested-With": "XMLHttpRequest"
}
headers = {
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

resp = requests.post(url, data=data, headers=headers)