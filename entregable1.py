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
        return f"Modelo: {self._modelo}\nPrecio: {self._precio}\nStock: {self._stock}\nEmpresa: {self._empresa}"

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
        return super().__str__() + f"\nEnergía Máxima: {self._energia_maxima}"
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
        return super().__str__() + f"\nNúmero de Derivaciones: {self._num_derivaciones}"
    
    def editar_informacion(self):
        super().editar_informacion()
        nuevo_num_derivaciones = Verificar_flotante("Nuevo número de derivaciones: ")
        self.__num_derivaciones = nuevo_num_derivaciones
class ResonanciaMagnetica(Maquina):
    def __init__(self, precio, stock, modelo, empresa, intensidad_campo):
        super().__init__(precio, stock, modelo, empresa)
        self._intensidad_campo = intensidad_campo
        self.__tipo = 'Resonancia Magnetica'
    def verTipo(self):
        return self.__tipo

    def __str__(self):
        return super().__str__() + f"\nIntensidad de Campo Magnético (Tesla): {self._intensidad_campo}"
   
    def editar_informacion(self):
        super().editar_informacion()
        nuevo_intensidad_campo = Verificar_flotante("Nueva intensidad de campo magnético en teslas: ")
        self._intensidad_campo = nuevo_intensidad_campo
class Sistema:
    def __init__(self):
        self.listaMaquinas = {}
    
    def maquina_existe(self,modelo):
        for i in self.listaMaquinas:
            if i is modelo:
                return True
        return False
    
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
        if opcion is '1':
            while True: 
                tipo_maq = input('seleccione la maquina que desea añadir: \n1.Desfribilador Hospitalario\n2. Maquina Electrocardiografica\n3. Maquina de Resonancia Magnetica')
                if tipo_maq is '1':
                    price_1 = Verificar_entero('el precio')
                    stock_1 = Verificar_entero('el stock')
                    modelo_1 = input('Ingrese modelo de la maquina')
                    empresa_1 = input('Ingrese la empresa fabricante')
                    Energia_Maxima = Verificar_flotante('la energía maxima')
                    maquina_1 = DesfibriladorHospitalario(price_1, stock_1, modelo_1, empresa_1, Energia_Maxima)
                    sistema.listaMaquinas[maquina_1.modelo] = maquina_1

                elif tipo_maq is '2':
                    price_2 = Verificar_entero('el precio')
                    stock_2 = Verificar_entero('el stock')
                    modelo_2 = input('Ingrese modelo de la maquina')
                    empresa_2 = input('Ingrese la empresa fabricante')
                    Num_Derivaciones = Verificar_flotante('el número de derivaciones')
                    maquina_2 = MaquinaElectrocardiografia(price_2, stock_2, modelo_2, empresa_2, Num_Derivaciones)
                    sistema.listaMaquinas[maquina_2.modelo] = maquina_2
                elif tipo_maq is '3':
                    price_3 = Verificar_entero('el precio')
                    stock_3 = Verificar_entero('el stock')
                    modelo_3 = input('Ingrese modelo de la maquina')
                    empresa_3 = input('Ingrese la empresa fabricante')
                    Intensidad_Campo_Magnetico = Verificar_flotante('La intensidad del campo magnetico')
                    maquina_3 = ResonanciaMagnetica(price_3, stock_3, modelo_3, empresa_3, Intensidad_Campo_Magnetico)
                    sistema.listaMaquinas[maquina_3.modelo] = maquina_3
                else:
                    print('seleccione una opción válida(el número)\nReintentando...')
        elif opcion is '2':
            pass
        elif opcion is '3':
            pass
        elif opcion is '4':
            while True:
                edit = input("Editar información de la maquina, seleccione:\n1.Editar precio\n2.editar stock\n3.Editar modelo\n4. editar empresa.")
        elif opcion is '5':
            print('cerrando sistema...')
            break
        else:
            print('Usted ha seleccionado una opción invalida, intente de nuevo.')