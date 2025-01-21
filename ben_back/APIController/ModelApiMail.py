import smtplib
# Doc : https://mailtrap.io/fr/blog/python-send-email/
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ModelApiMail:

    # Constructeur
    def __init__(self, smtp_server, smtp_port, email_address, email_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_address = email_address
        self.email_password = email_password

            # Création de la fonction send_email qui sert a l'envoie de mail
    def send_email(self, to_email, subject, body):
        try:
            # Création de l'objet MIMEMultipart
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # Connexion au serveur SMTP
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.ehlo()
            server.starttls()
            server.login(self.email_address, self.email_password)

            # Envoi du message
            server.sendmail(self.email_address, to_email, msg.as_string())
            server.quit()  

            return f"E-mail envoyé avec succès à {to_email}."
        except smtplib.SMTPException as e:
            return f"Erreur SMTP : {str(e)}"
        except Exception as e:
            return f"Erreur générale : {str(e)}"
