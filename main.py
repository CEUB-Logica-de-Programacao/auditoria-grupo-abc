from collections import Counter

def etapa1(id):
    idListado = sorted(list(id))
    if len(idListado) == 4:
        index0 = int(idListado[0]+idListado[3])
        index1 = int(idListado[1]+idListado[2])

        if (index0 + index1) <= 100:
            return True
            
    return False


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
    if etapa1('1234') > 100:
            print('ID inválido')
            exit(1)
    if len(etapa2([1, 1])) > 0:
        print('Voto inválido')
        exit(1)
    if not etapa3('abba'):
        print('Senha inválida')
        exit(1)
