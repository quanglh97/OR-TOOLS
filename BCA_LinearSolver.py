from __future__ import print_function
from ortools.linear_solver import pywraplp

def create_data_model():
  """Create the data for the example."""
  data = {}
  Number_teacher = 3
  Number_Class = 13
  Time_Class = [3, 3, 4, 3, 4, 3, 3, 3, 4, 3, 3, 4, 4]
  Class_for_Teacher = [[0, 2, 3, 4, 8, 10],[0, 1, 3, 5, 6, 7, 8 ],[1, 2, 3, 7, 9, 11, 12]]

  data['weights'] = weights
  data['values'] = values
  data['items'] = list(range(len(weights)))
  data['num_items'] = len(weights)
  num_bins = 5
  data['bins'] = list(range(num_bins))
  data['bin_capacities'] = [100, 100, 100, 100, 100]
  return data

def main():
    N = 0
    M = 0
    anpha = 10
    beta = 30
    MH_GV = []
    T_MH = []
    I = []
    J = []

    # [START input]
    with open('BCA.txt') as f:
        N, M = [int(x) for x in next(f).split()]  # read first line
        print('N = ', N, 'M = ', M)
        # Get value
        for i in range(N):
            MH_GV.append([int(x) for x in next(f).split()])
        for x in next(f).split():
            T_MH.append(int(x))

        for line in f:
            a, b = ([int(x) for x in line.split()])
            I.append(a)
            J.append(b)
        print('Mon hoc giao vien: ', MH_GV, '\n', 'Tiet mon hoc: ', T_MH, '\n', 'Bo xung dot: ', I, '\n', J)
    # [END input]

    # Create mip solver with the CBC backend
    solver = pywraplp.Solver('BCA_LinearSolver', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # Variables
    # x[i, j] = 1 if the teacher i is in class j
    x = {}
    for i in range(N):
        for j in range(M):
