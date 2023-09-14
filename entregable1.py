def Verificar_entero(entrada):
    while True:
        dato_int = input(f'ingrese {entrada}')
        try:
            return int(dato_int)
        except:
            print('para {entrada} debe ingresar un numero entero.')
            continue
def Verificar_flotante(entrada):
    while True:
        dato_float = input(f'ingrese {entrada}')
        try:
            return float(dato_float)
        except:
            print('para {entrada} debe ingresar un numero entero.')
            continue
class Maquina:
    def __init__(self, precio, stock, modelo, empresa):
        self.__precio = precio
        self.__stock = stock
        self.__modelo = modelo
        self.__empresa = empresa
        self.__tipo = ''

    def __str__(self):
        return f"Modelo: {self.__modelo}\nPrecio: {self.__precio}\nStock: {self.__stock}\nEmpresa: {self.__empresa}"

    def verTipo(self):
        return self.__tipo

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, nueva_empresa):
        self.__empresa = nueva_empresa
    
    def editar_informacion(self):
        edit = input("Editor de información de máquinas, seleccione una opción:\n1.Editar Precio.\n2.Editar Stock\n3.Editar Modelo\n4 Editar Empresa.")

        if edit == "1":
            nuevo_precio = Verificar_flotante("Nuevo Precio: ")
            self.__precio = nuevo_precio
        if edit == "2":
            nuevo_stock = Verificar_flotante("Nuevo stock: ")
            self.__stock = nuevo_stock
        if edit == "3":
            nuevo_mod = Verificar_flotante("Nuevo modelo: ")
            self.__modelo = nuevo_mod
        if edit == "4":
            nuevo_empresa = Verificar_flotante("Nuevo empresa: ")
            self.__empresa = nuevo_empresa
        else:
            print("Opción no válida, por favor seleccione otra opción.")


class DesfibriladorHospitalario(Maquina):
    def __init__(self, precio, stock, modelo, empresa, energia_maxima):
        super().__init__(precio, stock, modelo, empresa)
        self.__energia_maxima = energia_maxima
        self.__tipo = 'Desfibrilador'
    def verTipo(self):
        return self.__tipo
    def __str__(self):
        return super().__str__() + f"\nEnergía Máxima: {self.__energia_maxima}"
    def editar_informacion(self):
        super().editar_informacion()
        nuevo_energia_maxima = Verificar_flotante("Nueva energía Máxima: ")
        self.__energia_maxima = nuevo_energia_maxima

class MaquinaElectrocardiografia(Maquina):
    def __init__(self, precio, stock, modelo, empresa, num_derivaciones):
        super().__init__(precio, stock, modelo, empresa)
        self.__num_derivaciones = num_derivaciones
        self.__tipo = 'Maquina Electrocardiografica'
    def verTipo(self):
        return self.__tipo
    @property
    def ver_NumeroDerivaciones(self):
        return self.__num_derivaciones
    
    @ver_NumeroDerivaciones.setter
    def asignar_NumeroDerivaciones(self, nuevoNumero):
        self.__num_derivaciones = nuevoNumero

    def __str__(self):
        return super().__str__() + f"\nNúmero de Derivaciones: {self.__num_derivaciones}"
    
    def editar_informacion(self):
        super().editar_informacion()
        nuevo_num_derivaciones = Verificar_flotante("Nuevo número de derivaciones: ")
        self.__num_derivaciones = nuevo_num_derivaciones
class ResonanciaMagnetica(Maquina):
    def __init__(self, precio, stock, modelo, empresa, intensidad_campo):
        super().__init__(precio, stock, modelo, empresa)
        self.__intensidad_campo = intensidad_campo
        self.__tipo = 'Resonancia Magnetica'
    def verTipo(self):
        return self.__tipo

    def __str__(self):
        return super().__str__() + f"\nIntensidad de Campo Magnético (Tesla): {self.__intensidad_campo}"
   
    def editar_informacion(self):
        super().editar_informacion()
        nuevo_intensidad_campo = Verificar_flotante("Nueva intensidad de campo magnético en teslas: ")
        self._intensidad_campo = nuevo_intensidad_campo
class Sistema:
    def __init__(self):
        self.listaMaquinas = {}
    
    def maquina_existe(self,modelo):
        for i in self.listaMaquinas:
            if i == modelo:
                return True
        return False
    def mostrar_datos_maquina(self):
        modelo = input("Ingrese el modelo de la maquina: ")
        maquina = self.maquina_existe(modelo)

        if maquina == True:
            print("Datos de la maquina: ")
            print(self.listaMaquinas[modelo])
        else:
            print("No se encontró una maquina con el  modelo {modelo}")
    
    def Eliminar_Maquina(self):
        a = True
        while a == True:
            modelo_maq = input('Ingrese el modelo de la maquina que desea eliminar')
            f = self.maquina_existe(modelo_maq)
            if f:
                del self.listaMaquinas[modelo_maq]
                a = False
                break
            elif f == False:
                print('la maquina no existe en la base de datos')
                continue
    
def main():
    sistema = Sistema()
    while True:
        print("\nMenú de Administración de Máquinas:")
        opcion = input('''Seleccione la opción deseada:\n1.Crear Maquina\n2. Eliminar Máquina\n3. seleccionar Máquina\n4. Editar los datos de un equipo biomedico\n5.salir''')
        if opcion == '1':
            while True: 
                tipo_maq = input('seleccione la maquina que desea añadir: \n1.Desfribilador Hospitalario\n2. Maquina Electrocardiografica\n3. Maquina de Resonancia Magnetica')
                modelo = input('Ingrese modelo de la maquina')
                
                if sistema.maquina_existe(modelo) == True:
                    print('el modelo ingresado ya existe... intente de nuevo')
                    continue
                if sistema.maquina_existe(modelo) == False:
                    pass
                price = Verificar_entero('el precio')
                stock = Verificar_entero('el stock')
                empresa = input('Ingrese la empresa fabricante')

                if tipo_maq == '1':
                    Energia_Maxima = Verificar_flotante('la energía maxima')
                    maquina = DesfibriladorHospitalario(price, stock, modelo, empresa, Energia_Maxima)
                    sistema.listaMaquinas[maquina.modelo] = maquina
                    break

                elif tipo_maq == '2':
                    Num_Derivaciones = Verificar_flotante('el número de derivaciones')
                    maquina = MaquinaElectrocardiografia(price, stock, modelo, empresa, Num_Derivaciones)
                    sistema.listaMaquinas[maquina.modelo] = maquina
                    break
                    
                elif tipo_maq == '3':
                    Intensidad_Campo_Magnetico = Verificar_flotante('La intensidad del campo magnetico')
                    maquina = ResonanciaMagnetica(price, stock, modelo, empresa, Intensidad_Campo_Magnetico)
                    sistema.listaMaquinas[maquina.modelo] = maquina
                    break
                else:
                    print('seleccione una opción válida(el número)\nReintentando...')

        elif opcion == '2':
            sistema.Eliminar_Maquina()

        elif opcion == '3':
            sistema.mostrar_datos_maquina()

        elif opcion == '4': #CÓMO EDITAR LAS PROPIEDADES ESPECIALES DE CADA CLASES PREGUNTAR
            
            while True:
                modelo = input("Ingrese el modelo de la máquina que desea editar: ")
                if sistema.maquina_existe(modelo):
                    maquina = sistema.listaMaquinas[modelo]
                    maquina.editar_informacion()
                    break
                elif sistema.maquina_existe(modelo) == False:
                    print("la maquina no existe en la base de datos, intente de nuevo")
                    continue

        elif opcion == '5':
            print('cerrando sistema...')
            break
        else:
            print('Usted ha seleccionado una opción invalida, intente de nuevo.')

main()