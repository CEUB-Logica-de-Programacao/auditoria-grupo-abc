from collections import Counter

def etapa1(id):
    idListado = sorted(list(str(id)))
    soma = 101
    
    if int(id) < 1:
        return soma
        
    if len(idListado) > 0 and len(idListado) < 4:
        for x in range(0, 4-len(idListado) ):
            idListado.insert(0, "0")
            
    if len(idListado) == 4:
        index0 = int(idListado[0]+idListado[3])
        index1 = int(idListado[1]+idListado[2])
        soma = index0 + index1
        
    return soma


def etapa2(arr):
    arrAscend = sorted(arr)
    result = []
    
    if max(arr) < len(arrAscend):
        for x in range(1, len(arrAscend)):
            if (x + 1) not in arrAscend:
                result.append(x+1)
        
    else:
        for x in range(1, max(arr)):
            if (x + 1) not in arrAscend:
                result.append(x+1)
                
    return result


def etapa3(senha):
    senhaSeparada = list(senha)
    chars = list(Counter(senhaSeparada).values())
    
    if all(element == chars[0] for element in chars):
        return True
    else:
        return False

if __name__ == "__main__":
    if etapa1(1230) > 100:
            print('ID inválido')
            exit(1)
    if len(etapa2([1, 2,3,4,5,6,7,8,9])) > 0:
        print('Voto inválido')
        exit(1)
    if not etapa3('abba'):
        print('Senha inválida')
        exit(1)
