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
 - Deep Q Network(DQN) [**[Preview]**](./pages/space_invader_dqn.html) [**[Download**]](./space_invader_dqn.ipynb)
 - Dueling Double DQN [].
 - Monte Carlo Policy Gradient.
 - TD Actor-Critic.
 - Advantage Actor Critic (A2C).
 - Trust Region Policy Optimization(TRPO)
 - Proximal Policy Gradients(PPO).
 - Deep Deterministic Policy Gradient(DDPG)
 - Twin Delayed DDPG
 - Soft Actor Critic (SAC)



