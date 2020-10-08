# smdp
implementation of semi-Markov Decision Process with options(primitive actions and temporally extended actions towards a designated landmark) with a restricted initiation set

repository contents:
  1. valueIteration file = generic solver 
  2. setUp = primitive and landmark option setup, option space setup
    basics in setUp = used for landmarkOptionSetUp.py
  3. executive = transition, reward, and option space functions used in option value iteration
  4. tests = test files for option set up, value iteration, and value iteration functions (transition, reward, optionSpace)
  5. valueLearning = generate policy for the enviornment described in figure 2 in "Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning"
  6. main = file to generate improved policies (termination improvement for policy generated in valueLearning)
  7. visualization = drawHeatMap.py code and screenshot of the resulting heat map used to model figure 2 in "Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning"
  
    numbers = landmark number relating to the option
    black arrow = primitive option
    blue arrow = primitive option within the policy of the landmark option
    
*note: initial setUp and value iteration run on semi-MDP options are run using the generic value iteration solver
