import subprocess

# Get Chrome version via subprocess
output = subprocess.check_output(r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value', shell=True)
print(output.decode('utf-8').strip())

raw_input("Press Enter to exit")