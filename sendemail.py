import sendgrid

sg = sendgrid.SendGridClient('kevindiaz2990', 'Firemblem9%')

message = sendgrid.Mail()
message.add_to('Kevin Diaz <kevindiaz2990@gmail.com>')
message.set_subject('Example')
message.set_html('Body')
message.set_text('Body')
message.set_from('Doe John <doe@email.com>')
status, msg = sg.send(message)

#or

