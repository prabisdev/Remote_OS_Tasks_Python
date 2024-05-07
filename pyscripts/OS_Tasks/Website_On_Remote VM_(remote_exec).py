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

def remote_exec():
  print "Get System Info"
  run("hostname")
  run("uptime")
  run("df -h")
  run("free -m")

  sudo("yum install mariadb-server -y")
  sudo("systemctl start mariadb")
  sudo("systemctl enable mariadb")