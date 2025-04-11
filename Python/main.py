from Seeders import stock, admins
from Entities import Part
from time import sleep
from datetime import datetime

sales_log = []

def pause(seconds=0.5):
    sleep(seconds)

def find_admin(password):
    return next((admin for admin in admins if admin.password == password), None)

def display_stock():
    print("\nEstoque disponível:")
    for item in stock:
        print(f"ID: {item.id} - {item.name}: {item.quantity} em estoque - R${item.price:.2f}")

def add_part():
    name = input("Digite o nome da nova peça: ")
    quantity = int(input("Digite a quantidade em estoque da nova peça: "))
    price = float(input("Digite o preço da nova peça: "))
    new_id = len(stock) + 1
    stock.append(Part(new_id, name, quantity, price))
    print("Peça adicionada com sucesso!")

def delete_part():
    display_stock()
    product_id = int(input("\nDigite o ID do produto que deseja excluir: "))
    part = next((item for item in stock if item.id == product_id), None)
    
    if not part:
        print("ID do produto não encontrado. Tente novamente.")
        return
    
    confirmation = input(f"Você deseja excluir {part.name}? [S/N]: ").strip().upper()
    if confirmation == 'S':
        stock.remove(part)
        print("Peça excluída com sucesso!")
    else:
        print("Operação cancelada.")

def edit_part():
    display_stock()
    product_id = int(input("\nDigite o ID do produto que deseja editar: "))
    part = next((item for item in stock if item.id == product_id), None)
    
    if not part:
        print("ID do produto não encontrado. Tente novamente.")
        return
    
    options = {1: "Nome", 2: "Quantidade", 3: "Preço"}
    print("\nO que deseja editar?")
    for key, value in options.items():
        print(f"{key} - {value}")
    
    choice = int(input("Escolha uma opção: "))

    match choice:
        case 1:
            part.name = input("Digite o novo nome: ")
        case 2:
            part.quantity = int(input("Digite a nova quantidade: "))
        case 3: 
            part.price = float(input("Digite o novo preço: "))
        case _:
            print("Opção inválida!")
            return
    
    print("Alteração realizada com sucesso!")

def generate_report():
    today = datetime.today()
    sales_today = sum(qtd for date, qtd in sales_log if date.date() == today.date())
    sales_month = sum(qtd for date, qtd in sales_log if date.month == today.month and date.year == today.year)
    sales_year = sum(qtd for date, qtd in sales_log if date.year == today.year)
    
    display_stock()
    print("\nVendas:")
    print(f"Peças vendidas hoje: {sales_today}")
    print(f"Peças vendidas neste mês: {sales_month}")
    print(f"Peças vendidas neste ano: {sales_year}")
    input("\nAperte ENTER para voltar ao menu.")

def validate_quantity(product, quantity):
    if quantity > product.quantity:
        print("Não temos peças o suficiente. Tente novamente.")
        return False
    return True

def purchase_menu():
    while True:
        display_stock()
        product_id = int(input("\nDigite o ID do produto que deseja comprar: "))
        part = next((item for item in stock if item.id == product_id), None)
        
        if not part:
            print("ID do produto não encontrado. Tente novamente.")
            continue
        
        quantity = int(input("Digite a quantidade que deseja comprar: "))
        if not validate_quantity(part, quantity):
            continue
        
        confirmation = input(f"{quantity} adicionados ao carrinho.\nDeseja confirmar a compra? [S/N]: ").strip().upper()
        if confirmation == 'S':
            part.quantity -= quantity
            sales_log.append((datetime.now(), quantity))
            print("Compra feita com sucesso!")
        else:
            print("Compra cancelada.")
        
        choice = input("\n1 - Comprar mais peças\n2 - Logout\nEscolha: ")
        if choice == '2':
            return

def admin_menu():
    while True:
        try:
            choice = int(input("\nOpções:\n1 - Adicionar uma peça\n2 - Ver todas as peças\n3 - Excluir uma peça\n4 - Editar uma peça\n5 - Relatório\n6 - Logout\nEscolha: "))
            options = {1: add_part, 2: display_stock, 3: delete_part, 4: edit_part, 5: generate_report}
            if choice in options:
                options[choice]()
            elif choice == 6:
                return
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

def main():
    while True:
        print("Olá! Seja bem-vindo!")
        pause()
        
        password = input("Digite sua senha: ")
        admin = find_admin(password)
        
        if admin:
            admin_menu()
        else:
            print("Temos peças disponíveis para seu automóvel")
            pause()
            purchase_menu()

if __name__ == "__main__":
    main()
