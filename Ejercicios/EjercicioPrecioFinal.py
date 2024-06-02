DESC = 36 / 100

precioInicial = float(input("Ingrese el precio = "))
descuento = precioInicial * DESC 
precioFinal = precioInicial - descuento

print(f"El precio inicial de = {precioInicial:.0f} se le aplica descuento de 36% y quedaria en = COP ${precioFinal:.1f}")