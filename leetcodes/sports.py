class ScheduleMaker:
    """since it's not thread safe, it will kick you out if you try to create multiple schedules at once"""
    """code sample:
            main = ScheduleMaker([i for i in range(1, 9)])
            main.createScedule(10)

        _{func} as all functions exept createScedule are private and should only be accessed by createScedule
    """
    def __init__(self, teams):
        self.teams = teams
        self.teamsPlayed = {i: [] for i in range(1, len(teams)+1)}

        self.teamsPlayedThisRound = []
        self.whoPlayedWhothisRound = {}
        self.inAction = False


    def _playgame(self, team1, team2):
        self.teamsPlayed[team1].append(team2)
        self.teamsPlayed[team2].append(team1)
        self.teamsPlayedThisRound.append(team1)
        self.teamsPlayedThisRound.append(team2)
        self.whoPlayedWhothisRound[team1] = team2
        self.whoPlayedWhothisRound[team2] = team1


    def _unplay(self, team1, team2):
        self.teamsPlayed[team1].pop(self.teamsPlayed[team1].index(team2))
        self.teamsPlayed[team2].pop(self.teamsPlayed[team2].index(team1))
        self.teamsPlayedThisRound.pop(self.teamsPlayedThisRound.index(team1))
        self.teamsPlayedThisRound.pop(self.teamsPlayedThisRound.index(team2))
        self.whoPlayedWhothisRound[team1] = False
        self.whoPlayedWhothisRound[team2] = False
        


    def _pairTeamsUp(self):
        if len(self.teamsPlayedThisRound) == len(self.teams):
            return True
        for team1 in self.teams:
            if team1 in self.teamsPlayedThisRound:
                continue
            for team2 in self.teams:
                if team1 == team2:
                    continue
                if team2 in self.teamsPlayedThisRound:
                    continue
                if team1 in self.teamsPlayed[team2] or team2 in self.teamsPlayed[team1]:
                    continue
                self._playgame(team1, team2)
                if self._pairTeamsUp():
                    return True
                self._unplay(team1, team2)

        return False



    def _playRound(self):
        self.teamsPlayedThisRound = []
        self.whoPlayedWhothisRound = {}
        return self._pairTeamsUp()


    def createScedule(self, activities: int) -> str:
        if self.inAction:
            return "cannot create schedule while in action"
        self.inAction = True
        for round in range(1, activities+1):
            if self._playRound():
                roundsCanPlay = round
                print(self.whoPlayedWhothisRound)

        self.inAction = False
        return f"{roundsCanPlay} rounds can be played"




main = ScheduleMaker([i for i in range(1, 9)])
main.createScedule(10)