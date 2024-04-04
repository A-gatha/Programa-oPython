print("---------------------------")
print("VERIFICADOR DE ANO BISSEXTO")
print("---------------------------")


try:  
    ano = int(input("Escreva um ano para verificação:"))
    caractere_especial = "(!@#$%^&*()-_=+[]{}|;:,.<>?/~`)"

    if ano < 1 and ano == caractere_especial:
        raise ValueError("Erro na execução")

    def ano_bissexto(ano_verificado):
        if (ano_verificado % 4 == 0 and ano_verificado % 100 != 0) or (ano_verificado % 400 == 0):
            return True
        else:
            return False

    def saber_seculo(ano_verificado):
        if ano_verificado <= 100:
            return "I"

        elif ano_verificado <= 200 and ano_verificado > 100:
            return  "II"

        elif ano_verificado <= 300 and ano_verificado > 200:
            return  "III"

        elif ano_verificado <= 400 and ano_verificado > 300:
            return  "IV"

        elif ano_verificado <= 500 and ano_verificado > 400:
            return  "V"

        elif ano_verificado <= 600 and ano_verificado > 500:
            return  "VI"

        elif ano_verificado <= 700 and ano_verificado > 600:
            return  "VII"

        elif ano_verificado <= 800 and ano_verificado > 700:
            return  "VIII"

        elif ano_verificado <= 900 and ano_verificado > 800:
            return  "IX"

        elif ano_verificado <= 1000 and ano_verificado > 900:
            return  "X"
        
        elif ano <= 1100 and ano > 1000:
            return  "XI"

        elif ano <= 1200 and ano > 1100:
            return  "XII"

        elif ano <= 1300 and ano > 1200:
            return "XIII"

        elif ano <= 1400 and ano > 1300:
            return "XIV"

        elif ano <= 1500 and ano > 1400:
            return "XV"

        elif ano <= 1600 and ano > 1500:
            return "XVI"

        elif ano <= 1700 and ano > 1600:
            return "XVII"
        
        elif ano <= 1800 and ano > 1700:
            return "XVIII"

        elif ano <= 1900 and ano > 1800:
            return "XVIX"
        
        elif ano <= 2000 and ano > 1900:
            return "XX" 

        elif ano <= 2024 and ano > 2000:
            return "XXI"   
        
        else:
            return " inválido ou ainda ocorrerá no futuro"
    
    if ano_bissexto(ano):
        print(f"O ano verificado é bissexto, e ele se passa no século {saber_seculo(ano)}")
    
    else:
        print(f"O ano verificado não é bissexto, e ele se passa no século {saber_seculo(ano)}")

except ValueError as erro:
    print(erro)