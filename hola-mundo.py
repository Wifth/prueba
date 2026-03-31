edad : int = 18
altura : float = 1.8
nom : str = "Carlos"
ape = 'chan'
esVerde : bool = False

print (f"{nom} {ape} tiene {edad} años y su carro {"es" if esVerde else "no es"} verde")

#operador ternario
"""""
es = edad > 18 ? "Mayor edad" : "niño";
es = "Mayor edad" if edad > 18 else "niño"
"""""