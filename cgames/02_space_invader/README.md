# Atari Space Invaders

In this projects we'll implementing agents that learns to play OpenAi Gym Atari Space Invaders using several Deep Rl algorithms. OpenAI Gym is a toolkit for developing and comparing reinforcement learning algorithms. We'll be using pytorch library for the implementation.
<p align="center"><img src="./images/main.gif" height="300px"></p>

## Libraries Used

- OpenAi Gym
- PyTorch
- numpy
- opencv-python
- matplotlib

## About Enviroment

In this environment, the observation is an RGB image of the screen, which is an array of shape (210, 160, 3) Each action is repeatedly performed for a duration of k frames, where k is uniformly sampled from {2, 3, 4}. Our Target is to maximize our score.

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

- Deep Q Network(DQN) [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/02_space_invader/space_invader_dqn.ipynb) [**[Download]**](./space_invader_dqn.ipynb).
- Dueling Double DQN [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/02_space_invader/space_invader_ddqn.ipynb) [**[Download]**](./space_invader_ddqn.ipynb).
- Monte Carlo Policy Gradient [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/02_space_invader/space_invader_pg.ipynb) [**[Download]**](./space_invader_pg.ipynb).
- Rainbow [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/02_space_invader/space_invader_rainbow.ipynb) [**[Download]**](./space_invader_rainbow.ipynb).
- Advantage Actor Critic (A2C) [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/02_space_invader/space_invader_a2c.ipynb) [**[Download]**](./space_invader_a2c.ipynb).
- Proximal Policy Gradients(PPO) [**[Preview]**](https://github.com/deepanshut041/Reinforcement-Learning/blob/master/cgames/02_space_invader/space_invader_ppo.ipynb) [**[Download]**](./space_invader_ppo.ipynb).

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