import boto3
from botocore.exceptions import ClientError
# Create a new SES resource and specify a region.
client = boto3.client('ses', region_name='us-east-1')

def feedbackForm(email, body):
	# Replace sender@example.com with your "From" address.
	# This address must be verified with Amazon SES.
	SENDER = "Big Fungus <bigfungus.ca@gmail.com>"

	# Replace recipient@example.com with a "To" address. If your account 
	# is still in the sandbox, this address must be verified.
	RECIPIENT = email

	# The subject line for the email.
 
	SUBJECT = f"BigFungus automated email"

	# The email body for recipients with non-HTML email clients.
	BODY_TEXT = (f"Thanks for contacting us!\r\n"
				"A service representative will get back to you shortly for your inquiry:\r\n"
				f"{body}"
				)
				
	# The HTML body of the email.
	BODY_HTML = f"""<html>
	<head></head>
		<body>
			<h1>Thanks for contacting us!</h1>
			<p>A service representative will get back to you shortly for your inquiry:</p>
			<p>{body}</p>
   			<br/>
			<img src='https://bigfungus.ca/static/big_fungus.png' alt= 'image not found' />
		</body>
	</html>
				"""            

	# The character encoding for the email.
	CHARSET = "UTF-8"
 
	# Try to send the email.
	try:
		#Provide the contents of the email.
		response = client.send_email(
			Destination={
				'ToAddresses': [
					RECIPIENT,
					"bigfungus.ca@gmail.com",
				],
			},
			Message={
				'Body': {
					'Html': {
						'Charset': CHARSET,
						'Data': BODY_HTML,
					},
					'Text': {
						'Charset': CHARSET,
						'Data': BODY_TEXT,
					},
				},
				'Subject': {
					'Charset': CHARSET,
					'Data': SUBJECT,
				},
			},
			Source=SENDER,

		)
	# Display an error if something goes wrong.	
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print("Email sent! Message ID:"),
		print(response['MessageId'])
  
if __name__ == "__main__":
    feedbackForm("rhsensors@gmail.com", "this is a test email")