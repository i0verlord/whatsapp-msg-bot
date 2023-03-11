# Using python to send message

import pywhatkit as snd

# taking inputs
num = input("Enter the receiver's number: ")
msg = input("Enter the message: ")
hrs = eval(input("Enter the hour: "))
min = eval(input("Enter the minute: "))

# Line to send message
snd.sendwhatmsg(num, "msg", hrs, min)