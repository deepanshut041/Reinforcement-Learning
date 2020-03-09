# Soccer Twos

In this projects we'll implementing agents that learns to play Unity Soccer Twos using several Deep Rl algorithms. Unity Ml Agents is a toolkit for developing and comparing reinforcement learning algorithms. We'll be using pytorch library for the implementation.

<p align="center"><img src="./images/main.png"></p>

## Libraries Used

- Unity Ml Agents
- PyTorch
- numpy
- matplotlib

## About Enviroment

- Set-up: Environment where four agents compete in a 2 vs 2 toy soccer game.
- Goal:
  - Get the ball into the opponent's goal while preventing
  the ball from entering own goal.
  - Goalie:
- Agents: The environment contains four agents, with the same
  Behavior Parameters : Soccer.
- Agent Reward Function (dependent):
  - +1 When ball enters opponent's goal.
  - -1 When ball enters team's goal.
  - -0.001 Existential penalty.
- Behavior Parameters:
  - Vector Observation space: 336 corresponding to 11 ray-casts forward distributed over 120 degrees (264)
    and 3 ray-casts backward distributed over 90 degrees each detecting 6 possible object types, along with the object's distance.
    The forward ray-casts contribute 264 state dimensions and backward 72 state dimensions.
  - Vector Action space: (Discrete) Three branched actions corresponding to forward, backward, sideways movement,
      as well as rotation.
  - Visual Observations: None
- Float Properties: Two
  - ball_scale: Specifies the scale of the ball in the 3 dimensions (equal across the three dimensions)
    - Default: 7.5
    - Recommended minimum: 4
    - Recommended maximum: 10
  - gravity: Magnitude of the gravity
    - Default: 9.81
    - Recommended minimum: 6
    - Recommended maximum: 20

## Deep RL Agents

## Any questions

If you have any questions, feel free to ask me:

- **Mail**: <a href="mailto:deepanshut041@gmail.com">deepanshut041@gmail.com</a>  
- **Github**: [https://github.com/deepanshut041/Reinforcement-Learning](https://github.com/deepanshut041/Reinforcement-Learning)
- **Website**: [https://deepanshut041.github.io/Reinforcement-Learning](https://deepanshut041.github.io/Reinforcement-Learning) 
- **Twitter**: <a href="https://twitter.com/deepanshut041">@deepanshut041</a>

Don't forget to follow me on <a href="https://twitter.com/deepanshut041">twitter</a>, <a href="https://github.com/deepanshut041">github</a> and <a href="https://medium.com/@deepanshut041">Medium</a> to be alerted of the new articles that I publish

## How to help

- **Clap on articles**: Clapping in Medium means that you really like my articles. And the more claps I have, the more my article is shared help them to be much more visible to the deep learning community.
- **Improve our notebooks**: if you found a bug or **a better implementation** you can send a pull request.