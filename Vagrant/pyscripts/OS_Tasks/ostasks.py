#!/usr/bin/python3
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
    print("User Already Exists")
    print("################################")