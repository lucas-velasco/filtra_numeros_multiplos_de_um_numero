'''Faça uma função chamada filtraMultiplos para filtrar os múltiplos de um número n. Sua função deve receber como entrada uma lista de números e um número, e retornar 
   outra lista contendo todos os elementos da lista original que forem divisiveis por n.'''
   
   def filtraMultiplos(lista_numeros,n):
    '''A função retorna outra lista contendo todos os elementos da
       lista orignal que forem divisíveis por n.'''
    l=[]
    i=0
    while i < len(lista_numeros):
        if lista_numeros[i]%n == 0:
            l = l + [lista_numeros[i],]
            
        i= i+1
        
    return l
   
   




