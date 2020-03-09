# Walker

In this projects we'll implementing agents that learns to play Unity Walker using several Deep Rl algorithms. Unity Ml Agents is a toolkit for developing and comparing reinforcement learning algorithms. We'll be using pytorch library for the implementation.

<p align="center"><img src="./images/main.png"></p>

## Libraries Used

- Unity Ml Agents
- PyTorch
- numpy
- matplotlib

## About Enviroment

- Set-up: Physics-based Humanoids agents with 26 degrees of freedom. These DOFs
  correspond to articulation of the following body-parts: hips, chest, spine,
  head, thighs, shins, feet, arms, forearms and hands.
- Goal: The agents must move its body toward the goal direction as quickly as
  possible without falling.
- Agents: The environment contains 11 independent agents with same Behavior Parameters.
- Agent Reward Function (independent):
  - +0.03 times body velocity in the goal direction.
  - +0.01 times head y position.
  - +0.01 times body direction alignment with goal direction.
  - -0.01 times head velocity difference from body velocity.
- Behavior Parameters:
  - Vector Observation space: 215 variables corresponding to position, rotation,
    velocity, and angular velocities of each limb, along with goal direction.
  - Vector Action space: (Continuous) Size of 39, corresponding to target
    rotations applicable to the joints.
  - Visual Observations: None
- Float Properties: Four
  - gravity: Magnitude of gravity
    - Default: 9.81
    - Recommended Minimum:
    - Recommended Maximum:
  - hip_mass: Mass of the hip component of the walker
    - Default: 15
    - Recommended Minimum: 7
    - Recommended Maximum: 28
  - chest_mass: Mass of the chest component of the walker
    - Default: 8
    - Recommended Minimum: 3
    - Recommended Maximum: 20
  - spine_mass: Mass of the spine component of the walker
    - Default: 10
    - Recommended Minimum: 3
    - Recommended Maximum: 20
- Benchmark Mean Reward: 1000

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