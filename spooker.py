import functools
import operator
import os.path
import subprocess
from datetime import datetime
import pytz
from pathlib import Path
process = subprocess.Popen(['ipconfig'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
output_string = ""

while True:
    output = process.stdout.readline()
    print(output.strip())
    output_string = output_string + output.strip() + "\n"
    print("outputstring", output_string)
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output
        for output in process.stdout.readlines():
            print(output.strip())
            output_string_system = output_string_system + output.strip() + "\n"




        break

downloads_path = str(Path.home() / "Downloads")
print(downloads_path)


tz_london = pytz.timezone('Europe/London')
datetime_london = datetime.now(tz_london)
save_path = downloads_path
name_of_file = "WARNING"
completeName = os.path.join(save_path, name_of_file+".txt")
file1 = open(completeName, "w")
tup1 = ("London time:", datetime_london.strftime("%H:%M:%S") + "\n" + "\n" + "WARNING:" + "\n" + "- - - - - - - -" + "\n" + "NICE IP ADDRESS BOZO" + "\n" + output_string + "\n")
str = functools.reduce(operator.add, (tup1))
print(str)
file1.write(str)
file1.close()











process = subprocess.Popen(['systeminfo'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)
output_string_system = ""

while True:
    output = process.stdout.readline()
    print(output.strip())
    output_string_system = output_string_system + output.strip() + "\n"
    print("outputstring", output_string_system)
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output
        for output in process.stdout.readlines():
            print(output.strip())
            output_string_system = output_string_system + output.strip() + "\n"



        break

# downloads_path = str(Path.home() / "Downloads")
print(downloads_path)


# tz_london = pytz.timezone('Europe/London')
# datetime_london = datetime.now(tz_london)
save_path = downloads_path
name_of_file = "SYSTEM SPECS"
completeName = os.path.join(save_path, name_of_file+".txt")
file1 = open(completeName, "w")
# tup1 = ("London time:", datetime_london.strftime("%H:%M:%S") + "\n" + "\n" + "WARNING:" + "\n" + "- - - - - - - -" + "\n" + "NICE IP ADDRESS BOZO" + "\n" + output_string + "\n")
tup2 = output_string_system
str2 = functools.reduce(operator.add, tup2)
print(str2)
file1.write(str2)
file1.close()