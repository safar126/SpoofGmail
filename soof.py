import os, sys, requests
os.system("clear")
print("Code By = Safar/Cupu\nPemilikApi =Njank\nTools = Spoof gmail")
print('=' *30)
a = input("Nama Anda: ")
b = input("Email Anda: ")
c = input("Reply Nama: ")
d = input("Reply Email: ")
e = input("Email Tujuan: ")
f = input("Subject: ")
g = input("Isi Pesan:" )
url = "https://al-hikmah.xyz/Tools/api.php"

a = requests.post(url ,data={"fromname":a, "fromemail":b, "replytoname":c, "replytoemail":d, "to":e, "subject":f, "message":g,"submit":"Send"})
print("Pesan Gmail ke ==>" , e)


