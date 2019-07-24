import numpy as np

class CricketMatchSimulator:

    def __init__(self, runs_required, overs_left, players_left):
        # Number of runs
        self.runs = runs_required
        # Number of overs
        self.overs = overs_left
        # List of players
        self.players = players_left
        # Storing the probabilities of 0,1,2,3,4,5,6 and 7 (out) in a dictionary for the given players
        self.player_probability = {
            self.players[0]: [0.05, 0.30, 0.25, 0.10, 0.15, 0.01, 0.09, 0.05],
            self.players[1]: [0.10, 0.40, 0.20, 0.05, 0.10, 0.01, 0.04, 0.10],
            self.players[2]: [0.20, 0.30, 0.15, 0.05, 0.05, 0.01, 0.04, 0.20],
            self.players[3]: [0.30, 0.25, 0.05, 0.00, 0.05, 0.01, 0.04, 0.30]
        }
        self.scorecard = {}
        # List of remaining players (Since 1st two are on field)
        self.remaining_players = self.players[2:]
        self.over = 0
        self.ball = 0

    # Function to change the strike
    def changestrike(self, playing):
        return playing[::-1]

    # Function to generate a weighted random number based on given probabilities using numpy
    def play_ball(self, probs, playing):
        return np.random.choice(np.arange(8), p=probs[playing[0]])

    def print_ball(self, over, ball, player, score):
        if score == 7:
            print(str(over) + "." + str(ball + 1) + " " + str(player) + " Out!")
        else:
            print(str(over) + "." + str(ball + 1) + " " + str(player) + " scores " + str(score) + " run" + "s"[score==1:])

    # Function to print the scorecard for players
    def print_scorecard(self):
        for player in self.scorecard:
            print(player + " - " + str(self.scorecard[player]["Score"]) + "*"[self.scorecard[player]["Out"]:] + " (" + str(
                self.scorecard[player]["Balls"]) + " ball" + "s"[self.scorecard[player]["Balls"] == 1:] + ")")


    def simulate(self):
        # Scores for players, with an out flag
        # If the player hasn't been on the field yet, their scores will not be present here
        self.scorecard = {
            self.players[0]: {"Score": 0, "Balls": 0, "Out": False},
            self.players[1]: {"Score": 0, "Balls": 0, "Out": False}
        }
        # Current players (1st and 2nd on the field)
        playing = [self.players[0], self.players[1]]

        for over in range(self.overs):
            self.over = over
            print(str(self.overs - over) + " overs left. " +
                  str(self.runs) + " runs to win")
            # Loop over number of balls in an over. Assumes only legal balls
            for ball in range(6):
                self.ball = ball
                score = self.play_ball(self.player_probability, playing)
                # Increasing balls played for the player on strike
                self.scorecard[playing[0]]["Balls"] += 1
                # score being 7 means out
                if score != 7:
                    # Reducing number of runs remaining
                    self.runs = self.runs - score
                    # Increasing the score of the player
                    self.scorecard[playing[0]]["Score"] += score
                    # Print the score for that ball
                    self.print_ball(over, ball, playing[0], score)
                    # All required runs made, match won
                    if self.runs <= 0:
                        return
                    # If the no. of runs is odd then change strike
                    if score % 2 != 0:
                        playing = self.changestrike(playing)
                    else:
                        pass
                else:
                    # If score is 7 and the player is out
                    # Set the player status to Out
                    self.scorecard[playing[0]]['Out'] = True
                    self.print_ball(over, ball, playing[0], score)
                    # If all players are out, match lost
                    if len(self.remaining_players) == 0:
                        return
                    else:
                        # Put the next player on strike
                        playing = [self.remaining_players[0], playing[1]]
                        self.scorecard[playing[0]] = {"Score": 0, "Balls": 0, "Out": False}
                        # Remove onstrike player from remaining players list
                        self.remaining_players.remove(self.remaining_players[0])

            # At the end of an over, change strike
            playing = self.changestrike(playing)

    def print_result(self):
        print("")
        # More than given runs made, Bengaluru wins
        if self.runs <= 0:
            print("Bengaluru won by " + str(len(self.remaining_players)) + " wickets and " + str(((self.overs - 1 - self.over) * 6) + (5 - self.ball)) + " balls remaining")
        else:
            print("Bengaluru lost by " + str(self.runs) +
                  " run" + "s"[self.runs == 1:])
        print("")
        self.print_scorecard()