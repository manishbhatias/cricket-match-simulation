from cricketmatch_simulator import CricketMatchSimulator

# Sample problem parameters
simulator = CricketMatchSimulator(
    40, 4, ["Kirat Boli", "N.S Nodhi", "R Rumrah", "Shashi Henra"])
simulator.simulate()
simulator.print_result()