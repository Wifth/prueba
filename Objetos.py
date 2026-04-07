""""
    public Perro(string nombre) {
        this.nombre = nombre;
        this.edad = 1;
    }
    public void Ladra(){
        Console.WriteLine($"Guau, tengo {edad}")
    }
    public string ToString(){
        return $"{Soy {this.nombre} y tengo {this.edad} años}";
    }
Perro fido = new Perro("Fido");
"""

class Perro:
    def __init__(self, _nombre=""):
        self.nombre = _nombre
        self.edad = 1
    
    def __str__(self):
        return (f"Soy {self.nombre} y tengo {self.edad} años")

    def ladra(self):
        print(f"Guau, tengo {self.edad}")

fido = Perro("Fido")
print(fido.edad)