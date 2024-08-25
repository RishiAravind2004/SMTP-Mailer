"""

        Simple Code snippet for SMPT (Simple Mail Transfer Protocol) form sending gmails using Python!

        Note: Make sure your are using an valid gmail!

        Install teh packages by executing following command on command prompt

        Command: pip install smtplib

- CopyCat Developerz(Rishi Aravind)
"""


# Modules
import smtplib
from email.message import EmailMessage

# Replace these with your actual email and app-specific password
Sender_Email = "your_email@gmail.com"
App_password = "your_app_password"

def Send_Mail(Recipient_Emails, Subject, Content):
    # Create a new EmailMessage object
    msg = EmailMessage()

    # Set the sender, subject, and content of the email
    msg['From'] = Sender_Email
    # Check if Recipient_Emails is a list or a string and handle to multiple recipient mails
    if isinstance(Recipient_Emails, list):
        msg['To'] = ', '.join(Recipient_Emails)  # Join multiple recipients with a comma
    else:
        msg['To'] = Recipient_Emails  # Single recipient
    msg['Subject'] = Subject
    msg.set_content(Content)

    try:
        # Connect to the SMTP server using Gmail's SMTP server address and port number
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Start TLS (Transport Layer Security) for secure communication
        server.starttls()

        # Login to the SMTP server with your email and app-specific password
        server.login(Sender_Email, App_password)

        # Send the email message
        server.send_message(msg)
        print(f"Email sent successfully to {Recipient_Emails}!")

    except smtplib.SMTPAuthenticationError:
        # This exception is raised for authentication errors
        print("Failed to authenticate. Check your email and password.")
    except smtplib.SMTPException as e:
        # This exception is raised for other SMTP errors
        print("SMTP error occurred:", e)
    except Exception as e:
        # This catches any other exceptions that might occur
        print("Failed to send email:", e)

    finally:
        # Quit the SMTP server
        server.quit()

# Main usage
"""
    In case, if your sending mail for single person means create an string variable like below

    Recipient_Emails = "recipient1_email@gmail.com"

    In other case, if you want to send mail to more the one person means create a variable as list like below

    Recipient_Emails = ["recipient1_email@gmail.com", "recipient2_email@gmail.com"]
"""

Recipient_Emails = "recipient1_email@gmail.com"

Subject = "Test Email"
Content = "This is a test email sent from Python."

# Sending mail
Send_Mail(Recipient_Emails, Subject, Content)

