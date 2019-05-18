import getpass # this library is used to take password and username from user in secure way
import requests # this  library is used to interact with language
from bs4 import BeautifulSoup # this is used to parse web data
from tabulate import tabulate # tabulate the data in nice manner
user_name=input("Enter username : ")
passwd=getpass.getpass("Enter your password : ")# take password in secure manner
payload={"username":user_name,"password":passwd} #values to be supplied to webpage
r=requests.post("https://academics.gndec.ac.in/",data=payload) #post the values to web page and return the response after submission
cookies=r.cookies  # this will keep track of our response recieved
values2={"student_view_attendance":"in"}
rpost2 = requests.post("https://academics.gndec.ac.in", cookies=cookies, data=values2) #click the view attendance button, we have used cookies here because we are under same session only so to send further requests we have to keep track of previous response recieved
soup=BeautifulSoup(rpost2.content,'html.parser')# this make the html content of the page in readable form and easy to parse
li=list(soup.find_all("td"))# this will make a list of all the content of all td tag the td tag contains the details of attendance
li2=[]
li5=[]
for i in li:
   li5.append(i.get_text())# this will append the text contained in td tag
li6=[]
li6=li5[8:len(li5)-2]# this will extract the details of all the subjects
lov=int(len(li6)/6)# count total number of  subjects
yy=0#count
fl=[]
for x in range(1,lov+1):
   lis=[]# this will contain all details of individual subject
   for i in range(6):
      lis.append(li6[i+yy])
   yy+=6
   fl.append(lis)# this will store all sublist
for i in range(lov):
   a=(int(fl[i][4])-int(fl[i][3])*0.75)//0.75

   fl[i].append(a)# this will append the bunks calculated in each sublist

print(tabulate(fl,headers=["S.no","subject","subject code","No of lectures Held","No of lectures attended","%ge","Bunks permitted"]))
# print all the data in tabular form
