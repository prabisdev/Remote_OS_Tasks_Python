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
    os.system("useradd {}".format(user))
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


### Adding Users to Group
for user in userlist:
  print("Adding User {} in the group ProjectP1".format(user))
  if exitcode != 0:
    print ("User{} does note Exist.Adding It".format(user))
    print("###############################")
    print()
    os.system("usermod G projectP1 {}".format(user))
  
### Creating a Dir and Changing Ownership and Editing Permissions

print ("Adding Directory")
print("###############################")
print()

if os.path.isdir("/opt/ ProejctP1"):
  print("Directory already exists, Skipping it")
else:
  os.mkdir("/opt/ ProejctP1")

print("Assigning Permissions and ownership to the directory")
print("###############################")
print()
os.system("chown : ProjectP1 /opt/ProjectP1")
os.system("chmod 770 /opt/ProjectP1")