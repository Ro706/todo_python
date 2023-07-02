import datetime
data = x = datetime.datetime.now()
date = data.strftime("%F")
message = str(input("Enter a message:"))
message = message.split("and")
data : str = ""
for i in message:
   data +=i
   data +="\n"
message = data
with open(f'{date}.txt', 'w') as f:
    f.write(message)

print("mission successful")
