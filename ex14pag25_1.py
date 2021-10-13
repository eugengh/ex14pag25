"""
Elaboraţi un program care citeşte de la tastatură un tablou pătratic cu n linii,
2 ≤ n ≤ 10, şi afişează la ecran suma componentelor care se află:
	 a)	 pe diagonala principală;
	 b)	 pe diagonala secundară;
	 c)	 mai sus de diagonala principală;
	 d)	 mai jos de diagonala principală;
	 e)	 mai sus de diagonala secundară;
	 f)	 mai jos de diagonala secundară.
"""
l = int(input("randuri: ")) 
c = l

matrix = [] 
print("indicati", l*l, "elemente ce vor fi introduse in  tablou")   
for i in range(l):       
    a =[] 
    for j in range(c):    
         a.append(int(input())) 
    matrix.append(a) 
for i in range(l): 
    for j in range(c): 
        print(matrix[i][j], end = " ") 
    print()
dp = []  # diagonala princ
for e in range(len(matrix[0])):
    dp.append(matrix[e][e])
print(sum(dp))
ds = [] # diagonala secundara
d = (matrix[::-1])
for q in range(len(d[0])):
    ds.append(d[q][q])
print(sum(ds))
dpp = [] # deasupra diagonalei princ
for g in range(len(matrix)):
    for h in range(len(matrix)):
        if g-h < 0:
            dpp.append(matrix[g][h])
print(sum(dpp))
dss = [] # sub diagonala princ
for b in range(len(matrix)):
    for n in range(len(matrix)):
        if b-n > 0:
            dss.append(matrix[b][n])
print(sum(dss))
dppp = [] #deaspupra diagonalei secundare
for c in range(len(d)):
    for v in range(len(d)):
        if c-v < 0:
            dpp.append(d[c][v])
print(sum(dppp))
dsss= []        #sub diagonala secundara     
for k in range(len(d)):
    for l in range(len(d)):
        if k-l > 0:
            dsss.append(d[k][l])
print(sum(dsss))
