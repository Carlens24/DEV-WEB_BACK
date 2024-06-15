# function 02
def soma(a,b):
    s = a * b
    print(s)


soma(22,44)
soma(78, 90)
soma(123,90)

print("-" * 90)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} chegamos a {s}")

soma(22, 45, 67, 6)
soma(2,34,67,876,87)
soma(2024)