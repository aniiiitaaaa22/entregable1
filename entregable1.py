class Maquina:
    def __init__(self, precio, stock, modelo, empresa):
        self._precio = precio
        self._stock = stock
        self._modelo = modelo
        self._empresa = empresa

    def __str__(self):
        return f"Modelo: {self._modelo}\nPrecio: {self._precio}\nStock: {self._stock}\nEmpresa: {self._empresa}"

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):
        self._stock = nuevo_stock

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    @property
    def empresa(self):
        return self._empresa

    @empresa.setter
    def empresa(self, nueva_empresa):
        self._empresa = nueva_empresa


class DesfibriladorHospitalario(Maquina):
    def __init__(self, precio, stock, modelo, empresa, energia_maxima):
        super().__init__(precio, stock, modelo, empresa)
        self._energia_maxima = energia_maxima

    def __str__(self):
        return super().__str__() + f"\nEnergía Máxima: {self._energia_maxima}"


class MaquinaElectrocardiografia(Maquina):
    def __init__(self, precio, stock, modelo, empresa, num_derivaciones):
        super().__init__(precio, stock, modelo, empresa)
        self._num_derivaciones = num_derivaciones

    def __str__(self):
        return super().__str__() + f"\nNúmero de Derivaciones: {self._num_derivaciones}"


class ResonanciaMagnetica(Maquina):
    def __init__(self, precio, stock, modelo, empresa, intensidad_campo):
        super().__init__(precio, stock, modelo, empresa)
        self._intensidad_campo = intensidad_campo

    def __str__(self):
        return super().__str__() + f"\nIntensidad de Campo Magnético (Tesla): {self._intensidad_campo}"


