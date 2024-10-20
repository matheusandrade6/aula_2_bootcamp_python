#Escreva um programa que calcula a área de um círculo recebendo o raio como entrada
import math 
r = float(input("insira o raio do círculo: "))
area_do_circulo = math.pi * r ** 2
print(f"{area_do_circulo:.2f}") #método de formatação do número com 2 casas decimais