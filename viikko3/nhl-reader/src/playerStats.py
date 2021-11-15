import datetime

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader


    def top_scorers_by_nationality(self, country):
        players = self.reader.get_players()

        players_filtered = list(filter(lambda p: p.nationality == country, players))
        players_filtered = sorted(players_filtered, key=lambda player: player.assists+player.goals, reverse=True)

        print("Players from", country, datetime.datetime.now())

        return players_filtered