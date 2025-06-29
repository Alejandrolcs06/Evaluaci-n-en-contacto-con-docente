import random

# Lista de opciones válidas
opciones = ["piedra", "papel", "tijera"]

# Contadores de resultados
ganadas = 0
perdidas = 0
empates = 0

print("🎮 Bienvenido al juego de Piedra, Papel o Tijera 🎮")
print("Escribe 'salir' para terminar el juego en cualquier momento.\n")

# Estructura repetitiva: mientras el jugador no escriba 'salir'
while True:
    jugador = input("Elige: piedra, papel o tijera ➡ ").lower()

    # Opción para salir del juego
    if jugador == "salir":
        print("\nGracias por jugar. ¡Hasta la próxima!")
        break

    # Validación de la entrada
    if jugador not in opciones:
        print("❌ Opción inválida. Intenta de nuevo.\n")
        continue

    # Elección aleatoria de la computadora
    computadora = random.choice(opciones)
    print(f"🖥️ La computadora eligió: {computadora}")

    # Estructura lógica condicional para determinar el resultado
    if jugador == computadora:
        print("🤝 ¡Empate!\n")
        empates += 1  # Aumenta contador de empates
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("🎉 ¡Ganaste!\n")
        ganadas += 1  # Aumenta contador de victorias
    else:
        print("😢 Perdiste.\n")
        perdidas += 1  # Aumenta contador de derrotas

    # Mostrar resultados acumulados
    print("📊 Resultados hasta ahora:")
    print(f"   Ganadas: {ganadas}")
    print(f"   Perdidas: {perdidas}")
    print(f"   Empates: {empates}\n")