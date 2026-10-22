# 🎯 Jogo de Adivinhação em Python

Um projeto super simples e divertido de um jogo de adivinhação, ideal para iniciantes na programação que estão a dar os primeiros passos em Python.

---

## 🚀 Como Funciona o Jogo

1. O computador escolhe aleatoriamente um número entre **1 e 10**.
2. O jogador tenta adivinhar qual é o número.
3. Se acertar, o jogo dá os parabéns e termina.
4. Se errar, o programa avisa e dá uma nova oportunidade até acertar!

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** (utilizando a biblioteca básica `random`)

---

## 💻 Código do Projeto (`jogo_simples.py`)

```python
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
