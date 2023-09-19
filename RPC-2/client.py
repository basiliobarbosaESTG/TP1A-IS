import xmlrpc.client

PORT = 8080
HOST = "127.0.0.1"
IP = f"http://{HOST}:{PORT}"
HELP = "[HELP] Introduza o número da função entre 1 e 9 ou \"exit\" para sair:"
FORMAT = 'utf-8'

proxy = xmlrpc.client.ServerProxy(IP)

print(HELP)
run = input()
while(run != "exit"):
    run=int(run)
    if(run == 1):
        print("Introduza o nome:")
        nome = input()
        print("Introduza o cargo:")
        cargo = input().lower()
        print("Introduza o salario:")
        salario = float(input())

        print("%s" % str(proxy.f1(nome, cargo, salario)))
    if(run == 2):
        print("Introduza o nome:")
        nome = input()
        print("Introduza o sexo (M ou F):")
        sexo = input().upper()
        print("Introduza a idade:")
        idade = int(input())

        print("%s" % str(proxy.f2(nome, sexo, idade)))
    if(run == 3):
        print("Introduza o N1:")
        N1 = int(input())
        print("Introduza o N2:")
        N2 = int(input())

        print("%s" % str(proxy.f3(N1,N2)))
    if(run == 4):
        print("Introduza o sexo (M ou F):")
        sexo = input().upper()
        print("Introduza a altura:")
        altura = float(input())

        print("%s" % str(proxy.f4(sexo,altura)))
    if(run == 5):
        print("Introduza a idade:")
        idade = int(input())

        print("%s" % str(proxy.f5(idade)))
    if(run == 6):
        print("Introduza o nome:")
        nome = input()
        print("Introduza o nivel:")
        nivel = input().upper()
        print("Introduza o salario:")
        salario = float(input())
        print("Introduza o número de dependentes:")
        dependentes = int(input())

        print("%s" % str(proxy.f6(nome,nivel,salario,dependentes)))
    if(run == 7):
        print("Introduza a idade:")
        idade = int(input())
        print("Introduza o tempo de serviço:")
        servico = int(input())

        print("%s" % str(proxy.f7(idade,servico)))
    if(run == 8):
        print("Introduza o Saldo Medio:")
        saldo = float(input())

        print("%s" % str(proxy.f8(saldo)))
    if(run == 9):
        print("%s" % str(proxy.f9()))
    
    run = input()