# code by @riskiakbar279
# website : riskiakbar279.rf.gd
# artikel  : sxcodeprogrammerid.xyz

#import system
import requests, os, sys, time
from multiprocessing.pool import ThreadPool
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
r= requests.Session()
def find(y):
    try:
     kont=requests.get(url+y,timeout=10)
     if kont.status_code < 200 or kont.status_code <= 201:
      print "%s[%s!%s] %s%s ===> %sFound"%(pu,qu,pu,url,y,hi)
      open("hasil.txt","a+").write(sys.argv[1]+y+'\n')
     else:
      print "%s[%s!%s] %s%s ===> %sNot Found"%(pu,qu,pu,url,y,me)
    except Exception as e:
      print "%s%s"%(me,e)
      pass

try:
  os.system("clear")
  if 'https' or 'http' not in sys.argv[1]:
   url=sys.argv[1]
  else:
   url='https://'+sys.argv[1]
  print """%s
     _       _ _____ _           _  
    / \   __| |  ___(_)_ __   __| |
   / _ \ / _` | |_  | | '_ \ / _` | %scode by riskiakbar279%s
  / ___ \ (_| |  _| | | | | | (_| | %sartikel : sxcodeprogrammerid.xyz%s
 /_/   \_\__,_|_|   |_|_| |_|\__,_| %sAdmin Login Finder"""%(qu,pu,qu,pu,qu,pu,qu,qu)
  sys.argv[1]
  print
  ThreadPool(30).map(find,open("list.txt").read().splitlines())
  print "\n%s[%s✓%s] %sDone, file saved in %shasil.txt"%(pu,qu,pu,pu,ku)
except requests.exceptions.ConnectionError:
        exit('%s[%s!%s] %sCheck your internet'%(pu,qu,pu,pu))
except IndexError:
        exit('%s[%s!%s] Use : python2 %s https://domain.com'%(pu,qu,pu,sys.argv[0]))
except KeyboardInterrupt:
        exit('\n%s[%s!%s] %sClosing...'%(pu,qu,pu,pu))
