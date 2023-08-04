f = open("diamond.in")

l = [int(i) for i in f.readline().split()]
N = int(l[0])
K = l[1]

diamonds = []
for i in range(N):
    diamonds.append(int(f.readline()))

diamonds.sort()    
i = 0
largest = 0
while i < N:
    for x in range(i+1,N+1):
        if len(diamonds[i:x]) > largest:
            if max(diamonds[i:x]) - min(diamonds[i:x]) <= K:
                largest = len(diamonds[i:x])
    i += 1
    

with open("diamond.out","w") as f:
    f.write(str(largest))
  
