Q1 Notes: For the DFS implementation i use a set to store the visited nodes and
          a stack (which the project offers an implementation of) that holds objects of the form: (node, path: list of moves it took to get here).

          Using a set for the explored nodes is critical because we need a fast lookup time since we need to check every single time we move, if the node we are considering moving to has been visited before. Also to eliminate the chance of duplicates.

          Every unvisited node pushes its successor nodes to the stack, in the order the function getSuccessors returns them, meaning they will be the next ones checked out (LIFO).
          "Always explore the most recently discovered node first."

          The final path returned is a list that contains all the actions Pacman takes to reach the goal.

Q2 Notes: For the BFS implementation i use a set again to store the visited nodes and now
          a queue (which again the project offers an implementation of) that holds objects of the same form as before: (node, path: list of moves it took to get here).
          Every unvisited node pushes its successor nodes to the back of the queue, in the order the function getSuccessors returns them, meaning they will be checked out last (FIFO).
          "Always explore the oldest discovered node first."

          The only difference between the DFS and BFS implementations is if the data structure being used is a stack or a queue.

Q3 Notes: For the UCS implementation i use a set again to store the visited nodes and now
          a priority queue, which arranges them so the next to be popped is the one with the lowest priority. I make use of that characteristic described in util.py since thats exactly what UCS needs, if the priority is
          set as the accumulated cost to reach the successor from the start node.

Q4 Notes: For the A* search implementation i used the same structure as the UCS implementation, with a set for visited nodes and
          priority queue, with the main difference being the priority now being calculated as the accumulated cost to reach the successor from the start node plus the heuristic cost.

Q5 Notes: The state structure i chose for the corners agent implementation is (Pacman location coordinates, tuple of four boolean variables to show visited or not corners)
          Get start state performs a check to see if Pacman starts at a corner, in which case we need to cast the tuple into a list to mutate it (switch the according boolean variable)
          and then convert it back into a tuple so that it remains hashable for the visited set we used in the above (Q 1-4) algos.

Q6 Notes: For the corners heuristic, i calculate the manhattan distance from Pacman's current
          position to every unvisited corner, and return the max of those. Its admissible since it
          never overestimates (without walls it will take atleast this many steps to get to that corner),
          and it is consistent because the estimates shrink smoothly (by at most 1, each step Pacman takes).

Q7 Notes: For the food heuristic, i calculate the true maze distance from Pacman to every remaining food
          pellet and return the max one. The true maze distance calculation is implemented in a helper
          function called mazeDistance. Using manhattan would not be close enough to the real number of
          steps to reach the goal state so too many nodes would have been expanded. The heuristic is
          admissible since Pacman has to take atleast the shortest path to the furthest pellet to finish the game, if he deviates because theres more food left, the steps are naturally more. Its also
          consistent, since again, when Pacman moves one step, the heuristic will decrease by at most 1.