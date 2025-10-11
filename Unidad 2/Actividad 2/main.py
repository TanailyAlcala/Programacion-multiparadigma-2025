# TANAILY ALCALA BARRAZA 21100152


# CLASE PRODUCTO: 

class Producto:
    
    def __init__(self, nombre: str, precio: float):
        # atributo pub
        self.nombre = nombre
        
        # atributo priv
        self.__stock = 0 
        
        # Atributo protegido 
        self._precio = 0.0
        
        # Usamos el setter para validar el precio inicial
        self.precio = precio 

    # --- Propiedades Getters y Setters ---

    @property
    def stock(self) -> int:
        """Getter para __stock: permite leer el valor privado."""
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        """Setter para __stock: no permite valores negativos."""
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print(f"⚠️ Error: El stock de '{self.nombre}' no puede ser negativo.")

    @property
    def precio(self) -> float:
        """Getter para _precio: permite leer el valor protegido."""
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float):
        """Setter para _precio: valida que el precio sea positivo."""
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser un valor positivo.")

    # --- metodos especiales Dunder Methods ---
    
    def __str__(self) -> str:
        """Representación legible para el usuario (usada por print())."""
        return f"Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock}"

    def __eq__(self, other) -> bool:
        """Compara si dos productos son iguales (basado en el nombre)."""
        if isinstance(other, Producto):
            return self.nombre.lower() == other.nombre.lower()
        return False

# CLASE INVENTARIO
class Inventario:
    
    def __init__(self):
        # atributo priv para almacenar los productos 
        self.__productos = {}

    def agregar_producto(self, producto: Producto):
        """
        Agrega o actualiza un producto en el inventario. Si ya existe, 
        actualiza su stock.
        """
        nombre_clave = producto.nombre.lower()
        
        # verifica si ya existe en el diccionario privv
        if nombre_clave in self.__productos:
            # ai existe se actualiza el stock sumándole el stock del nuevo objeto
            producto_existente = self.__productos[nombre_clave]
            producto_existente.stock = producto_existente.stock + producto.stock
            print(f"🔄 Stock actualizado para '{producto.nombre}'. Nuevo stock: {producto_existente.stock}")
        else:
            # si no existe, lo agrega al diccionario
            self.__productos[nombre_clave] = producto
            print(f"✅ Producto '{producto.nombre}' agregado al inventario.")

    def buscar_producto(self, nombre: str) -> Producto | None:
        """Busca un producto por nombre y lo retorna, o None si no existe."""
        return self.__productos.get(nombre.lower())

    def total_valor_inventario(self) -> float:
        """Calcula el valor monetario total de todo el inventario (Precio * Stock)."""
        valor_total = sum(p.precio * p.stock for p in self.__productos.values())
        return valor_total

    # --- metodos especiales Dunder Methods ---

    def __len__(self) -> int:
        """Retorna el número de productos únicos en el inventario (usado por len())."""
        return len(self.__productos)

    def __str__(self) -> str:
        """Lista todos los productos del inventario en formato legible."""
        if not self.__productos:
            return "El inventario está vacío."
        
        productos_str = "--- Inventario Actual ---\n"
        for producto in self.__productos.values():
            productos_str += f"  - {producto}\n"
        productos_str += f"-------------------------\nTotal de productos únicos: {len(self)}\n"
        
        return productos_str


# =================================================================
if __name__ == "__main__":
    print("--- 1. Inicialización y Agregación de Productos ---")
    almacen = Inventario()

    # creación de Productos
    laptop = Producto("Laptop X1", 1200.50)
    mouse = Producto("Mouse", 25.00)
    teclado = Producto("Teclado Mecánico", 75.99)
    # se crea un producto con el mismo nombre para probar la actualización en agregar_producto
    mouse_adicional = Producto("Mouse", 25.00) 

    # modificar stock inicial
    laptop.stock = 10
    mouse.stock = 50
    teclado.stock = 20
    mouse_adicional.stock = 5 # aqui se sumará al 'Mouse' ya existente

    almacen.agregar_producto(laptop)
    almacen.agregar_producto(mouse)
    almacen.agregar_producto(teclado)
    # 'mouse_adicional' se sumará al 'mouse'
    almacen.agregar_producto(mouse_adicional) 

    print(f"\nNúmero total de productos únicos en inventario: {len(almacen)}")
    print(almacen) # uso de Inventario.__str__

    # -------------------------------------------------------------
    print("--- 2. Manipulación y Búsqueda ---")
    
    # búsqueda y modificación getter/setter
    prod_laptop = almacen.buscar_producto("Laptop X1")
    if prod_laptop:
        print(f"Estado antes de modificar: {prod_laptop}")
        
        # modifica stock 
        prod_laptop.stock -= 3
        
        # modifica precio
        prod_laptop.precio = 1150.99
        print(f"Estado después de modificar (venta de 3): {prod_laptop}")
        
        # intentar stock inválido (error del setter)
        prod_laptop.stock = -1 

    # -------------------------------------------------------------
    print("\n--- 3. Cálculos y Comparaciones ---")
    
    # uso del método total_valor_inventario
    valor = almacen.total_valor_inventario()
    print(f"El valor total del inventario es: ${valor:,.2f}")

    # uso de Producto.__eq__ para casos de TRUE y FALSE
    mouse_comparacion = almacen.buscar_producto("Mouse")

    # Caso TRUE con mismo nombre: Mouse vs mouse_comparacion
    print(f"\n¿'Mouse' es igual a 'Mouse' (basado en nombre)? {mouse == mouse_comparacion}")
    
    # Caso FALSE con nombres diferentes: Mouse vs Laptop X1
    print(f"¿'Mouse' es igual a 'Laptop X1'? {mouse == laptop}")