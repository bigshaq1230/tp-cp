import numbers
x = input()
l = []
sum = 0
type = ""
def resolve(c):
    if(c.isnumeric()):
        return int(c)
    else:
        if(c == "T"):
            return 10
        elif(c == "J"):
            return 11
        elif(c == "Q"):
            return 12
        elif(c == "K"):
            return 13
        elif(c == "A"):
            return 14
for i in range(len(x)):

    if(i == 1):
        type = x[i]
    elif(x[i] == " "):
        continue
    else:
        if(i%3 == 0):
            h = resolve(x[i])
            l.append(h)
            sum += h
        elif(i%3 == 1 and type != x[i]):
            print("NO")
            break


if(len(l)==5):
    l.sort()
    s = (5/2)*(l[0] + l[-1])
    if(s != sum):
        print("NO")
    else:
        print("YES")