
import subprocess
import sys
import os
import requests
import time

HOST            = os.environ["AWSEC"]
FOLDER          = r"C:\Users\Tristan\Desktop\bigFungus"
PEMLOCATION     = r"C:\Users\Tristan\Desktop\topcap.pem"
REMOTE_PATH     = "/home/ubuntu/testUpload"
LAUNCH_SCRIPT   = f"cd {REMOTE_PATH}/bigFungus && nohup gunicorn --workers=3 bigFungusWeb:app && exit" 
COMMAND_GETPID  = "ps ax  | grep bigFungusWeb | awk '{print $1}'"
COMMAND_UPLOAD  = f"scp -i {PEMLOCATION} -r {FOLDER} {HOST}:{REMOTE_PATH}"

def exec_remote(command, host=HOST) -> list or NotImplementedError:
    ssh = subprocess.Popen(["ssh", "-i", PEMLOCATION, "%s" % host, command],
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print(sys.stderr, "ERROR: %s" % error)
    return result

def upload_files():
    print(subprocess.run(COMMAND_UPLOAD, capture_output=True))
    pass

#upload_files()
try:
    pidstring = ' '.join([str(int(i)) for i in exec_remote(COMMAND_GETPID)])
    print(f"KILLING --> : {pidstring}")
    KILL = exec_remote(f"kill {pidstring}")
    print(KILL)
    
except Exception as e:
    print(e)
    pass

finally:
    LAUNCH  = subprocess.Popen(["ssh", "-i", PEMLOCATION, "%s" % HOST, LAUNCH_SCRIPT])
    print(LAUNCH)

time.sleep(5)
base_url = requests.get('https://bigfungus.ca/')
assert int(base_url.status_code) == 200