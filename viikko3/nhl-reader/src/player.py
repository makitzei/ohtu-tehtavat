class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
    
    def __str__(self):
        points = self.goals + self.assists
        return f"{self.name:20} {self.team:3} {str(self.goals):>2} + {str(self.assists):>2} = {str(points):>3}"