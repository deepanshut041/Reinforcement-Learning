# Doom Defend the Center

In this projects we'll implementing agents that learns to play **VizDoom Defend the Center** using several Deep Rl algorithms. Vizdoom is a toolkit for developing and comparing reinforcement learning algorithms on doom games. We'll be using pytorch library for the implementation.

<p align="center"><img src="./images/main.gif" height="300px"></p>

## Libraries Used

- vizdoom
- PyTorch
- numpy
- opencv-python
- matplotlib

## About Enviroment

The purpose of this scenario is to teach the agent that killing the monsters is GOOD and when monsters kill you is BAD. In addition, wasting amunition is not very good either. Agent is rewarded only for killing monsters so he has to figure out the rest for himself. Map is a large circle. Player is spawned in the exact center. 5 melee-only, monsters are spawned along the wall. Monsters are killed after a single shot. After dying each monster is respawned after some time.Episode ends when the player dies.

## Actions

- turn left
- turn right
- shoot (attack)

## REWARDS

- +1 for killing a monster
- -1 for death penalty

## Preprocessing And Stacking Frames

Preprocessing Frames is an important step, because we want to reduce the complexity of our states to reduce the computation time needed for training. 

Stacking frames is really important because it helps us to give have a sense of motion to our Neural Network.

Steps:

- Grayscale each of our frames (because color does not add important information ).
- Crop the screen (in our case we remove the part below the player because it does not add any useful information).
- We normalize pixel values.
- Finally we resize the preprocessed frame to (84 * 84).
- Stacking Frames 4 frames together.

## Deep RL Agents

- Deep Q Network(DQN) [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/03_doom_defend_center/doom_defend_center_dqn.ipynb) [**[Download]**](./doom_defend_center_dqn.ipynb).
- Dueling Double DQN [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/03_doom_defend_center/doom_defend_center_ddqn.ipynb) [**[Download]**](./doom_defend_center_ddqn.ipynb).
- Monte Carlo Policy Gradient [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/03_doom_defend_center/doom_defend_center_pg.ipynb) [**[Download]**](./doom_defend_center_pg.ipynb).
- Rainbow [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/03_doom_defend_center/doom_defend_center_rainbow.ipynb) [**[Download]**](./doom_defend_center_rainbow.ipynb).
- Advantage Actor Critic (A2C) [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/03_doom_defend_center/doom_defend_center_a2c.ipynb) [**[Download]**](./doom_defend_center_a2c.ipynb).
- Proximal Policy Gradients(PPO) [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/03_doom_defend_center/doom_defend_center_ppo.ipynb) [**[Download]**](./doom_defend_center_ppo.ipynb).

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