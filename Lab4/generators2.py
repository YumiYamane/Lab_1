def evengen(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=int(input())
even = []
for i in evengen(n):
    even.append(str(i))
print(", ".join(even))