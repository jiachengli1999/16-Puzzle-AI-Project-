# 16-Puzzle-AI-Project-
-Given: A intital 4x4 state containing numbers 1-14 and 2 zeros (the zeros indicate blank spaces), and a goal state
-Output: the least amount of actions to reach from the initial state to the goal state
The output will be in this format:
9 3 13 4
2 7 1 0
10 12 0 5
14 11 8 6

9 3 13 4
2 7 1 0
10 12 0 5
14 11 8 6

14
80
D2 R2 R2 U2 U1 L1 D1 L1 D1 R1 U1 R1 R1 L2
14 14 14 14 14 14 14 14 14 14 14 14 14 14 14

-The first grid represents the final state of the intial state after reaching the goal
-The second grid represents the goal state
-14 is the depth of the tree
-80 is the total number of nodes (states) generated
(D2 R2 ....) represents the actions
  -EX: D2 = move the seond blank down, R2 = move the second blank right, U1 = move the first blank up
-(14 14 ...) represents the f(n) values calculated for the state in each action
f(n) = g(n) + h(n)
g(n) = depth of the state
h(n) = Manhatten Distance 
