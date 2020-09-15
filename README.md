# smdp
implementation of smdp with options with a restricted initiation set

repository contents:
  1. valueIteration file = generic solver 
  2. setUp = primitive and landmark option setup, option space setup
    basics in setUp = used for landmarkOptionSetUp.py
  3. executive = transition, reward, and option space functions used in option value iteration
  4. tests = test files for option set up, value iteration, and value iteration functions (transition, reward, optionSpace)
  5. drawHeatMap.py = visualization (heat map) of policy resulting from value iteration
          drawHeatMap.py produces the visualization for Fig.2 in the "Between MDPs and semi=MDPs: A framework for temporal abstraction in reinforcement learning" paper

*note: initial setUp and value iteration run on semi-MDP options are run using the generic value iteration solver
