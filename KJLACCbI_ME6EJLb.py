class Furniture:
    'Супер класс Мебель'
#    def test(self):
#        a = 0
class seat(Furniture):
    'Класс сиденья'
    def __init__(self, material, price, weight, count):
        self.material = material
        self.price = price
        self.weight = weight
        self.count = count
    def IIoDC4ET_BECA_CuDEHuY(self):
        BEC_CTyJLbEB_B_3AKA3E = _3AKA3_IIJLACTuKOBbIX_CTyJLbEB.count * _3AKA3_IIJLACTuKOBbIX_CTyJLbEB.weight
        #print("Вес стульев в заказе:", BEC_CTyJLbEB_B_3AKA3E)
        return BEC_CTyJLbEB_B_3AKA3E
    def IIODC4ET_cheni_CTyJLbEB(self):
        chena_CTyJLbEB = _3AKA3_IIJLACTuKOBbIX_CTyJLbEB.count * _3AKA3_IIJLACTuKOBbIX_CTyJLbEB.price
        #print("Стоимость стульев в заказе бдет стоить:", chena_CTyJLbEB)
        return chena_CTyJLbEB

def IIPOBEPKA_3AKA3A_HA_GRy3OIIODbEMHOCTb():
    if(_3AKA3_IIJLACTuKOBbIX_CTyJLbEB.IIoDC4ET_BECA_CuDEHuY() <= GPy3OIIODbEMHOCTb_MAIIIuHbI):
        print("Заказ подходит по весу для вашей машины!")
    else:
        print("Заказ не подходит по весу для вашей машины. Закажите отдельно доставку.")

def _BO3MOZXHOCTb_uCIIOJLHEHu9I_3AKA3A():
    if(_3AKA3_IIJLACTuKOBbIX_CTyJLbEB.count <= OCTATOK_IIJLACTuKOBbIX_CTyJLbEB.count):
        print("Заказ может быть исполнен(на складе хватает продукта)!")
    else:
        print("Заказ не может быть исполнен из-за нехватки продукта ;(")

class storage(Furniture):
    'Класс хранилища'
    def __init__(self, material, price, weight):
        self.material = material
        self.price = price
        self.weight = weight

class beds(Furniture):
    'Класс Мебель для сна'
    def __init__(self, material, price, weight):
        self.material = material
        self.price = price
        self.weight = weight

class surfaces(Furniture):
    'Класс Столы и полки'
    def __init__(self, material, price, weight):
        self.material = material
        self.price = price
        self.weight = weight

print("*** Программа для заказа стульев ***")

#Складские остатки стульев
OCTATOK_IIJLACTuKOBbIX_CTyJLbEB = seat("plastic", 5, 2, 25)
OCTATOK_DEPEB9IHHbIX_CTyJLbEB = seat("wood", 15, 6, 7)
KOJLu4ECTBO_IIJLACTuKOBbIX_CTyJLbEB = int(input('Введите кол-во пластиковых стульев, которое хотите купить '))
GPy3OIIODbEMHOCTb_MAIIIuHbI = int(input('Введите грузопоъёмность вашей машины(в кг) '))

print("*** Вывод исходя из введённых данных ***")

_3AKA3_IIJLACTuKOBbIX_CTyJLbEB = seat("plastic", 5, 2, KOJLu4ECTBO_IIJLACTuKOBbIX_CTyJLbEB)
IIPOBEPKA_3AKA3A_HA_GRy3OIIODbEMHOCTb()
_BO3MOZXHOCTb_uCIIOJLHEHu9I_3AKA3A()
print("Вес стульев в заказе:", _3AKA3_IIJLACTuKOBbIX_CTyJLbEB.IIoDC4ET_BECA_CuDEHuY())
print("Стоимость стульев в заказе будет стоить:", _3AKA3_IIJLACTuKOBbIX_CTyJLbEB.IIODC4ET_cheni_CTyJLbEB())