def calcular_descuento(tasa_cambio, perfiles):
  for perfil, datos in perfiles.items():
    precio_original_dolares = datos['precio_bruto_pesos'] / tasa_cambio
    descuento = precio_original_dolares - datos['precio_venta_dolares']
    porcentaje_descuento = (descuento / precio_original_dolares) * 100
    print(f"Perfil: {perfil}")
    print(f"Precio bruto en pesos: {datos['precio_bruto_pesos']}")
    print(f"Precio de venta en dólares: {datos['precio_venta_dolares']}")
    print(f"Porcentaje de descuento: {porcentaje_descuento:.2f}%")
    print("--------------------")
perfiles = {
  "Chapa 1 m": {"precio_bruto_pesos": 14939, "precio_venta_dolares": 10.8},
  "Perfil 80x40x15x1,6mm": {"precio_bruto_pesos": 10044, "precio_venta_dolares": 4.9},
  "Perfil 100x40x15x1,6mm": {"precio_bruto_pesos": 12357.17, "precio_venta_dolares": 5.5},
  "Perfil 120x50x15x1,6mm": {"precio_bruto_pesos": 14397.34, "precio_venta_dolares": 6.7},
  "Perfil 80x40x15x2mm": {"precio_bruto_pesos": 14303.83, "precio_venta_dolares": 6.0},
  "Perfil 100x40x15x2mm": {"precio_bruto_pesos": 17212.61, "precio_venta_dolares": 6.7},
  "Perfil 120x50x15x1,6mm": {"precio_bruto_pesos": 22683.26, "precio_venta_dolares": 8.3}
  # Agrega más perfiles aquí...
}
tasa_cambio = float(input("Tasa de cambio del día: "))
calcular_descuento(tasa_cambio, perfiles)