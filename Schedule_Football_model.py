#[start program]
#[start import]
from __future__ import print_function
from ortools.sat.python import cp_model
#[end import]
def main():
    #[start input]
    with open('Data_Schedule_Foolball.txt')as f:
        N = [int(x) for x in next(f).split()][0]
        print(N)
        #get value
        d = []
        for i in range(N):
            d.append([int(x) for x in next(f).split()])
        print(d)
    f.close()
    #[end input]

    #[start model]
    model = cp_model.CpModel()
    a = model.NewIntVar(0, 2, 'a')
    print("a =",a,'\na.GetVarValueMap=', a.GetVarValueMap(), "\ntype(a)", type(a), "\ntype getvalue:", type(a.GetVarValueMap()))
    #X[i][k]: san ma doi i thi dau tuan k
    #D(X) = 0->n-1
    X = [[model.NewIntVar(0, N-1, 'X[%i][%i]'%(i, k) )for k in range(2*N -2)] for i in range(N)]
    #Y[i][k]: quy dinh doi i da san khach hay san nha tuan k
    #D(Y) = 0-1
    Y = [[model.NewIntVar(0, 1, 'X[%i][%i]' %(i, k)) for k in range(2*N -2)] for i in range(N)]
    #[end model]

    #[start constraints]
    model.Add(sum(Y[i][k] for k in range(2*N-2) for i in range(N)) == N-1)

    for i in range(N):
        for k in range(2*N -2):
            if Y[i][k] == 1:
                model.Add(X[i][k] == i)
            else:
                model.Add(X[i][k]!= i)
            for j in range(N):
                if i != j:
                    if X[i][k] == j:
                        model.Add(X[j][k] == j)
                        for h in range(N):
                            if (i != h) and (j != h):
                                model.Add(X[h][k] != j)
    #[end constraints]

    #[ham muc tieu]
    # for i in range(N):
    #     F = d[X[i][0]][X[i][2*N - 3]] 
    #     for k in range(2*N -3):
    #         F += d[X[i][k]][X[i][k+1]]
    #     model.Minimize(F)

    #[start slover]
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    print(status)
    if status == cp_model.OPTIMAL:
        for i in range(N):
            for k in range(2*N -2):
                print('X[%i][%i] = %d'%(i, k, solver.Value(X[i][k])))

if __name__ == '__main__':
    main()



