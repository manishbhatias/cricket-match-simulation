# Cricket Match Simulation
Simulating a cricket match scenario provided in the [problem statement](./code%20problem.pdf) using weighted random number generation based on probability

# Installing
```
pip install cricketmatch_simulator
```

I recommend using virtualenv to avoid package dependency issues.

# Usage

```python
from cricketmatch_simulator import CricketMatchSimulator

# Setup match parameters according to problem and call simulate
simulator = CricketMatchSimulator(40, 4, ["Kirat Boli", "N.S Nodhi", "R Rumrah", "Shashi Henra"])
simulator.simulate()
simulator.print_result()
```

# Built with
- [Numpy](https://numpy.org/)
