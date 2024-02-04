import random
import sqlite3
from sqlite3 import Error
import pandas as pd
from sqlalchemy import create_engine

number_of_rows = 500_000

def generate_data():
	rows = []
	alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZAEIOUAEOI"
	numero = 0
	print("Creando informacion de censo...")
	for i in range(500_000):
		aumento = random.randint(1,2)
		numero += aumento
		letras = random.sample(alfabeto, 5)
		nombre = "".join(letras)
		edad = random.randint(18,99)
		impuestos = random.choice((True, True, True, False))
		rows.append([numero, nombre, edad, impuestos])
		if len(rows) % 100_000 == 0:
			print("Creados", len(rows), "registros")
	print("Informacion de censo creada.")
	return rows

def generate_data_base(rows):
	print("Creando base de datos sqlite...")
	df =pd.DataFrame(rows, columns= ['ID', 'nombre', 'edad', 'impuesto'])
	engine = create_engine('sqlite:///censo.db')
	df.to_sql('usuarios', con=engine, index=False, if_exists='replace')
	print("Base de datos sqlite creada")

if __name__ == "__main__":
	rows = generate_data()
	generate_data_base(rows)
