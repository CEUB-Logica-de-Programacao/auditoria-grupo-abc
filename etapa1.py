def idValido():
    id = str(input("Insira o Id: \n"))
    if id.isnumeric():
        idListado = sorted(list(id))
        if len(idListado) == 4:
            index0 = int(idListado[0]+idListado[3])
            index1 = int(idListado[1]+idListado[2])
            
            if (index0 + index1) <= 100:
                return print("Id é valido")
            
    print("Id é invalido")
    
idValido()
