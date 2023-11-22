
auto1 = ["volante", "ruedas", "asiento", "puertas"]
auto2 = ["baul", "motor", "vidrios", "espejos"]

auto_completo = auto1 + auto2
print(len(auto_completo))  # Lee los 8 elementos de la lsita
print(auto_completo[2:6])  # Imprime del indice 2 al 6

# Agregando ambas listas en una :
# print(auto1 + auto2)

# Agregar Ruedas al ultimo de auto2
auto2.append("Ruedas")
print(auto2)

# usando if (si volante esta dentro de auto1 imprime: yes)
if "volante" in auto1:
    print("Yes")
