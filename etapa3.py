def senha():
    senha = str(input("Insira a senha: "))
    senhaSeparada = list(senha)
    chars = list(Counter(senhaSeparada).values())
    
    return all(element == chars[0] for element in chars)
  
  senha()
