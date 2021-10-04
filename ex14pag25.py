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
print("indicati",l*l, "elemente ce vor fi introduse in tablou")  
for i in range(l):        
    a =[] 
    for j in range(c):    
         a.append(int(input())) 
    matrix.append(a) 
for i in range(l): 
    for j in range(c): 
        print(matrix[i][j], end = " ") 
    print() 
for e in range(len(matrix[0])):
    print(matrix[e][e])
d = (matrix[::-1])
for q in range(len(d[0])):
    print(d[q][q])
for g in range(len(matrix)):
    for h in range(len(matrix)):
        if g-h < 0:
            print(matrix[g][h])
for b in range(len(matrix)):
    for n in range(len(matrix)):
        if b-n > 0:
            print(matrix[b][n])
for c in range(len(d)):
    for v in range(len(d)):
        if c-v < 0:
            print(d[c][v])
for k in range(len(d)):
    for l in range(len(d)):
        if k-l > 0:
            print(d[k][l])
