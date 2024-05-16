def calcular_media_n1(a1, a2, a3, a4):
    media_n1 = (a1 + a2 + a3 + a4) / 4
    return media_n1

def calcular_nota_final(media_n1, n2):
    nota_final = (media_n1 * 0.4) + (n2 * 0.6)
    return nota_final

def verificar_aprovacao(nota_final):
    if nota_final >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

# Exemplo de uso:
a1 = float(input("Digite a nota da atividade 1 da N1: "))
a2 = float(input("Digite a nota da atividade 2 da N1: "))
a3 = float(input("Digite a nota da atividade 3 da N1: "))
a4 = float(input("Digite a nota da atividade 4 da N1: "))
n2 = float(input("Digite a nota da prova N2: "))

media_n1 = calcular_media_n1(a1, a2, a3, a4)
nota_final = calcular_nota_final(media_n1, n2)
resultado = verificar_aprovacao(nota_final)

print(f"A média da N1 é: {media_n1}")
print(f"A nota final da disciplina é: {nota_final}")
print(f"Resultado: {resultado}")
