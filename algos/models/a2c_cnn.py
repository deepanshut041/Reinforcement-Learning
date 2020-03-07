import torch
import torch.nn as nn
import torch.autograd as autograd 
import torch.nn.functional as F
from torch.distributions import Categorical

class A2CCnn(nn.Module):
    def __init__(self, input_shape, num_actions):
        super(A2CCnn, self).__init__()
        self.input_shape = input_shape
        self.num_actions = num_actions

        self.actor_features = nn.Sequential(
            nn.Conv2d(input_shape[0], 32, kernel_size=8, stride=4),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1),
            nn.ReLU()
        )
        
        self.critic_features = nn.Sequential(
            nn.Conv2d(input_shape[0], 32, kernel_size=8, stride=4),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1),
            nn.ReLU()
        )
        
        self.actor_fc = nn.Sequential(
            nn.Linear(self.actor_feature_size(), 512),
            nn.ReLU(),
            nn.Linear(512, self.num_actions)
        )

        self.critic_fc = nn.Sequential(
            nn.Linear(self.critic_feature_size(), 512),
            nn.ReLU(),
            nn.Linear(512, 1)
        )
        
    def forward(self, x):
        actor_x = self.actor_features(x)
        critic_x = self.critic_features(x)

        actor_x = actor_x.view(actor_x.size(0), -1)
        critic_x = critic_x.view(critic_x.size(0), -1)
        
        probs = self.actor_fc(actor_x)
        value = self.critic_fc(critic_x)
        dist  = Categorical(probs)

        return dist, value
    
    def actor_feature_size(self):
        return self.actor_features(autograd.Variable(torch.zeros(1, *self.input_shape))).view(1, -1).size(1)
    
    def critic_feature_size(self):
        return self.critic_features(autograd.Variable(torch.zeros(1, *self.input_shape))).view(1, -1).size(1)