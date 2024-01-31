
texto = input ("dame un texto ")
repeticiones = input("cuantas veces se repetira: ")

salida = ""
for i in range(int(repeticiones)):
	salida += texto

print(f"::set-output name=output_text::{salida}")

