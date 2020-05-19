""" SImple solve"""
from __future__ import absolute_import
from __future__ import  division
from __future__ import  print_function

from ortools.sat.python import cp_model

def SimpleSatProgam():
    #creatde model
    #[START model]
    model = cp_model.CpModel()
    #[END model]

    #create the variables
    #[START variables]
    num_vals = 3
    x = model.NewIntVar(0, num_vals-1, 'x')
    y = model.NewIntVar(0, num_vals-1, 'y')
    z = model.NewIntVar(0, num_vals-1, 'z')
    #[END variables]

    #creates the constraints
    #[START constraints]
    model.Add(x != y)
    #[END constraints]

    #Creates a solver and solves the model
    #[START solve]
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    #[END solve]

    if status == cp_model.FEASIBLE:
        print('x = %i ' % solver.Value(x))
        print('y = %i ' % solver.Value(y))
        print('z = %i ' % solver.Value(z))

SimpleSatProgam()
#[END program]