"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""


def rock_paper_scissor(games):
    # Comprobacion de quien gana, uso de matriz
    rules: dict = {"🗿": ["✂", "🦎"],
                   "🧻": ["🗿", "🖖"],
                   "✂": ["🖖", "🦎"],
                   "🦎": ["🖖", "🧻"],
                   "🖖": ["🗿", "✂"]
                   }

    player_one = 0

    player_tow = 0

    for game in games:
        player_one_game = game[0]
        player_tow_game = game[1]
        if player_one_game != player_tow_game:
            if player_tow_game in rules[player_one_game]:
                player_one += 1
            else:
                player_tow += 1

    return "Tie" if player_one == player_tow else "Player 1 won" if player_one > player_tow else "Player 2 won"


print(rock_paper_scissor([("🗿", "🧻"),("🖖", "🦎"),("🦎", "🦎"),("🗿", "🖖"),("🗿", "✂"),("🦎", "🦎"),
                          ("✂", "🧻"),("🗿", "🖖"),("🗿", "✂"),("🗿", "🦎"),("🗿", "✂"),("🗿", "🧻")]
                         ))

