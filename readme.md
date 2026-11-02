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