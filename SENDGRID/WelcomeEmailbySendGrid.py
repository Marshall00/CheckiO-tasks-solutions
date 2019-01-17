import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content #Imported elements from sendgrid

API_KEY = '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' #API key generated on the sendgrid website
SUBJECT = 'Welcome' #subject of sending mail
BODY = 'Hi {}' #body of sending mail

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):            #Function that contains all core info about mail, which will be sent
    from_email=Email("test@example.com")
    to_email=Email(email)
    subject=SUBJECT
    content=Content("text/plain", BODY.format(name))
    mail=Mail(from_email, subject, to_email, content)
    response=sg.client.mail.send.post(request_body=mail.get())