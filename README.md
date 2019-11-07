# 16-Puzzle-AI-Project-
-Given: A intital 4x4 state containing numbers 1-14 and 2 zeros (the zeros indicate blank spaces), and a goal state  <br />
EX: <br />
9 13 7 4<br />
12 3 0 1<br />
2 0 5 6<br />
14 10 11 8<br />

-Output: the least amount of actions to reach from the initial state to the goal state  <br />
The output will be in this format:  <br />
9 3 13 4  <br />
2 7 1 0  <br />
10 12 0 5  <br />
14 11 8 6  <br />
 <br />
9 3 13 4  <br />
2 7 1 0  <br />
10 12 0 5  <br />
14 11 8 6  <br />
 <br />
14  <br />
80  <br />
D2 R2 R2 U2 U1 L1 D1 L1 D1 R1 U1 R1 R1 L2  <br />
14 14 14 14 14 14 14 14 14 14 14 14 14 14 14  <br />
<br />
-The first grid represents the final state of the intial state after reaching the goal  <br />
-The second grid represents the goal state  <br />
-14 is the depth of the tree  <br />
-80 is the total number of nodes (states) generated  <br />
(D2 R2 ....) represents the actions  <br />
    -EX: D2 = move the seond blank down, R2 = move the second blank right, U1 = move the first blank up  <br />
-(14 14 ...) represents the f(n) values calculated for the state in each action  <br />
f(n) = g(n) + h(n)  <br />
g(n) = depth of the state  <br />
h(n) = Manhatten Distance   <br />

## Read instructions.pdf for more information 
