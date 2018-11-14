"""
What is the most interesting/funny/cool thing(s) about Python that you learned from this class or from somewhere else.

You can use code or a short paragraph to illustrate it.
"""

# As a computer enthusiast and a worker in Babson IT, I looked for some ways that Python can help us better pull up data
# from students / faculties' laptop. And by using some libraries such as platform, some lines of python code can help us
# see what computers the users are using, as well as their Asset Tag ID.

print("Gathering system info...")

import platform
bit = platform.machine()
platformname = platform.platform()
generalinfo = platform.uname()
system = platform.system()
CPU = platform.processor()

print("The user is running ", bit[-2:], "bit system.")
print("OS: ", platformname.split('-')[0],platformname.split('-')[1])
print("Asset Tag / System ID: ", generalinfo[1])
if generalinfo[1][0:2] == "L1":
    print("This is a Babson-issued laptop.")
    if generalinfo[1][2] == "8":
        print("Model Number: Lenovo X1-Yoga Gen3")
    else:
        print("Model Number: Lenovo X1-Yoga Gen2")
elif generalinfo[1][0:2] == "D1":
    print("This is a Babson-issued desktop.")
else:
    print('This is a non-Babson computer.')

print("The computer is running a", generalinfo[-1].split()[-1], "CPU.")