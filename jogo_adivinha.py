import random

print("=== JOGO DE ADIVINHAÇÃO ===")

# O computador escolhe um número de 1 a 10
numero_secreto = random.randint(1, 10)

palpite = 0

# O jogo continua até o jogador acertar
while palpite != numero_secreto:
    palpite = int(input("Adivinha o número (entre 1 e 10): "))
    
    if palpite == numero_secreto:
        print("🎉 Boa! Acertaste em cheio!")
    else:
        print("❌ Ah, não foi esse. Tenta outra vez!\n")
