productos=[]
precio=[]
produprecio=['',]
produpreci=[]
presio=[0,]
def buskarytodoeso():
    print('''q hacer?? :
1.- COMPRAR
2.- BORRAR
3.- TICKET

        ''')
    hacer=int(input('OPCIÓN??? :'))
    
    if hacer==1:
        añadir()
    if hacer==2:
        borrar() 
    if hacer==3:
       suma()

def añadir():   #AÑADIR PRODUKTO Y PRESIO!!!!!!
    añadirpro=input('Nombre del producto :')
    productos.clear()
    productos.append(añadirpro)
    preciopre=int(input('precio? :'))
    presio.append(preciopre)
    precio.clear()
    precio.append(preciopre)
    ola=(f'''{productos} {precio}''')
    produpreci.append(ola)
    adiosadios=len(produpreci)

    print(adiosadios)
    ola=(f'{adiosadios}.-{ola}')

    produprecio.append(ola)
    return añadir

def mostrar():    #NO LO USE AL FINAL :(
    print('\n')
    print(produprecio)

def suma():    #TICKET AERGDFGTQRREG
    print(produprecio)
    ekis=sum(presio)
    print(f'\nPRECIO TOTAL: {ekis}')

def borrar():  
    posicion=int(input('Cuál quieres borrar? Escribe ---EL NÚMERO--- del producto. :'))
    produprecio.pop(posicion)
    presio.pop(posicion)

while True:
    buskarytodoeso()
    salir=input('\n¡¡Enter para continuar, S para salir!!.....\n').upper()
    if salir=='S':
        print(':3  :33')
        print('BAI!! ☺\n')
        break
    else:
        continue
