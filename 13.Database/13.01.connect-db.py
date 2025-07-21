import sqlite3 as sqlite

# connection = sqlite.connect("test.db")

connection = sqlite.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("select * from customers")



# result = cursor.fetchall()

# for customer in result:
#     print(f"{customer}\n")


# for customer in result:
#     print(f"{customer[1]}\n")


"""
Output:
(1, 'Luís', 'Gonçalves', 'Embraer - Empresa Brasileira de Aeronáutica S.A.', 'Av. Brigadeiro Faria Lima, 2170', 'São José dos Campos', 'SP', 'Brazil', '12227-000', '+55 (12) 3923-5555', '+55 (12) 3923-5566', 'luisg@embraer.com.br', 3)

(2, 'Leonie', 'Köhler', None, 'Theodor-Heuss-Straße 34', 'Stuttgart', None, 'Germany', '70174', '+49 0711 2842222', None, 'leonekohler@surfeu.de', 5)

(3, 'François', 'Tremblay', None, '1498 rue Bélanger', 'Montréal', 'QC', 'Canada', 'H2G 1A7', '+1 (514) 721-4711', None, 'ftremblay@gmail.com', 3)

...

Luís

Leonie

François

Bjørn

...

"""


# cursor.execute("select * from customers where country = 'Brazil'")
# result = cursor.fetchall()

# for i in result:
#     print(f"{i}\n")


"""
Output:
(1, 'Luís', 'Gonçalves', 'Embraer - Empresa Brasileira de Aeronáutica S.A.', 'Av. Brigadeiro Faria Lima, 2170', 'São José dos Campos', 'SP', 'Brazil', '12227-000', '+55 (12) 3923-5555', '+55 (12) 3923-5566', 'luisg@embraer.com.br', 3)

(10, 'Eduardo', 'Martins', 'Woodstock Discos', 'Rua Dr. Falcão Filho, 155', 'São Paulo', 'SP', 'Brazil', '01007-010', '+55 (11) 3033-5446', '+55 (11) 3033-4564', 'eduardo@woodstock.com.br', 4)

...
"""


# cursor.execute("select * from customers where country = 'Brazil'")
# result = cursor.fetchone()
# print(result)

"""
Output:
(1, 'Luís', 'Gonçalves', 'Embraer - Empresa Brasileira de Aeronáutica S.A.', 'Av. Brigadeiro Faria Lima, 2170', 'São José dos Campos', 'SP', 'Brazil', '12227-000', '+55 (12) 3923-5555', '+55 (12) 3923-5566', 'luisg@embraer.com.br', 3)
"""


sql = "INSERT INTO genres(name) VALUES ('Adventure')"
cursor.execute(sql)
connection.commit()


connection.close()