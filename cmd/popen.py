import time
import subprocess

p = subprocess.Popen("tail -f {}/celery.log".format("logs"), shell=True, stdout=subprocess.PIPE)
while p.poll() is None:
    line = p.stdout.readline()
    print(line)

# It's done
print("Process ended, ret code:", p.returncode)
