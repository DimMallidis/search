Q1 Notes: For the DFS implementation i use a set to store the visited nodes and
          a stack (which the project offers an implementation of) that holds objects of the form: (node, list of moves it took to get here).

          Using a set for the explored nodes is critical because we need a fast lookup time since we need to check every single time we move, if the node we are considering moving to has been visited before. Also to eliminate the chance of duplicates.

          Every unvisited node pushes its succesor nodes to the stack, in the order the function getSuccessors returns them, meaning they will be the next ones checked out (LIFO).
          "Always explore the most recently discovered node first."

          The final path returned is a list that contains all the actions Pacman takes to reach the goal.

