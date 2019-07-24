# Cricket Match Simulation
Simulating a cricket match scenario provided in the [problem statement](./code%20problem.pdf) using weighted random number generation based on probability

## Installing
Download / clone the repository, setup a virtualenv ( recommended to avoid package dependency conflicts ) and install the requirements using [pip](https://pip.pypa.io/en/stable/)
```
git clone git@github.com:manishbhatias/cricket-match-simulation.git
cd cricket-match-simulation
virtualenv .
pip install -r requirements.txt
```

You can also use the package manager [pip](https://pip.pypa.io/en/stable/) to install cricketmatch_simulator module.

```bash
pip install cricketmatch_simulator
```

## Usage
The default parameters provided in the [problem statement](./code%20problem.pdf) have already been setup so that we can run it directly in the cloned directory using
```bash
python cricketmatch_simulator
```

You can also import the module into your own code and setup different match parameters for simulation
```python
from cricketmatch_simulator import CricketMatchSimulator

# Setup match parameters according to problem and call simulate
simulator = CricketMatchSimulator(40, 4, ["Kirat Boli", "N.S Nodhi", "R Rumrah", "Shashi Henra"])
simulator.simulate()
simulator.print_result()
```

## Sample Output
```bash
4 overs left. 40 runs to win
0.1 Kirat Boli scores 1 run
0.2 N.S Nodhi scores 0 runs
0.3 N.S Nodhi scores 2 runs
0.4 N.S Nodhi scores 1 run
0.5 Kirat Boli scores 6 runs
0.6 Kirat Boli scores 3 runs
3 overs left. 27 runs to win
1.1 Kirat Boli scores 1 run
1.2 N.S Nodhi scores 1 run
1.3 Kirat Boli scores 4 runs
1.4 Kirat Boli scores 3 runs
1.5 N.S Nodhi Out!
1.6 R Rumrah scores 1 run
2 overs left. 17 runs to win
2.1 R Rumrah scores 2 runs
2.2 R Rumrah scores 0 runs
2.3 R Rumrah scores 4 runs
2.4 R Rumrah scores 1 run
2.5 Kirat Boli scores 2 runs
2.6 Kirat Boli Out!
1 overs left. 8 runs to win
3.1 R Rumrah scores 2 runs
3.2 R Rumrah scores 2 runs
3.3 R Rumrah Out!

Bengaluru lost by 4 runs

N.S Nodhi - 4 (5 balls)
Kirat Boli - 20 (8 balls)
Shashi Henra - 0* (0 balls)
R Rumrah - 12 (8 balls)
```

## To do

- [ ] Refactor  player's logic into ts own class
- [ ] Allow setting up more match parameters such as team names, player probabliities etc.

## Built with
- [Numpy](https://numpy.org/)
