#! /usr/bin/python3
from flask import Flask, request
from pymessenger.bot import Bot
import random
import sqlalchemy as db

app = Flask('pygrades')
ACCESS_TOKEN = 'EAAEYCy6sKrIBABaAncav5iTTIBfngP9NF4gHTlXyKdSZCKNZAkrF6ZBmtAuWyLe5hKoTXjcOCJT3MOBtTka22Hw289cp9zGQ9VVs1Qart074bCIa74mXTOutZCF5zMDHCUMjHdJhxLme981fZACiQEtLnHVC9qc0uZCOZCklwYe0QZDZD'
VERIFY_TOKEN = 'REHAMNOUR'
bot = Bot(ACCESS_TOKEN)

engine = db.create_engine('postgresql://postgres:HM50i5kPaX@127.0.0.1/pygrades')
connection = engine.connect()

###app.config['SQLALCHEMY_DATABSE_URL'] = 'postgresql://postgres:HM50i5kPaX@127.0.0.1/pygrades'
###db = SQLAlchemy(app)


@app.route('/api', methods=['GET', 'POST'])
def retreive_data():

	if request.method == 'GET':

		token_sent = request.args.get("hub.verify_token")
		return verify_fb_token(token_sent)
"""	else:
		output = request.get_json()
		for event in output['entry']:
			messaging = event['messaging']
			for mess in messaging:
				if mess.get('message'):
					sender_id_fb = mess['sender']['id']
					if mess['message'].get('text'):
						response_sent_text = get_message()
						send_message(sender_id_fb, response_sent_text)
					elif mess['message'].get('attachments'):
						response_sent_nontext = get_message()
						send_message(sender_id_fb, response_sent_nontext)
	return "Message Sent" """
  else:
       output = request.get_json()
        for event in output['entry']:
          messaging = event['messaging']
            for mess in messaging: #access to each element in the list
                if mess.get('message'): #each element is a dict, so if 'message' key exist, do
                    sender_id_fb = mess['sender']['id'] #access to 'id' key in 'sender' key
                     print(sender_id_fb)
                    if mess['message'].get('text'):
                      regex = '^([\w\.\-])+\@((alexu)+\.)+((edu)+\.)+(eg)+$'
                      regex_pass = '([A-Z]){1}([a-z]){2}([0-9]{4})'
                      temp_storage = mess['message']['text']
                     if re.match(regex, temp_storage):
                        email_storage = mess['message']['text']
                        print(email_storage)
                      elif re.match(regex_pass, temp_storage):
                        pass_storage = mess['message']['text']
                        print(pass_storage)
                      response_sent_text = get_message()
                      send_message(sender_id_fb, response_sent_text)
                   elif mess['message']['attachments']:
                     response_sent_nontext = get_message()
                     send_message(sender_id_fb, response_sent_nontext)
                    return "Message Sent"

def verify_fb_token(token_sent):

	if token_sent == VERIFY_TOKEN:
		return request.args.get("hub.challenge")
	return 'Ivalid verification token or Wrong Request Method'

def send_message(recipient_id, response):

	bot.send_text_message(recipient_id, response)
	return "success" 

def get_message():

	sample_responses =  ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    
	return random.choice(sample_responses)
    
def create_tables():
    metadata = db.MetaData
    db.Table('Students', metadata,
    db.Column('id', db.INT, db.Sequence('stud_id'), primary_key=True),
    db.Column('Sender_id', db.INT, primary_key=True),
    db.Column('Email', db.String(64),
    db.Column('Password', db.String(50),
    db.Column('Session_ID', db.INT),
    db.Column('SubjectID', db.INT),
    db.Column('JSON_ID', db.INT),
    db.Column('Subject_Name', db.String(convert_unicode=True),
    db.Column('DegreeSymbol', db.String(5),
    db.Column('Last_update', db.DATETIME)
    )
    metadata.create_all(engine)
    return "Table Created"

def add_student(id_student, Email_student, Password_student, SubjectID_student, Subject_Name_student, JSON_ID_student, DegreeSymbol_student, Session_ID_student):
   
    insert_student = db.insert(Students).values(id=id_student,
    Email=Email_student,
    Password=Password_student,
    SubjectID=SubjectID_student,
    JSON_ID=JSON_ID_student,
    Session_ID=Session_ID_student,
    DegreeSymbol=DegreeSymbol_student,
    Subject_Name=Subject_Name_student 
  )
    execute_insert = connection.execute()
    return "New student inserted!"



if __name__ == '__main__':
	app.run()