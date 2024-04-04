while True:

    print("-----------------------------------")
    print("             LOGIN                 ")
    print("-----------------------------------")


    senha = "1234"

    login_senha = input("Digite sua Senha: ")

    print("___________________________________")

    if login_senha == senha:
        print("Senha correta, acesso permitido.")
        break
    
    else:
        print("Senha incorreta, acesso negado. (Tente Novamente)")
        continue