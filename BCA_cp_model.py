#[START program]
#[START import]
from __future__ import print_function

from ortools.sat.python import cp_model
#[END import]


def main():

    N = 0
    M = 0
    anpha = 10
    beta = 17
    MH_GV = []
    T_MH = []
    I = []
    J = []

    #[START input]
    with open('BCA.txt') as f:
        N, M = [int(x) for x in next(f).split()]  # read first line
        print('N = ',N,'M = ', M)
        # Get value
        for i in range(N):
            MH_GV.append([int(x) for x in next(f).split()])
        for x in next(f).split():
            T_MH.append(int(x))

        for line in f:
            a, b = ([int(x) for x in line.split()])
            I.append(a)
            J.append(b)
        print('Mon hoc giao vien: ',MH_GV, '\n','Tiet mon hoc: ', T_MH, '\n','Bo xung dot: ', I, '\n', J)
    #[END input]

    #[START model]
    model = cp_model.CpModel()
    # X[i, j] la giao vien i day mon j vs X[i,j] = {0,1}
    X = [[model.NewIntVar(0, 1, 'x%i%i' % (i, j)) for j in range(M)] for i in range(N)]
    # Ham muc tieu
    #f = model.NewIntVar(0, M*5, 'f')

    #[START contraints]
    # Giao vien i giang day mon j trong danh sach hop le
    for i in range(N):
        for j in range(M):
            found = False
            for k in MH_GV[i]:
                if j == k:
                    found = True
            if found == False:
                model.Add(X[i][j] == 0)

    # Rang buoc xung dot mon hoc
    for k in range(I.__len__()):
        for i in range(N):
            model.Add(X[i][I[k]] + X[i][J[k]] <= 1)

    # Moi mon hoc chi 1 giao vien giang day
    for j in range(M):
        model.Add(sum(X[i][j]for i in range(N)) == 1)

    # Rang buoc ham muc tieu
    F = []
    for i in range(N):
        model.Add(sum(X[i][j]*T_MH[j] for j in range(M)) >= anpha)
        model.Add(sum(X[i][j]*T_MH[j] for j in range(M)) <= beta)
        F.append(sum(X[i][j]*T_MH[j] for j in range(M)))

    model.Minimize(max(F))
    #[END contraints]
    #[END model]

    #[START slover]
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL:
        for i in range(N):
            for j in range(M):
                print('X%i%i = %d'%(i,j,solver.Value(X[i][j])))

    # if status == cp_model.FEASIBLE:
    #     print(solver.Value(X))

    #[END slover]

#[Class solution]
class SolutionPrinter(cp_model.CpSolverSolutionCallback):
  """Print intermediate solutions."""

  def __init__(self, variables):
    cp_model.CpSolverSolutionCallback.__init__(self)
    self.__variables = variables
    self.__solution_count = 0

  def OnSolutionCallback(self):
    self.__solution_count += 1
    for v in self.__variables:
      print('%s = %i' % (v, self.Value(v)), end = ' ')
    print()

  def SolutionCount(self):
    return self.__solution_count

if __name__ == '__main__':
    main()
