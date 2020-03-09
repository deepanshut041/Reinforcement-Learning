# 3D Balance Ball

In this projects we'll implementing agents that learns to play Unity 3D Balance Ball using several Deep Rl algorithms. Unity Ml Agents is a toolkit for developing and comparing reinforcement learning algorithms. We'll be using pytorch library for the implementation.

<p align="center"><img src="./images/main.png"></p>

## Libraries Used

- Unity Ml Agents
- PyTorch
- numpy
- matplotlib

## About Enviroment

- **Set-up:** A balance-ball task, where the agent balances the ball on it's head.
- **Goal:** The agent must balance the ball on it's head for as long as possible.
- **Agents:** The environment contains 12 agents of the same kind, all using the same Behavior Parameters.
- **Agent Reward Function:**
    1. +0.1 for every step the ball remains on it's head.
    2. -1.0 if the ball falls off.
- **Behavior Parameters:**
    1. **Vector Observation space:** 8 variables corresponding to rotation of the agent cube, and position and velocity of ball.
    2. **Vector Observation space (Hard Version):** 5 variables corresponding to rotation of the agent cube and position of ball.
    3. **Vector Action space:** (Continuous) Size of 2, with one value corresponding to X-rotation, and the other to Z-rotation.
    4. **Visual Observations: None.**
- **Float Properties:** Three
    1. **scale:** Specifies the scale of the ball in the 3 dimensions (equal across the three dimensions)
        - **Default:** 1
        - **Recommended Minimum:** 0.2
        - **Recommended Maximum:** 5
    2. **gravity:** Magnitude of gravity
        - **Default:** 9.81
        - **Recommended Minimum:** 4
        - **Recommended Maximum:** 105
    3. **mass:** Specifies mass of the ball
        - **Default:** 1
        - **Recommended Minimum:** 0.1
        - **Recommended Maximum:** 20
- **Benchmark Mean Reward:** 100

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