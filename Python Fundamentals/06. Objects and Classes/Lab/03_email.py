class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
email_data = input()

while not email_data == "Stop":
    sen, rec, con = email_data.split()
    current_email = Email(sen, rec, con)
    emails.append(current_email)
    email_data = input()

mails_to_send = [int(index) for index in input().split(", ")]
for i in mails_to_send:
    email = emails[i]
    email.send()

for email in emails:
    print(email.get_info())
