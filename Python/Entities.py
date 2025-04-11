"""
@authors: 
@created_at:

Este arquivo é responsável por criar os objetos do projeto.
"""
class Part:
    def __init__(self, id: int, name: str, quantity: int, price: float):
        self._id = id
        self._name = name
        self._quantity = quantity
        self._price = price

    # Propriedades (Campos que serão alterados)
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def quantity(self):
        return self._quantity
    
    @property
    def price(self):
        return self._price
    
    # Setters (Responsáveis pela alteração do valor das propriedades)
    @id.setter
    def id(self, new_id):
        if (new_id > 0 and isinstance(new_id, int)):
            self._id = new_id
        else:
            print("O campo 'ID' deve ser positivo e flutuante.")

    @name.setter
    def name(self, new_name):
        if (isinstance(new_name, str)):
            self._name = new_name
        else:
            print("O campo 'Nome' deve receber uma string.")

    @quantity.setter
    def quantity(self, new_quantity):
        if (new_quantity > 0):
            self._quantity = new_quantity
        else:
            print("O campo 'Quantidade' deve ser positivo.")

    @price.setter
    def price(self, new_price):
        if (new_price > 0 and isinstance(new_price, float)):
            self._price = new_price
        else:
            print("O campo 'Preço' deve ser positivo e flutuante.")


class Admin:
    def __init__(self, name, password):
        self._name = name,
        self._password = password

    @property
    def name(self):
        return self._name
    
    @property
    def password(self):
        return self._password
    
    @name.setter
    def name(self, new_name):
        if (isinstance(new_name, str)):
            self._name = new_name
        else:
            print("O campo 'Nome' deve receber uma string.")
    
    @password.setter
    def password(self, new_password):
        if (isinstance(new_password, str)):
            self._pasnew_password = new_password
        else:
            print("O campo 'Senha' deve receber uma string.")
    

        

