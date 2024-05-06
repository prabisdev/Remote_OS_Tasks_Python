#!/usr/bin/python3
## Checking weather users exists and adding Users
import os
userlist = ["alpha", "beta", "gama"]

print("Adding Users to System")
print("###############################")

for user in userlist:
  exitcode = os.system("id {}".format(user))
  if exitcode != 0:
    print ("User{} does note Exist.Adding It".format(user))
    print("###############################")
    print()
    os.system("useradd {}".formar(user))
  else:
    print("User Already Exists.Skipping it")
    print("################################")
  
### Checking the group availibility and adding group
exitcode = os.system("grep ProjectP1 /etc/group")
if exitcode ! = 0:
  print("Group ProjectP1 does not exists.Adding it ")
   print("################################")
   print()
else:
  print("Group Already Exists. Skipping it")
  print("##################################")
  print()
  