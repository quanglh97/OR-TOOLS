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
   
    X = [[[model.NewIntVar(0, 1, 'X[%i][%i][%i]'%(i, j, k) )for k in range(2*N -2)] for j in range(N)] for i in range(N)]
    #Y = [[[model.NewIntVar(0, 1, 'X[%i][%i][%i]'%(i, j, k) )for k in range(2*N -2)] for j in range(N)] for i in range(N)]
    
    #[end model]

    #[start constraints]
    for i in range(N):
        NumSN = 0
        NumSK = 0
        for j in range(N):
            for k in range(2*N -2):
                if i == j:
                    NumSN += X[i][j][k]
                if i != j:
                    NumSK += X[i][j][k]
                    if(X[i][j][k] == 1):
                        model.Add(X[j][j][k] == 1)
                        for h in range(N):
                            if (h!=i) and (h!=j):
                                model.Add(X[h][j][k] == 0)

        model.Add(NumSN == N-1)
        model.Add(NumSK == N-1)
    
        model.Add(sum(X[i][j][k] for j in range(N) for k in range(2*N -2)) == 2*N -2)
        for k in range(2*N -2):
            model.Add(sum(X[i][j][k] for j in range(N))==1)
        
    #[end constraints]

    #[ham muc tieu]
    F = []
    for i in range(N):
        F.append(0)
        for k in range(2*N -3):
            for j1 in range(N):
                if X[i][j1][k] == 1:
                    F[i] +=sum(X[i][j2][k+1]*d[j1][j2] for j2 in range(N))
        model.Minimize(F[i])


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



