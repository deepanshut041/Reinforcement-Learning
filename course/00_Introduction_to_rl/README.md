# An introduction to Reinforcement Learning
Reinforcement learning is the study of agents that act in an environment with the goal of maximizing cumulative reward signals. The agent is not told which actions to take but discovers which actions yield most rewards by trying them. Its actions also may affect not only the immediate rewards but rewards for the next situations.

## Subelements of Reinforcement Learning
A reinforcement learning problem can be divided into four subelements: policy, reward function, value function, and a model.
 - **Reward**: A reward is a scalar feedback signal it indicates how well the agent is doing at step t. The agent’s sole objective is to maximize the total reward it receives over the long run.
    - A Reward is a real-valued response to an action.
    - The reward signal is the primary basis for altering the policy. 
    - **R(s)** indicates the reward for simply being in the state **S**.
    - **R(S,a)** indicates the reward for being in a state **S** and taking an action **a**.
    - **R(S, a, S')** indicates the reward for being in a state **S**, taking an action **a** and ending up in a state **S'**.
 - **Policy**:  It is agent behavior function or simply agent's behavior. The policy is a mapping from perceived states of the environment to actions to be taken when in those states or simply it maps the action to state.
    - A policy is a solution to the Markov Decision Process.
    - A policy is a set of actions that are taken by the agent to reach a goal.
    - It indicates the action **a** to be taken while in state **S**.
    - There are two types of policy Deterministic and Stochastic.
 - **Value Function**: It is a prediction of future reward. The value of a state is the total amount of reward an agent can expect to accumulate over the future, starting from that state. Used to evaluate the goodness and badness of a state. 
 - **Model**: A model predicts what environment will do next. Models are used for planning, by which we mean any way of deciding on a course of action by considering possible future situations before they are actually experienced.
    - A Model (sometimes called Transition Model) gives an action’s effect in a state. In particular, **T(S, a, S')** defines a transition **T** where being in state **S** and taking an action **a** takes us to state **S'** (**S** and **S'** may be same).
    - For stochastic actions (noisy, non-deterministic) we also define a probability **P(S’|S,a)** which represents the probability of reaching a state **S'** if action **a** is taken in state **S**.
    - Methods for solving reinforcement learning problems that use models and planning are called model-based methods, as opposed to simpler model-free methods.

## Markov Decision Processes

### Markov Processes

 - **Markov property**: Once the current state is known, the history of information encountered so far may be thrown away, and that state is a sufficient statistic that gives us the same characterization of the future as if we have all the history.
<p align="center"><strong>P[S<sub>t+1</sub> | S<sub>t</sub>] = P[S<sub>t+1</sub> | S<sub>1</sub>, S<sub>2</sub> .......... S<sub>t</sub>]</strong></p>

 - **Transition probability**:  It’s a probability distribution over next possible successor states, given the current state, i.e. the agent is in some state, there is a probability to go to the first state, and another probability to go to the second state and so on.

 - **State transition matrix**: It defines transition probabilities from all state **S** to successor state **S'**. 

A Markov process is a memory-less random process, i.e. a sequence of random states **S<sub>1</sub>**, **S<sub>2</sub>**, ..... with the Markov property. A Markov process or Markov chain is a tuple **(S, P)** on state space **S**, and transition function **P**. The dynamics of the system can be defined by these two components **S** and **P**.

### Markov Reward Process
A Markov Reward Process or an MRP is a Markov process with value judgment, saying how much reward accumulated through some particular sequence that we sampled. An MRP is a tuple **(S, P, R)** where **S** is a finite state space, **P** is the state transition probability function, **R** is a reward function where it says how much immediate reward we expect to get from state **S** at the moment.
<p align="center"><strong>R<sub>s</sub> = [R<sub>t+1</sub> | S<sub>t</sub> = S]</strong></p>

There is the notion of the return **G<sub>t</sub>**, which is the total discounted rewards from time step **t**. This is what we care about, the goal is to maximise this return
<p align="center">
  <img float="center" src="./images/discounted_reward.png" height="100px"/>
</p>

**γ** is a discount factor, where **γ** ∈ [0, 1]. It informs the agent of how much it should care about rewards now to rewards in the future. If (**γ** = 0), that means the agent is short-sighted, in other words, it only cares about the first reward. If (**γ** = 1), that means the agent is far-sighted, i.e. it cares about all future rewards.

### Markov Decision Process
It decomposes scenarios as a series of states, connected by actions and associated to a specific reward. In MDPs, an AI agent can transition from state to state by selecting an action and obtaining the corresponding rewards. MDPs aim to help AI agents to find the optimal policy in a target environment. Policies are defined by the action an AI agent takes on a specific state. The objective of MDP policies is to maximize the future return from the AI agent. 

* Policy learning focuses on directly inferring a policy that maximizes the reward on a specific environment.  The AI agent would try to infer a strategy to develop the pieces in a way that can achieve the certain well-known position. 
* Value learning tries to quantify the value of every state-action pair. The AI agent would assign a value to every position and select the moves that score higher.






