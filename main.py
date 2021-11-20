import instaloader
from tkinter import *
window=Tk()
btn=Button(window, text="THANK YOU FOR BEING WITH US", fg='blue')
btn.place(x=80, y=100)
lbl=Label(window, text="RAJ INSTA VERSION", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.title('INSTA LOADER VARIFIED')
window.geometry("300x200+10+10")
window.mainloop()
import re
while True:

  user_input = input("Set a password for varification: ")
  is_valid = False

  if (len(user_input)<6 or len(user_input)>12):

    print("Not valid ! Total characters should be between 6 and 12")
    continue
  elif not re.search("[A-Z]",user_input):

    print("Not valid ! It should contain one letter between [A-Z]")
    continue
  elif not re.search("[a-z]",user_input):

    print("Not valid ! It should contain one letter between [a-z]")
    continue
  elif not re.search("[1-9]",user_input):

    print("Not valid ! It should contain one letter between [1-9]")
    continue
  elif not re.search("[~!@#$%^&*]",user_input):

    print("Not valid ! It should contain at least one letter in [~!@#$%^&*]")
    continue
  elif re.search("[\s]",user_input):

    print("Not valid ! It should not contain any space")
    continue
  else:

    is_valid = True
    break


if(is_valid):
  print("Password is valid")


ig = instaloader.Instaloader()
dp = input("Enter Insta username : ")

import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.instagram.com//')
soup = BeautifulSoup(html.text, 'lxml')
item = soup.select_one("meta[property='og:description']")
name = item.find_previous_sibling().get("content").split("•")[0]
followers = item.get("content").split(",")[0]
following = item.get("content").split(",")[1].strip()
print(f'{name}\n{followers}\n{following}')

ig.download_profile(dp, profile_pic_only=True)

from datetime import datetime, timedelta
ini_time_for_now = datetime.now()
print ("initial_date", str(ini_time_for_now))
future_date_after_2yrs = ini_time_for_now + \
                         timedelta(days = 730)

future_date_after_2days = ini_time_for_now + \
                          timedelta(days = 2)

# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))
