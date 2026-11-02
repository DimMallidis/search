# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** MY CODE HERE ***"
    start_node = problem.getStartState() # get the start node
    visited = set() # create a set to keep track of visited nodes, important for lookup and to avoid duplicates
    Stack = util.Stack() # stack to implement DFS, since its LIFO

    Stack.push((start_node, []))

    while not Stack.isEmpty():

        # pop current node and path
        current_node, path = Stack.pop()

        # if we have reached the goal state, return the path
        if problem.isGoalState(current_node):
            return path
        
        # add current node to visited, if not already, and add its successors to the stack
        if current_node not in visited:
            visited.add(current_node)
            for next_node, action, cost in problem.getSuccessors(current_node):
                Stack.push((next_node, path + [action]))
    
    #if no path is found, return empty list
    return [] 
    "*** MY CODE HERE ***"

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** MY CODE HERE ***"
    start_node = problem.getStartState() # get the start node
    visited = set() # create a set to keep track of visited nodes, important for lookup and to avoid duplicates
    Queue = util.Queue() # queue to implement BFS, since its FIFO

    Queue.push((start_node, []))

    while not Queue.isEmpty():

        # pop current node and path
        current_node, path = Queue.pop()

        # if we have reached the goal state, return the path
        if problem.isGoalState(current_node):
            return path
        
        # add current node to visited, if not already, and add its successors to the queue
        if current_node not in visited:
            visited.add(current_node)
            for next_node, action, cost in problem.getSuccessors(current_node):
                Queue.push((next_node, path + [action]))

    #if no path is found, return empty list
    return []
    "*** MY CODE HERE ***"

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** MY CODE HERE ***"
    start_node = problem.getStartState() # get the start node
    visited = set() # create a set to keep track of visited nodes, important for lookup and to avoid duplicates
    PriorityQueue = util.PriorityQueue() # priority queue to implement UCS, with the priority being the least accumulated cost

    # we are passing a tuple of (node, path, cost) to the priority queue, with the priority being the cost
    PriorityQueue.push((start_node, [], 0), 0)

    while not PriorityQueue.isEmpty():

        # pop current node, path and cost
        current_node, path, current_cost = PriorityQueue.pop()

        # if we have reached the goal state, return the path
        if problem.isGoalState(current_node):
            return path

        # add current node to visited, if not already, and add its successors to the priority queue
        # make sure to calculatte the new cost for each successor when passing him to the pq
        if current_node not in visited:
            visited.add(current_node)
            for next_node, action, next_cost in problem.getSuccessors(current_node):
                PriorityQueue.push((next_node, path + [action], current_cost + next_cost), current_cost + next_cost)

    #if no path is found, return empty list
    return []
    "*** MY CODE HERE ***"

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
