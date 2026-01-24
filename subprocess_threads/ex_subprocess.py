import subprocess
import sys


cmd = ['ls -lah /']
plataform = sys.platform
encoding = 'utf-8' 

if plataform == 'win32':
    encoding = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,text=encoding, shell=True
)



print(proc.stdout)

