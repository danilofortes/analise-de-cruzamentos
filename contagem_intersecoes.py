# Suponha que você tenha duas linhas P e Q horizontais e paralelas.
# Em cada uma delas estão distribuídos n pontos, atráves de uma lista p1,p2,...,pn na linha P e a outra lista q1, q2,...,qn na linha Q.
# Imagine um conjunto de n segmentos de linha conectando cada ponto pi a qi.
# Escreva um algoritmo para determinar quantos pares desses segmentos de linha se intersectam(cruzam).

#p1<p2 && q1>q2 (as linhas se cruzam)

#uso de ponteiros
#analise recursiva

linha_p = [1,2,3,4,5]
linha_q = [6,3,2,4,5]

cruzamentos = 0

for (ponteiro_1, _) in enumerate(linha_p):
    for (ponteiro_2, p2) in enumerate(linha_p[ponteiro_1 + 1:]):
        p1 = linha_p[ponteiro_1]
        q1 = linha_q[ponteiro_1]
        q2 = linha_q[ponteiro_1 + 1:][ponteiro_2]

        if((p1<p2) and (q1 > q2)):
            cruzamentos += 1


print(f'Cruzamentos:{cruzamentos}')
