import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import ssl
import csv
from datetime import datetime
import time
from pathlib import Path

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "mariosfish1@gmail.com"
# receiver_email = "dacir72856@mailer2.net"
password = input("Type your password and press enter: ")
subject = "last test"
body = "This is an email with attachment sent from Python for testing"
file_attachment = 'test.pdf'
contacts = 'contacts.csv'


def sendMail(sender_email, receiver_email, smtp_server, port, password, subject, body, file_attachment):

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # filename = os.path.join('mail','test.pdf')  # In same directory as script
    filename = Path("mail/") / file_attachment

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename.name}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


# Main loop
with open(Path("mail/")/contacts) as file:
    reader = csv.reader(file)  # for txt: file.readline()
    # next(reader)  # Skip header row if csv with header line
    for email in reader:
        sendMail(sender_email, email[0].strip(), smtp_server,
                 port, password, subject, body, file_attachment)
        #  write to a log file
        f = open(Path("mail/logfile.txt"), "a")
        f.write(
            f"Το email εστάλη στην διεύθυνση {email[0].strip()} την {datetime.now()}\n")
        f.close()
        print(
            f"Το email εστάλη στην διεύθυνση {email[0].strip()} την {datetime.now()}")
        time.sleep(1)
