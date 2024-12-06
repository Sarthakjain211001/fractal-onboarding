from datetime import datetime
def generateTimestamp():
    curr_dt_time = datetime.now()
    return curr_dt_time

try:
    with open('logfile.txt', 'a') as file:
        file.write(f'{generateTimestamp()} Process started\n')
        file.write(f'{generateTimestamp()} Process in execution\n')    
        file.write(f'{generateTimestamp()} Error occured\n')
        file.write(f'{generateTimestamp()} Process end\n')
    with open('logfile.txt', 'r') as file:
        print(file.read())
except IOError:
    print("Some error occured")