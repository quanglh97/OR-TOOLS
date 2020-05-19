from __future__ import print_function
from ortools.linear_solver import pywraplp

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

     # Create the mip solver with the CBC backend.
    solver = pywraplp.Solver('simple_mip_program',
                           pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    #Da san nha
    x=[[[solver.IntVar(0, 1, 'x[%i][%i][%i]'%(i, j, t))for t in range(2*N -1)]for j in range(N)]for i in range(N)]
    #Da san khach
    y=[[[solver.IntVar(0, 1, 'y[%i][%i][%i]'%(i, j, t))for t in range(2*N -1)]for j in range(N)]for i in range(N)]
    #Bien xac dinh di chuyen
    F=[[[[solver.IntVar(0,1, 'F[%i][%i][%i][%i]'%(i, j, k, t))for t in range(2*N-2)]for k in range(N)]for j in range(N)]for i in range(N)]
    #Bien quang duong cua i
    D=[solver.IntVar(0, solver.infinity(), 'D[%i]'%(i))for i in range(N)]
    
    #[Constraints]
    for i in range(N):
        for j in range(N):
            if i != j:
                # i vs j 1 lan duy nhat tren san i
                solver.Add(sum(x[i][j][t] for t in range(2*N -1))== 1)
                #i vs j 1 lan duy nhat tran san j
                solver.Add(sum(y[i][j][t] for t in range(2*N -1))== 1)
            for t in range(2*N -1):
                #x[i][i][t] = 0 y[i][i][t] = 0
                if i == j:
                    solver.Add(x[i][j][t] == 0)
                    solver.Add(y[i][j][t] == 0)
                #Rang buoc san khach san nha
                solver.Add(x[i][j][t] == y[j][i][t])  
            for k in range(N):
                for t in range(2*N -2):
                    #2 tran lien tiep i da tren san nha
                    if i == j and i == k:
                        solver.Add(2*F[i][j][k][t] >= sum(x[i][h][t]for h in range(N)) + sum(x[i][h][t+1] for h in range(N))-1)
                        solver.Add(2*F[i][j][k][t] <= sum(x[i][h][t]for h in range(N)) + sum(x[i][h][t+1] for h in range(N)))
                    #tran dau san nha, tran sau san khach
                    if i == j and i != k:
                        solver.Add(2*F[i][j][k][t] >= sum(x[i][h][t]for h in range(N))+y[i][k][t+1]-1)
                        solver.Add(2*F[i][j][k][t] <= sum(x[i][h][t]for h in range(N))+y[i][k][t+1])
                    #tran dau san khach, tran sau san nha
                    if i !=j and i == k:
                        solver.Add(2*F[i][j][k][t] >= y[i][j][t]+sum(x[i][h][t+1]for h in range(N))-1)
                        solver.Add(2*F[i][j][k][t] <= y[i][j][t]+sum(x[i][h][t+1]for h in range(N)))
                    #2 tran san khach
                    if i !=j and i != k:
                        solver.Add(2*F[i][j][k][t] >= y[i][j][t] + y[i][k][t+1] -1)
                        solver.Add(2*F[i][j][k][t] <= y[i][j][t] + y[i][k][t+1])              
        for t in range(2*N -1):
            #moi tuan chi da 1 tran vs moi i
            solver.Add(sum((x[i][j][t]+y[i][j][t])for j in range(N))==1)
        #Tinh khoang cach
        solver.Add(D[i] == sum(F[i][j][k][t]*d[j][k] for j in range(N) for k in range(N) for t in range(2*N -2)))

    #Ham muc tieu
    solver.Minimize(solver.Sum(D))

    status = solver.Solve()
    print('status:' ,status, pywraplp.Solver.OPTIMAL, pywraplp.Solver.INFEASIBLE)

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for i in range(N):
            for j in range(N):
                for t in range(2*N-1):
                    print(x[i][j][t].name(), '=', x[i][j][t].solution_value())
    else:
        print('problem does not have an optimal solution')

if __name__ == '__main__':
  main()



    







