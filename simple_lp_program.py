from __future__ import print_function
from ortools.linear_solver import pywraplp


def main():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver('simple_lp_program',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # Create the variables x and y.
    #x1 = solver.NumVar(0, 1, 'x1')
    #x2 = solver.NumVar(0, 2, 'x2')
   # x3 = solver.NumVar(0, 3, 'x3')
    x4 = solver.NumVar(0, 4, 'x4')
    x5 = solver.NumVar(0, 5, 'x5')
    print('Number of variables =', solver.NumVariables())

    # Create a linear constraint, ct <= 14.
    ct = solver.Constraint(-solver.infinity(), -1)

    #ct2 = solver.Constraint(0, 1, 'ct2')
    #ct2.SetCoefficient(x1, 1)
    #ct3 = solver.Constraint(0, 1, 'ct3')
    #ct3.SetCoefficient(x2, 1)
    ct4 = solver.Constraint(0, 1, 'ct4')
    ct4.SetCoefficient(x4, 1)
    ct5 = solver.Constraint(0, 1, 'ct5')
    ct5.SetCoefficient(x5, 1)
    #ct6 = solver.Constraint(0, 1, 'ct6')
    #ct6.SetCoefficient(x3, 1)

    #ct.SetCoefficient(x1, 8)
    #ct.SetCoefficient(x2, 7)
    #ct.SetCoefficient(x3, 11)
    ct.SetCoefficient(x4, 6)
    ct.SetCoefficient(x5, 19)
    print('Number of constraints =', solver.NumConstraints())

    # Create the objective function, 3 * x + y.
    objective = solver.Objective()
    #objective.SetCoefficient(x1, 23)
    #objective.SetCoefficient(x2, 19)
   # objective.SetCoefficient(x3, 28)
    objective.SetCoefficient(x4, 14)
    objective.SetCoefficient(x5, 44)
    objective.SetMaximization()

    solver.Solve()

    print('Solution:')
    print('Objective value =', objective.Value())
    #print('x1 =', x1.solution_value())
   # print('x2 =', x2.solution_value())
    #print('x3 =', x3.solution_value())
    print('x4 =', x4.solution_value())
    print('x5 =', x5.solution_value())


if __name__ == '__main__':
    main()