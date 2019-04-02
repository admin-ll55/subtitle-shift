import os
import re
import sys
import traceback
def shift(line):
  global offset
  m = re.findall("(([0-9]):([0-9][0-9]):([0-9][0-9])\.([0-9][0-9]))", line)
  tsh = int(m[0][1])*3600000
  tsm = int(m[0][2])*60000
  tss = int(m[0][3])*1000
  tsms = int(m[0][4])
  ts = tsh+tsm+tss+tsms+offset
  tsh = int(ts//3600000)
  tsm = int((ts-tsh*3600000)//60000)
  tss = int((ts-tsh*3600000-tsm*60000)//1000)
  tsms = int((ts-tsh*3600000-tsm*60000-tss*1000))
  ts = m[0][0]
  line = line.replace(ts, str(tsh)+":"+str(tsm).zfill(2)+":"+str(tss).zfill(2)+"."+str(tsms).zfill(2))
  teh = int(m[1][1])*3600000
  tem = int(m[1][2])*60000
  tes = int(m[1][3])*1000
  tems = int(m[1][4])
  te = teh+tem+tes+tems+offset
  teh = int(te//3600000)
  tem = int((te-teh*3600000)//60000)
  tes = int((te-teh*3600000-tem*60000)//1000)
  tems = int((te-teh*3600000-tem*60000-tes*1000))
  te = m[1][0]
  line = line.replace(te, str(teh)+":"+str(tem).zfill(2)+":"+str(tes).zfill(2)+"."+str(tems).zfill(2))
  return line
try:
  if len(sys.argv) < 2 or len(sys.argv) > 3:
    raise("Invalid Arguments.")
  ass = re.sub("\\r\\n", "\\n", open(sys.argv[1], 'rb').read().decode())
  if len(sys.argv) == 2:
    offset = int(input("Please input offset in ms: "))
  else:
    offset = int(sys.argv[2])
  lines = ass.split("\n")
  for x in range(0, len(lines)):
    if re.search("^Dialogue:", lines[x]):
      lines[x] = shift(lines[x])
  os.rename(sys.argv[1], sys.argv[1]+".bak")
  open(sys.argv[1], 'wb').write(("\n".join(lines)).encode())
except:
  traceback.print_exc()
  input()
sys.exit(0)