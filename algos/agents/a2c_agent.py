import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim
import random

class A2CAgent():
    def __init__(self, input_shape, action_size, seed, device, gamma, alpha, beta, update_every, actor_m, critic_m):
        """Initialize an Agent object.
        Params
        ======
            input_shape (tuple): dimension of each state (C, H, W)
            action_size (int): dimension of each action
            seed (int): random seed
            device(string): Use Gpu or CPU
            gamma (float): discount factor
            alpha (float): Actor learning rate
            beta (float): Critic learning rate 
            update_every (int): how often to update the network
            actor_m(Model): Pytorch Actor Model
            critic_m(Model): PyTorch Critic Model
        """
        self.input_shape = input_shape
        self.action_size = action_size
        self.seed = random.seed(seed)
        self.device = device
        self.gamma = gamma
        self.alpha = alpha
        self.beta = beta
        self.update_every = update_every

        # Actor-Network
        self.actor_net = actor_m(input_shape, action_size).to(self.device)
        self.actor_optimizer = optim.Adam(self.actor_net.parameters(), lr=self.alpha)

        # Critic-Network
        self.critic_net = critic_m(input_shape).to(self.device)
        self.critic_optimizer = optim.Adam(self.critic_net.parameters(), lr=self.beta)

        # Memory
        self.log_probs = []
        self.values    = []
        self.rewards   = []
        self.masks     = []
        self.entropies = []

        self.t_step = 0

    def step(self, state, log_prob, entropy, reward, done, next_state):

        state = torch.from_numpy(state).unsqueeze(0).to(self.device)
        
        value = self.critic_net(state)
        
        # Save experience in  memory
        self.log_probs.append(log_prob)
        self.values.append(value)
        self.rewards.append(torch.from_numpy(np.array([reward])).to(self.device))
        self.masks.append(torch.from_numpy(np.array([1 - done])).to(self.device))
        self.entropies.append(entropy)

        self.t_step = (self.t_step + 1) % self.update_every

        if self.t_step == 0:
           self.learn(next_state)
           self.reset_memory()
                
    def act(self, state):
        """Returns action, log_prob, entropy for given state as per current policy."""
        
        state = torch.from_numpy(state).unsqueeze(0).to(self.device)
        action_probs = self.actor_net(state)

        action = action_probs.sample()
        log_prob = action_probs.log_prob(action)
        entropy = action_probs.entropy().mean()

        return action.item(), log_prob, entropy

        
        
    def learn(self, next_state):
        next_state = torch.from_numpy(next_state).unsqueeze(0).to(self.device)
        next_value = self.critic_net(next_state)

        returns = self.compute_returns(next_value, self.gamma)

        log_probs = torch.cat(self.log_probs)
        returns   = torch.cat(returns).detach()
        values    = torch.cat(self.values)

        advantage = returns - values

        actor_loss  = -(log_probs * advantage.detach()).mean()
        critic_loss = advantage.pow(2).mean()

        loss = actor_loss + 0.5 * critic_loss - 0.001 * sum(self.entropies)

        # Minimize the loss
        self.actor_optimizer.zero_grad()
        self.critic_optimizer.zero_grad()
        loss.backward()
        self.actor_optimizer.step()
        self.critic_optimizer.step()

    def reset_memory(self):
        del self.log_probs[:]
        del self.rewards[:]
        del self.values[:]
        del self.masks[:]
        del self.entropies[:]

    def compute_returns(self, next_value, gamma=0.99):
        R = next_value
        returns = []
        for step in reversed(range(len(self.rewards))):
            R = self.rewards[step] + gamma * R * self.masks[step]
            returns.insert(0, R)
        return returns