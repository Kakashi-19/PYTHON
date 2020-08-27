import os
totalsize = 0
for file in os.listdir(r"C:\Users\vaibhav pratap singh\Desktop\python"):
    if os.path.isfile(os.path.join('C:\\Users\\vaibhav pratap singh\\Desktop\\python', file)) == True:
        b = os.path.getsize(os.path.join('C:\\Users\\vaibhav pratap singh\\Desktop\\python', file))
        totalsize += b

print(totalsize)

