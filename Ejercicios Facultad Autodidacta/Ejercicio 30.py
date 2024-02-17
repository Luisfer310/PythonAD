# Elimina duplicados de una lista
lista1 = ['Luis','Mara', 'Juan', 'Luis', 'Nelson']
lista_sin_duplicados = list(set(lista1)) # Lo que se hizo es que convertiremos nuestra lista en un set, debido a que los sets, acomodan por orden y no aceptan duplicados. Y este
# set lo tendremos dentro de un convertidor de lista para que ya que este ordenado y sin duplicados lo regrese a lista.
print(lista_sin_duplicados)