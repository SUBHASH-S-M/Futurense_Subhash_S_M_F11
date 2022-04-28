import smtplib, ssl
import maskpass
def Mail_sending(file_name,encrypt_password,user_receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "18bcs6052@gmail.com"  # Enter your address
    receiver_email = "vt8566@gmail.com"  # Enter receiver address
    #pass=Madara@1
    password = maskpass.askpass(prompt="Password:", mask="#")
    message = "Hi there Your file {} have been encrypted with password {}".format(file_name,encrypt_password)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, user_receiver_email, message)