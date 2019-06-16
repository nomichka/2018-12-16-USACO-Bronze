fin=open("mixmilk.in", "r")
lines=fin.readlines()

for i in range(3):
    lines[i]=lines[i].split(" ")
    lines[i][0]=int(lines[i][0])
    lines[i][1]=int(lines[i][1])
total=[lines[0][0], lines[1][0], lines[2][0]]
state=[lines[0][1], lines[1][1], lines[2][1]]
#all_states=[]
#all_states.append(state)

i=0
while i<100:
    i+=1
    taken=(i-1)%3
    given=i%3
    state[given]+=state[taken]
    state[taken]=0
    if state[given]>total[given]:
        extra=state[given]-total[given]
        state[taken]+=extra
        state[given]-=extra
    """
    if state in all_states:
        print(i)
        break
    all_states.append(state)
    """
output=""
for element in state:
    output+=str(element)+"\n"

fout=open("mixmilk.out", "w")
fout.write(output)
fout.close()
