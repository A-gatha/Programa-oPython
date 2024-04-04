print('''
___________________________________
   REQUISITOS PARA SENHA FORTE:
-----------------------------------
- Ter pelo menos 8 caracteres 
- Ter pelo menos 1 letra maiúscula
- Ter pelo menos 1 letra minúscula
- Ter pelo menos 1 caractere especial (!@#$%^&*()-_=+[]{}|;:,.<>?/~`)
- Ter pelo menos 1 número
------------------------------------
''')

senha = input("Insira sua nova senha:")

num_caractere = 8
num_maiusculo = 1
num_minusculo = 1
num_caractere_especial = 1

maiusculo_encontrado = sum(1 for Maiusculo in senha if Maiusculo in "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ")
minusculo_encontrado = sum(1 for Minusculo in senha if Minusculo in "abcdefghijklmnopqrstuvwxyz")
c_especial_encontrado = sum(1 for Especial in senha if Especial in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`")

if len(senha) < num_caractere:
    print("Erro na validação da senha, é nescessário ter ao menos 8 caracteres. (Aperte F5 e tente novamente)")
   
elif maiusculo_encontrado < num_maiusculo:
    print("Erro na validação da senha, é necessário ter ao menos uma letra maiuscula. (Aperte F5 e tente novamente)")
   
elif minusculo_encontrado < num_minusculo:
    print("Erro na validação da senha, é necessário ter ao menos uma letra minuscula. (Aperte F5 e tente novamente)")

elif c_especial_encontrado < num_caractere_especial:
    print("Erro na validação da senha, é necessário ter ao menos um carctere especial. (Aperte F5 e tente novamente)")
   
else:
    print("Senha validada!")
    print("___________________________________")

    print("      LOGIN CAIXA ELETRÔNICO       ")
    print("-----------------------------------")
    login_senha = input("Digite sua Senha: ")
    print("___________________________________")

    if login_senha != senha:
        print("Senha incorreta, aperte F5 e tente novamente.")
   
    else:
        saldo = 150

        def valor_saldo():
            print(f"Olá, o seu saldo é de R${saldo}")

        def deposito(v_deposito):
            global saldo
            saldo = saldo + v_deposito
            print(f"Seu Depósito foi realizado com sucesso! Seu saldo atual é de R${saldo}")
        
        def sacar(v_sacar):
            global saldo
            saldo -= v_sacar
            print(f"Saque realizado com sucesso! Seu novo saldo é R${saldo}")
        
        def main():
            print("         CAIXA ELETRÔNICO          ")
            print("-----------------------------------")

            while True:
                print('''
Selecione ação você deseja efetuar:

1 - Verificar Saldo atual
2 - Depositar
3 - Sacar
4 - Sair
                ''')

                try:
                    acao = int(input("Escolha uma ação válida: "))

                except:
                    print("Opção inválida, tente novamente.")
                    continue

                if acao == 1:
                    valor_saldo()
                
                elif acao == 2:
                    deposito(int(input("Digite o valor que será depositado: ")))
                
                elif acao == 3:
                    sacar(int(input("Digite o valor a ser sacado: ")))
                elif acao == 4:
                    print("Obrigado por usar nosso caixa eletrônico!")
                    break
                else:
                    print("Opção inválida, tente novamente.")

        if __name__ == "__main__":
            main()
                        

        