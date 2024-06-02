import os 
os.system("cls")
import json

datos_empresas = [
    {"rut": "72642413-6", "nombre": "Comercial Calcetas Runner", "ventas": 150000000},
    {"rut": "76437473-2", "nombre": "Reparación Mac", "ventas": 300000000},
    {"rut": "76254356-9", "nombre": "ProgramaSoftware", "ventas": 27500000},
    {"rut": "76077262-3", "nombre": "Calzados Roma", "ventas": 15000000},
    {"rut": "76310800-8", "nombre": "Empresa Arcos", "ventas": 80000000},
    {"rut": "76283690-4", "nombre": "Casino Coffe", "ventas": 120000000},
    {"rut": "76952985-5", "nombre": "Cafe Express ltda", "ventas": 50000000},
    {"rut": "76081440-2", "nombre": "Vino Export SA", "ventas": 20000000},
    {"rut": "76216579-1", "nombre": "Cepa Merl LTDA", "ventas": 30000000},
    {"rut": "76597875-0", "nombre": "Comercial Ropa America", "ventas": 60000000},
    {"rut": "76852106-3", "nombre": "Empresas JP", "ventas": 90000000},
    {"rut": "76887745-8", "nombre": "Empresas ICata SA", "ventas": 100000000},
    {"rut": "76210124-2", "nombre": "Buses Peñalolen", "ventas": 150000000},
    {"rut": "76802052-4", "nombre": "Sandias Paine LTDA", "ventas": 70000000},
    {"rut": "76575973-1", "nombre": "Modas Junior P", "ventas": 400000000},
    {"rut": "76869384-2", "nombre": "Bar del 81", "ventas": 25000000},
    {"rut": "76877803-6", "nombre": "Empresas LLS", "ventas": 8000000},
    {"rut": "76706124-0", "nombre": "Empresas luz y vida SA", "ventas": 3000000},
    {"rut": "76162938-1", "nombre": "Empresa Matrix", "ventas": 120000000},
]

for empresa in datos_empresas:
    ventas = empresa["ventas"]
    if ventas <= 100000000:
        clasificacionEmpresas = "pequeño contribuyente"
    elif 100000001 <= ventas <= 200000000:
        clasificacionEmpresas = "mediano contribuyente"
    else:
        clasificacionEmpresas = "gran contribuyente"
    
    empresa["clasificacionEmpresa.json"] = clasificacionEmpresas


with open("segmentacionEmpresas.json", "w") as archivo:
    json.dump(datos_empresas,archivo)