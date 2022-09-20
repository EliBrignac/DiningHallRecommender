
#from email.quoprimime import body_check
import smtplib, ssl
import working_web_scraper_3
from google_sheet_1 import records_data

print('Working...')

try:
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "dininghallrecommender@gmail.com"
    password = input("Type your password and press enter: ")
    for record in records_data:
        receiver_email = record['Email Address']
        subject_text = """Subject: Todays Scores \n"""
        body_text = ''
        # body_text += working_web_scraper_3.top_meal(record) This is the linith the problem
        formatted_results = working_web_scraper_3.top_meal(record)
        body_text += formatted_results
        body_text += working_web_scraper_3.find_overall_scores(record)
        body_text += "\n" + "\n"
        body_text += """If you would like to edit your response, search for 'Dining Preferences:' in your gmail,
        and click 'edit response' to edit your response.
        """

        message = subject_text + body_text

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            # TODO: Send email here
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            # Print any error messages to stdout
            print('first one')
            print(record['Timestamp'])
            print(formatted_results)
            print(e)
        finally:
            server.quit()
except Exception as e:
    print('second one')
    # Print any error messages to stdout
    print(e)

print("Done")
