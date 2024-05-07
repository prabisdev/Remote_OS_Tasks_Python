from fabric.api import *
env.user = 'devops'
def greeting(msg):
  print "Good %s" % msg

def system_info():
  print "Disk Space"
  local("df -h")

  print "RAM size"
  local("free -m")

  print "System uptime."
  local("uptime")