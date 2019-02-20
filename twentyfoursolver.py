# Tugas Kecil 1 IF2211 Strategi Algoritma
# Nama  : Leonardo
# NIM   : 13517048
import time #untuk mencatat waktu eksekusi program

def solve(equation): #input1 berupa string
    #fungsi eval adalah primitif untuk menyelesaikan isi string
    try: #try except digunakan untuk mencegah error karena pembagian dengan 0
        epsilon = 10**(-12) #untuk angka-angka jika dibulatkan ke angka 24
        if (eval(equation) >= (24-epsilon) and eval(equation) <= (24+epsilon)):
            #mencetak string equation ke layar apabila
            #hasil perhitungan adalah 24
            print(equation)
            return 1
        else : return 0
    except ZeroDivisionError:
        #apabila ada pembagian dengan 0, dianggap bukan solusi
        return 0

def count_solution(a, b, c, d):
    op = ['+', '-', '*', '/'] #semua jenis operator
    solutions = 0
    #solusi dengan pengurungan 2 angka
    for i in range(4):
        for j in range(4):
            for k in range(4):
                list_equation = ['(', a, op[i], b, ')', op[j] , '(', c, op[k] , d, ')']
                equation = ''.join(list_equation)
                solutions += solve(equation)

    #solusi dengan pengurungan di dalam pengurungan         
    for i in range(4):
        for j in range(4):
            for k in range(4):
                list_equation = ['(', '(', a, op[i], b, ')', op[j], c, ')', op[k] , d]
                equation = ''.join(list_equation)
                solutions += solve(equation)

    for i in range(4):
        for j in range(4):
            for k in range(4):
                list_equation = ['(', a, op[i], '(', b, op[j], c, ')', ')', op[k] , d]
                equation = ''.join(list_equation)
                solutions += solve(equation)
                
    for i in range(4):
        for j in range(4):
            for k in range(4):
                list_equation = [a, op[i], '(', '(', b, op[j], c, ')', op[k] , d, ')']
                equation = ''.join(list_equation)
                solutions += solve(equation)

    for i in range(4):
        for j in range(4):
            for k in range(4):
                list_equation = [a, op[i], '(', b, op[j], '(', c, op[k] , d, ')', ')']
                equation = ''.join(list_equation)
                solutions += solve(equation)

    return solutions

if __name__ == '__main__': #main program
    #diasumsikan input pengguna selalu valid
    inp = [0 for i in range(4)]
    inp[0] = str(input("angka ke-1 : "))
    inp[1] = str(input("angka ke-2 : "))
    inp[2] = str(input("angka ke-3 : "))
    inp[3] = str(input("angka ke-4 : "))
    print()
    start = time.time()
    #menghitung semua kemungkinan kombinasi angka
    how_many = 0
    #melakukan implementasi if untuk mencegah 2 solusi atau
    #lebih yang sama apabila ada 2 atau lebih input sama
    if (inp[0] == inp[1] == inp[2] == inp[3]):
        how_many += count_solution(inp[0], inp[0], inp[0], inp[0])
    elif (inp[0] == inp[1] == inp[2]):
        how_many += count_solution(inp[0], inp[0], inp[0], inp[3])
        how_many += count_solution(inp[0], inp[0], inp[3], inp[0])
        how_many += count_solution(inp[0], inp[3], inp[0], inp[0])
        how_many += count_solution(inp[3], inp[0], inp[0], inp[0])
    elif (inp[0] == inp[1] == inp[3]):
        how_many += count_solution(inp[0], inp[0], inp[0], inp[2])
        how_many += count_solution(inp[0], inp[0], inp[2], inp[0])
        how_many += count_solution(inp[0], inp[2], inp[0], inp[0])
        how_many += count_solution(inp[2], inp[0], inp[0], inp[0])
    elif (inp[0] == inp[2] == inp[3]):
        how_many += count_solution(inp[0], inp[0], inp[0], inp[1])
        how_many += count_solution(inp[0], inp[0], inp[1], inp[0])
        how_many += count_solution(inp[0], inp[1], inp[0], inp[0])
        how_many += count_solution(inp[1], inp[0], inp[0], inp[0])
    elif (inp[1] == inp[2] == inp[3]):
        how_many += count_solution(inp[1], inp[1], inp[1], inp[0])
        how_many += count_solution(inp[1], inp[1], inp[0], inp[1])
        how_many += count_solution(inp[1], inp[0], inp[1], inp[1])
        how_many += count_solution(inp[0], inp[1], inp[1], inp[1])
    elif (inp[0] == inp[1]):
        if (inp[2] == inp[3]):
            how_many += count_solution(inp[0], inp[0], inp[2], inp[2])
            how_many += count_solution(inp[0], inp[2], inp[0], inp[2])
            how_many += count_solution(inp[0], inp[2], inp[2], inp[0])
            how_many += count_solution(inp[2], inp[0], inp[0], inp[2])
            how_many += count_solution(inp[2], inp[2], inp[0], inp[0])
            how_many += count_solution(inp[2], inp[0], inp[2], inp[0])
        else:
            how_many += count_solution(inp[0], inp[0], inp[2], inp[3])
            how_many += count_solution(inp[0], inp[2], inp[0], inp[3])
            how_many += count_solution(inp[0], inp[2], inp[3], inp[0])
            how_many += count_solution(inp[2], inp[0], inp[0], inp[3])
            how_many += count_solution(inp[2], inp[3], inp[0], inp[0])
            how_many += count_solution(inp[2], inp[0], inp[3], inp[0])
            how_many += count_solution(inp[0], inp[0], inp[3], inp[2])
            how_many += count_solution(inp[0], inp[3], inp[0], inp[2])
            how_many += count_solution(inp[0], inp[3], inp[2], inp[0])
            how_many += count_solution(inp[3], inp[0], inp[0], inp[2])
            how_many += count_solution(inp[3], inp[2], inp[0], inp[0])
            how_many += count_solution(inp[3], inp[0], inp[2], inp[0])
    elif (inp[0] == inp[2]):
        if (inp[1] == inp[3]):
            how_many += count_solution(inp[0], inp[0], inp[1], inp[1])
            how_many += count_solution(inp[0], inp[1], inp[0], inp[1])
            how_many += count_solution(inp[0], inp[1], inp[1], inp[0])
            how_many += count_solution(inp[1], inp[0], inp[0], inp[1])
            how_many += count_solution(inp[1], inp[1], inp[0], inp[0])
            how_many += count_solution(inp[1], inp[0], inp[1], inp[0])
        else:
            how_many += count_solution(inp[0], inp[0], inp[1], inp[3])
            how_many += count_solution(inp[0], inp[1], inp[0], inp[3])
            how_many += count_solution(inp[0], inp[1], inp[3], inp[0])
            how_many += count_solution(inp[1], inp[0], inp[0], inp[3])
            how_many += count_solution(inp[1], inp[3], inp[0], inp[0])
            how_many += count_solution(inp[1], inp[0], inp[3], inp[0])
            how_many += count_solution(inp[0], inp[0], inp[3], inp[1])
            how_many += count_solution(inp[0], inp[3], inp[0], inp[1])
            how_many += count_solution(inp[0], inp[3], inp[1], inp[0])
            how_many += count_solution(inp[3], inp[0], inp[0], inp[1])
            how_many += count_solution(inp[3], inp[1], inp[0], inp[0])
            how_many += count_solution(inp[3], inp[0], inp[1], inp[0])
    elif (inp[0] == inp[3]):
        if (inp[1] == inp[2]):
            how_many += count_solution(inp[0], inp[0], inp[1], inp[1])
            how_many += count_solution(inp[0], inp[1], inp[0], inp[1])
            how_many += count_solution(inp[0], inp[1], inp[1], inp[0])
            how_many += count_solution(inp[1], inp[0], inp[0], inp[1])
            how_many += count_solution(inp[1], inp[1], inp[0], inp[0])
            how_many += count_solution(inp[1], inp[0], inp[1], inp[0])
        else:
            how_many += count_solution(inp[0], inp[0], inp[1], inp[2])
            how_many += count_solution(inp[0], inp[1], inp[0], inp[2])
            how_many += count_solution(inp[0], inp[1], inp[2], inp[0])
            how_many += count_solution(inp[1], inp[0], inp[0], inp[2])
            how_many += count_solution(inp[1], inp[2], inp[0], inp[0])
            how_many += count_solution(inp[1], inp[0], inp[2], inp[0])
            how_many += count_solution(inp[0], inp[0], inp[2], inp[1])
            how_many += count_solution(inp[0], inp[2], inp[0], inp[1])
            how_many += count_solution(inp[0], inp[2], inp[1], inp[0])
            how_many += count_solution(inp[2], inp[0], inp[0], inp[1])
            how_many += count_solution(inp[2], inp[1], inp[0], inp[0])
            how_many += count_solution(inp[2], inp[0], inp[1], inp[0])
    elif (inp[1] == inp[2]):
        how_many += count_solution(inp[1], inp[1], inp[0], inp[3])
        how_many += count_solution(inp[1], inp[0], inp[1], inp[3])
        how_many += count_solution(inp[1], inp[0], inp[3], inp[1])
        how_many += count_solution(inp[0], inp[1], inp[1], inp[3])
        how_many += count_solution(inp[0], inp[3], inp[1], inp[1])
        how_many += count_solution(inp[0], inp[1], inp[3], inp[1])
        how_many += count_solution(inp[1], inp[1], inp[3], inp[0])
        how_many += count_solution(inp[1], inp[3], inp[1], inp[0])
        how_many += count_solution(inp[1], inp[3], inp[0], inp[1])
        how_many += count_solution(inp[3], inp[1], inp[1], inp[0])
        how_many += count_solution(inp[3], inp[0], inp[1], inp[1])
        how_many += count_solution(inp[3], inp[1], inp[0], inp[1])
    elif (inp[1] == inp[3]):
        how_many += count_solution(inp[1], inp[1], inp[0], inp[2])
        how_many += count_solution(inp[1], inp[0], inp[1], inp[2])
        how_many += count_solution(inp[1], inp[0], inp[2], inp[1])
        how_many += count_solution(inp[0], inp[1], inp[1], inp[2])
        how_many += count_solution(inp[0], inp[2], inp[1], inp[1])
        how_many += count_solution(inp[0], inp[1], inp[2], inp[1])
        how_many += count_solution(inp[1], inp[1], inp[2], inp[0])
        how_many += count_solution(inp[1], inp[2], inp[1], inp[0])
        how_many += count_solution(inp[1], inp[2], inp[0], inp[1])
        how_many += count_solution(inp[2], inp[1], inp[1], inp[0])
        how_many += count_solution(inp[2], inp[0], inp[1], inp[1])
        how_many += count_solution(inp[2], inp[1], inp[0], inp[1])
    elif (inp[2] == inp[3]):
        how_many += count_solution(inp[2], inp[2], inp[0], inp[1])
        how_many += count_solution(inp[2], inp[0], inp[2], inp[1])
        how_many += count_solution(inp[2], inp[0], inp[1], inp[2])
        how_many += count_solution(inp[0], inp[2], inp[2], inp[1])
        how_many += count_solution(inp[0], inp[1], inp[2], inp[2])
        how_many += count_solution(inp[0], inp[2], inp[1], inp[2])
        how_many += count_solution(inp[2], inp[2], inp[1], inp[0])
        how_many += count_solution(inp[2], inp[1], inp[2], inp[0])
        how_many += count_solution(inp[2], inp[1], inp[0], inp[2])
        how_many += count_solution(inp[1], inp[2], inp[2], inp[0])
        how_many += count_solution(inp[1], inp[0], inp[2], inp[2])
        how_many += count_solution(inp[1], inp[2], inp[0], inp[2])
    else : #semua angka berbeda
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        if (a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d):
                            how_many += count_solution(inp[a], inp[b], inp[c], inp[d])
    print(how_many, "solusi ditemukan")
    end = time.time()
    print("Waktu eksekusi program : ", end-start, "detik")