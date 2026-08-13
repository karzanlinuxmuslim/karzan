import smtplib
from colorama import Fore

print(f"The Project is Created By {Fore.BLUE}KarzanPc Python{Fore.WHITE}for sending Sms via email phishing")

email = input(f"Hacker email> ")
pas = input(F"Enter App Password of Hacker Email> ")
target_email = input(f"Target Email> ")

sub = input(f"SubJect> ")
msg = input(f"Message?> ")

text = f"Inatagram Help: {sub}\n\n{msg}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email,pas)
server.sendmail(email, target_email, text)
print(f"{Fore.GREEN} Success the Email is sended to the Target{Fore.WHITE}")