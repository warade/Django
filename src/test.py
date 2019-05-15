#!/usr/bin/python
"""Copyright 2008 Orbitz WorldWide
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

import sys
import time
import os
import platform 
import subprocess
from socket import socket
import datetime


CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003
delay = 2
sock = socket()
try:
  sock.connect( (CARBON_SERVER,CARBON_PORT) )
except:
  print("Couldn't connect to %(server)s on port %(port)d, is carbon-agent.py running?" % { 'server':CARBON_SERVER, 'port':CARBON_PORT })
  sys.exit(1)

cnt = 0

import graphitesend
g = graphitesend.init(prefix='test', system_name='', graphite_server='127.0.0.1')
g.send('count', 10)


# while True:
#   now = int( time.time() )
#   Now = datetime.datetime.now()
#   message = "test.count " + str(cnt%10) + " " + str(now)
#   cnt = cnt + 1
#   print(message)
#   #We're gonna report all three loadavg values
# #   loadavg = get_loadavg()
# #   lines.append("system.loadavg_1min %s %d" % (loadavg[0],now))
# #   lines.append("system.loadavg_5min %s %d" % (loadavg[1],now))
# #   lines.append("system.loadavg_15min %s %d" % (loadavg[2],now))
# #   message = '\n'.join(lines) + '\n' #all lines must end in a newline
# #   print("sending message\n")
# #   print('-' * 80)
# #   print(message)
# #   print()
#   sock.sendall(message)
#   time.sleep(delay)