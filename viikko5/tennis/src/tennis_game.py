# Tämän tenniksen pistelaskusysteemissä on pientä vikaa. Eikö tilanne 40-40 eli 3-3 ole jo Deuce?

score_strings = ["Love", "Fifteen", "Thirty", "Forty"]

class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):
        if self.score1 == self.score2:
            return self.tie()
        elif self.score1 >= 4 or self.score2 >= 4:
            return self.advantage_or_win()
        else:
            return f"{score_strings[self.score1]}-{score_strings[self.score2]}"
    
    def tie(self):
        if self.score1 < 4:
            return f"{score_strings[self.score1]}-All"
        else:
            return "Deuce"
    
    def advantage_or_win(self):
        difference = self.score1 - self.score2

        if difference == 1:
            return f"Advantage {self.player1}"
        elif difference == -1:
            return f"Advantage {self.player2}"
        elif difference >= 2:
            return f"Win for {self.player1}"
        else:
            return f"Win for {self.player2}"


