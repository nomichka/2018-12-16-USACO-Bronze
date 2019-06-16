#READING
fin=open("blist.in", "r")
lines=fin.readlines()
num_cows=int(lines[0])
cows=lines[1: num_cows+1]
for i in range(num_cows):
    cows[i]=cows[i].split(" ")
    cows[i][0]=int(cows[i][0])
    cows[i][1]=int(cows[i][1])
    cows[i][2]=int(cows[i][2])
#ORDERING by start time
order_start=[]
for i in range(num_cows):
    order_start.append(cows[i][0])
order_sorted=sorted(order_start)
od=[]
for i in range(num_cows):
    s=order_sorted[i]
    index=order_start.index(s)
    od.append(cows[index])
"""
#ITERATING
max_b=0
for i in range(num_cows):
    now_b=od[i][2]
    now_t1=od[i][1]
    for j in range(i+1, num_cows):
        now_s2=od[j][0]
        now_t2=od[j][1]
        if now_s2<now_t1:
            now_b+=od[j][2]
        else:
            break
    max_b=max(max_b, now_b)
"""
max_b=0
num_b=0
including=[0]
for i in range(num_cows):
    s=od[i][0]
    b=od[i][2]
    num_b=b
    for j in range(num_cows):
        ss=od[j][0]
        tt=od[j][1]
        bb=od[j][2]
        if ss<s<tt:
            num_b+=bb
        max_b=max(max_b, num_b)


#WRITING
fout=open("blist.out", "w")
fout.write(str(max_b)+"\n")
fout.close()





