import time
initial = time.time()
k = 0
while(k<45):

    print("This is Mustafa Hassan")
    k+=1
    print("while loop ran in", time.time() -initial, "seconds")

initial2 = time.time()
for i in range(45):
    print("This is Mustafa Hassan")
    print("for loop ran in", time.time() -initial, "seconds")