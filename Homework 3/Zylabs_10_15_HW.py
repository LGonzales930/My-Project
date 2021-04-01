# Lorenzo Gonzales
# ID: 1934789
# Zylabs 10.15 CIS 2348 LAB: Winning team (classes)
# TODO: Define get_win_percentage()
class Team:
    def __init__(self, team_name = 'none', team_wins = 0.00, team_losses = 0.00):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage():
        win_percentage = win_percentage
        win_percentage = team_wins / team_wins + team_losses
        return win_percentage

Team_Cal = Team()
Team_Cal.team_name = input()
Team_Cal.team_wins = int(input())
Team_Cal.team_losses = int(input())
if Team_Cal.team_losses <= Team_Cal.team_wins :
        print('Congratulations, Team', Team_Cal.team_name,'has a winning average!')
else:
        print('Team', Team_Cal.team_name, 'has a losing average.')
Team_Cal.get_win_percentage


