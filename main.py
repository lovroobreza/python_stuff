import datetime as dt
from smtplib import SMTP
import pandas, json

MY_EMAIL="obreza.lovro@gmail.com"
MY_PASSWORD="xlhwzayhmawffjad"

today = (dt.datetime.now().day, dt.datetime.now().month)

def main():
    data = pandas.read_csv("./files/rojstni-dnevi.csv")

    birthday_dict={(d["dan"], d["mesec"]): (d["email"], d["name"]) for (index, d) in data.iterrows()}
    
    for item in birthday_dict.items():
        if (item[0] == today):
            voscilnica_path="./files/voscilnica.txt"
            with open(file=voscilnica_path, encoding="utf-8") as letter_file:
                contents = letter_file.read()
                contents = contents.replace("[NAME]", item[1][1])
            
            with SMTP(host="smtp.gmail.com", port=587) as conntection:
                conntection.starttls()
                conntection.login(MY_EMAIL, MY_PASSWORD)
                conntection.sendmail(from_addr=MY_EMAIL,
                                     to_addrs=item[1][0], 
                                     msg=f"SUBJECT: Vse najbolje\n\n{contents}".encode("utf-8"))
    

main()
print("Successfull exit")