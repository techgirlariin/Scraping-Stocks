import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


from_add='aradhanapradhan27@gmail.com'

to_add='aradhanapradhan55@gmail.com'

subject = "Finance BY Aradhana"

def send(filename):
    #header
    msg= MIMEMultipart()
    msg['From']=from_add
    msg['To']=to_add
    msg['Subject']= subject

    #body
    body="<i>Stock REport</i>"
    msg.attach(MIMEText(body,'html'))
    my_file=open("filename","rb")

    part= MIMEBase('application','octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment;filename=' + 'filename')
    msg.attach(part)



    message=msg.as_string()


    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('aradhanapradhan27@gmail.com','zpvrplezkomwsxkb')

    server.sendmail(from_add,to_add,message)

    server.quit()
    
    