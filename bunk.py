import getpass
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
a=input("Enter username : ")
b=getpass.getpass("Enter your password : ")
payload={"username":a,"password":b}
r=requests.post("https://academics.gndec.ac.in/",data=payload)
cookies=r.cookies
values2={"student_view_attendance":"in"}
rpost2 = requests.post("https://academics.gndec.ac.in", cookies=cookies, data=values2)
soup=BeautifulSoup(rpost2.content,'html.parser')
li=list(soup.find_all("td"))
li2=[]
li3=list(soup.find_all("span"))
li5=[]
for i in li:
   li5.append(i.get_text())
li6=[]
li6=li5[8:len(li5)-2]
lov=int(len(li6)/6)
yy=0
fl=[]
for x in range(1,lov+1):
   lis=[]
   for i in range(6):
      lis.append(li6[i+yy])
   yy+=6
   fl.append(lis)
for i in range(lov):
   a=(int(fl[i][4])-int(fl[i][3])*0.75)//0.75

   fl[i].append(a)

print(tabulate(fl,headers=["S.no","subject","subject code","No of lectures Held","No of lectures attended","%ge","Bunks permitted"]))

