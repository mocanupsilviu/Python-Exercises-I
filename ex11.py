"""
Exercise 11:
 Run the command "netstat -ano" in the command prompt.
 Get the output and print the following:
 Count of all Unique local address
 Count of all Unique Foreign addresses
 Unique State
 Unique PID
"""

import subprocess

def analyze_netstat():
    result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    print(lines)

    local_addresses = []
    foreign_addresses = []
    states = []
    pids = []

    for line in lines[4:]:
        columns = line.split()
        if len(columns) >= 5:
            local_address = columns[1].split(":")[0]
            foreign_address = columns[2].split(":")[0]
            state = columns[3]
            pid = columns[4]

            if local_address not in local_addresses:
                local_addresses.append(local_address)
            if foreign_address not in foreign_addresses:
                foreign_addresses.append(foreign_address)
            if state not in states:
                states.append(state)
            if pid not in pids:
                pids.append(pid)

    print("Count of Unique Local Addresses:", len(local_addresses))
    print("Count of Unique Foreign Addresses:", len(foreign_addresses))
    print("Unique States:", states)
    print("Unique PIDs:", pids)

analyze_netstat()