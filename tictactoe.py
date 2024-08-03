class TicTacToe:
    def __init__(self, player1_pm, player2_pm):
        self.fields = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Инициализация игрового поля
        self.player1 = player1_pm
        self.player2 = player2_pm

    def check_winner(self):
        # Определение выигрышных комбинаций
        winning_combinations = [
            (0, 1, 2), (0, 4, 8), (0, 3, 6),
            (2, 4, 6), (1, 4, 7), (3, 4, 5),
            (6, 7, 8), (2, 5, 8)
        ]

        # Проверка, выиграл ли кто-нибудь из игроков
        for comb in winning_combinations:
            if self.fields[comb[0]] == self.fields[comb[1]] == self.fields[comb[2]] == 1:
                print(f"{self.player1} выиграл!")
                return True
            elif self.fields[comb[0]] == self.fields[comb[1]] == self.fields[comb[2]] == 2:
                print(f"{self.player2} выиграл!")
                return True

    def play(self):
        queue = [1, 2, 1, 2, 1, 2, 1, 2, 1]
        draw = []
        for item in queue:
            field = int(input(f"Ход игрока {item}:"))
            if self.fields[field] == 0:
                self.fields[field] = item
                draw.append(item)
                print(self.fields[0:3])
                print(self.fields[3:6])
                print(self.fields[6:])
                print("------------")
                if self.check_winner():
                    break
                if draw == queue:
                    print("НИЧЬЯ!")


# Пример использования класса TicTacToe
t1 = TicTacToe("Игрок 1", "Игрок 2")

t1.play()
