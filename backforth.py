#READING
fin=open("backforth.in", "r")
lines=fin.readlines()
for i in range(2):
    lines[i]=lines[i].split(" ")
    """
    for j in range(10):
        lines[i][j]=int(lines[i][j])
    """
barn1=lines[0]
barn2=lines[1]

#GETTING RID of >2
b1=[]
for bucket in barn1:
    if bucket in b1:
        b1.remove(bucket)
        if bucket not in b1:
            b1.append(bucket)
    b1.append(bucket)
b2=[]
for bucket in barn2:
    if bucket in b2:
        b2.remove(bucket)
        if bucket not in b2:
            b2.append(bucket)
    b2.append(bucket)

#ALL options
amounts=[]
c1_1=' '.join(map(str, b1))
c2_1=' '.join(map(str, b2))
for i in range(len(b1)):
    a=1000
    b1=c1_1.split(" ")
    b2=c2_1.split(" ")
    bucket=b1[i]
    b1.remove(bucket)
    b2.append(bucket)
    a-=int(bucket)
    c1_2=' '.join(map(str, b1))
    c2_2=' '.join(map(str, b2))
    new1=a
    for j in range(len(b2)):
        a=new1
        b1=c1_2.split(" ")
        b2=c2_2.split(" ")
        bucket1=b2[j]
        b2.remove(bucket1)
        b1.append(bucket1)
        a+=int(bucket1)
        c1_3=' '.join(map(str, b1))
        c2_3=' '.join(map(str, b2))
        new2=a
        for k in range(len(b1)):
            a=new2
            b1=c1_3.split(" ")
            b2=c2_3.split(" ")
            bucket2=b1[k]
            b1.remove(bucket2)
            b2.append(bucket2)
            a-=int(bucket2)
            c1_4=' '.join(map(str, b1))
            c2_4=' '.join(map(str, b2))
            new3=a
            for l in range(len(b2)):
                a=new3
                b1=c1_4.split(" ")
                b2=c2_4.split(" ")
                bucket3=b2[l]
                b2.remove(bucket3)
                b1.append(bucket3)
                a+=int(bucket3)
                if a not in amounts:
                    amounts.append(a)


#WRITING
fout=open("backforth.out", "w")
fout.write(str(len(amounts))+"\n")
fout.close()











