from cola import Cola
import linecache

#trabaja con archivos de texto, separando en cada línea valores por punto y coma.
def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split

class NodeTree():

    def __init__(self, value, other_values=None, description=""):
        self.value = value
        self.other_values = other_values
        self.description = description
        self.left = None
        self.right = None
        self.height = 0


class BinaryTree:

    def __init__(self):
        self.root = None

#calcula la altura de un nodo del arbol
    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def buscar_jedi(self, name):
        def __buscar_jedi(root, name):
            if root is not None:
                if root.value() == name:
                    print("Nombre:", root.value)
                    if root.other_values:
                        print("Ranking:", root.other_values.get("ranking", "-"))
                        print("Specie:", root.other_values.get("specie", "-"))
                        print("Master:", root.other_values.get("master", "-"))
                        print("Lightsaber color:", root.other_values.get("lightsaber color", "-"))
                        print("Birthdate year:", root.other_values.get("birthdate year", "-"))
                    print()
                __buscar_jedi(root.left, name)
                __buscar_jedi(root.right, name)


    def insert_node(self, value, other_values=None):

        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)

#Realiza un recorrido por niveles del árbol e imprime los valores de los nodos.
    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

# Realiza un recorrido inorden del árbol y, para cada nodo, lee un valor adicional desde un archivo 
# y lo imprime junto con el valor del nodo.
    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)

        __inorden_file(self.root, file_name)

#filtra los nodos que tienen un color de sable de luz específico.
    def inorden_file_lightsaber(self, file_name, lightsaber_color):
        def __inorden_file_lightsaber(root, file_name, lightsaber_color):
            if root is not None:
                __inorden_file_lightsaber(root.left, file_name, lightsaber_color)
                value = get_value_from_file(file_name, root.other_values)
                if lightsaber_color in value[4].split('/'):
                    print(root.value, value[4].split('/'))
                __inorden_file_lightsaber(root.right, file_name, lightsaber_color)

        __inorden_file_lightsaber(self.root, file_name, lightsaber_color)

    def inorden_heroe_or_villano(self, is_hero, other_values=None):
        def __inorden_h_v(root, is_hero,  other_values):
            if root is not None:
                __inorden_h_v(root.left, is_hero,  other_values)
                if root.other_values == is_hero and  other_values in root.value.lower():
                    print(root.value)
                __inorden_h_v(root.right, is_hero,  other_values)

        __inorden_h_v(self.root, is_hero, other_values)

    def inorden_start_with(self, cadena):
        def __inorden_start_with(root, cadena):
            if root is not None:
                __inorden_start_with(root.left, cadena)
                if root.other_values is True and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value, root.height)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)

    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.lower().startswith(value.lower()):
                    print(root.value)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value.lower())

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value

            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count

        return __contar(self.root, value)
    
    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count

        return __contar_heroes(self.root)
    

    def contar_villanos(self):
        def __contar_villanos(root):
            count = 0
            if root is not None:
                if root.other_values is False:
                    count = 1
                count += __contar_villanos(root.left)
                count += __contar_villanos(root.right)
            return count

        return __contar_villanos(self.root)

#Lista los nodos de los arboles de manera descendente
    def inorden_descendente(self, root):
        if root is not None:
            self.inorden_descendente(root.right) 
            if root.other_values is True: 
                print(root.value)  
            self.inorden_descendente(root.left)

    def dividir_arbol_heroesyvillanos(self):
        self.arbol_heroes = BinaryTree()
        self.arbol_villanos = BinaryTree()
        self._dividir_arbol_heroesyvillanos(self.root)

    def _dividir_arbol_heroesyvillanos(self, root):
        if root is not None:
            self._dividir_arbol_heroesyvillanos(root.left)
            if root.other_values is True:  # Es heroe
                self.arbol_heroes.insert_node(root.value, True)
            else:
                self.arbol_villanos.insert_node(root.value, False)  # Es villano
            self._dividir_arbol_heroesyvillanos(root.right)

    def inorden_start_with_jedi(self, cadena):
        def __inorden_start_with_jedi(root, cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value is not None and root.value.lower().startswith(cadena.lower()):
                    print("Nombre:", root.value)
                    if root.other_values:
                        print("Ranking:", root.other_values.get("ranking", "-"))
                        print("Specie:", root.other_values.get("specie", "-"))
                        print("Master:", root.other_values.get("master", "-"))
                        print("Lightsaber color:", root.other_values.get("lightsaber color", "-"))
                        print("Birthdate year:", root.other_values.get("birthdate year", "-"))
                    print()
                __inorden_start_with_jedi(root.right, cadena)

        __inorden_start_with_jedi(self.root, cadena.lower())

    def inorden_ranking_jedi_master(self):
        def __inorden_ranking_jedi_master(root):
            if root is not None:
                __inorden_ranking_jedi_master(root.left)
                if root.other_values and "ranking" in root.other_values:
                    ranking = root.other_values["ranking"]
                    if ranking == "jedi master":
                        print("name: ", root.value)
                        print("Ranking:", root.other_values.get("ranking", "-"))
                    print()
                __inorden_ranking_jedi_master(root.right)

        __inorden_ranking_jedi_master(self.root)

    def inorden_jedi_with_greensaber(self):
        def __inorden_jedi_with_greensaber(root):
            if root is not None:
                __inorden_jedi_with_greensaber(root.left)
                if root.other_values and "lightsaber color" in root.other_values:
                    ranking = root.other_values["lightsaber color"]
                    if ranking == "green":
                        print("Name: ", root.value)
                        print("Lightsaber color:", root.other_values.get("lightsaber color", "-"))
                    print()
                __inorden_jedi_with_greensaber(root.right)

        __inorden_jedi_with_greensaber(self.root)


    def listar_jedi_with_master(self):
        def __listar_jedi_with_master(root):
            if root is not None:
                __listar_jedi_with_master(root.left)
                if root.other_values.get("master") != "-":
                    print("Name :", root.value)
                    print("Master:", root.other_values.get("master"))
                    print()
                __listar_jedi_with_master(root.right)

        __listar_jedi_with_master(self.root)


    def mostrar_jedi_specie(self, species):
            def __mostrar_jedi_specie(root):
                if root is not None:
                    __mostrar_jedi_specie(root.left)
                    if root.other_values and "specie" in root.other_values and root.other_values["specie"] in species:
                        print("Name:", root.other_values.get("name", "-"))
                        print("Specie:", root.other_values["specie"])
                        print()
                    __mostrar_jedi_specie(root.right)

            __mostrar_jedi_specie(self.root)

    def listar_jedi_con_guion(self):
        def __listar_jedi_con_guion(root):
            if root is not None:
                __listar_jedi_con_guion(root.left)
                if "-" in root.value:
                    print("Nombre:", root.value)
                    if root.other_values:
                        print("Ranking:", root.other_values.get("ranking", "-"))
                        print("Specie:", root.other_values.get("specie", "-"))
                        print("Master:", root.other_values.get("master", "-"))
                        print("Lightsaber color:", root.other_values.get("lightsaber color", "-"))
                        print("Birthdate year:", root.other_values.get("birthdate year", "-"))
                    print()
                __listar_jedi_con_guion(root.right)

        __listar_jedi_con_guion(self.root)

    def inorden_creatures(self):
        def __inorden_creatures(root):
            if root is not None:
                __inorden_creatures(root.left)
                print("Name:", root.value) if root.other_values else '-'
                print("Defeated by: ", root.other_values.get("defeated by", "-"))
                print()
                __inorden_creatures(root.right)

        __inorden_creatures(self.root)

    def inorden_start_with_creatures(self, cadena):
        def __inorden_start_with_creatures(root, cadena):
            if root is not None:
                __inorden_start_with_creatures(root.left, cadena)
                if root.value is not None and root.value.lower().startswith(cadena.lower()):
                    print("Nombre:", root.value)
                    if root.other_values:
                        print("Defeated by:", root.other_values.get("defeated by", "-"))
                        print("Description:", root.other_values.get("description", "-"))
                        print("Captured by:", root.other_values.get("captured by", "-"))
                    print()
                __inorden_start_with_creatures(root.right, cadena)

        __inorden_start_with_creatures(self.root, cadena.lower())


    def contar_derrotas(self):
        def __contar_derrotas(root, derrota_count):
            if root is not None:
                __contar_derrotas(root.left, derrota_count)
                defeated_by = root.other_values.get("defeated by")
                if defeated_by and defeated_by != "-":
                    if defeated_by in derrota_count:
                        derrota_count[defeated_by] += 1
                    else:
                        derrota_count[defeated_by] = 1
                __contar_derrotas(root.right, derrota_count)

        derrota_count = {}
        __contar_derrotas(self.root, derrota_count)
        return derrota_count

    def maximos_derrotadores(self):
        derrota_count = self.contar_derrotas()
        best_creatures = sorted(derrota_count.items(), key=lambda x: x[1], reverse=True)[:3] # ordena en función del segundo elemento de cada tupla, 
                                                                                            # que es el número de derrotas, ordena de manera descendente(reverse true)
                                                                                            # toma los tres primeros elementos ([:3])
        return best_creatures


    def defeated_by_heracles(self):
        def __defeated_by_heracles(root):
            if root is not None:
                __defeated_by_heracles(root.left)
                if root.other_values and "defeated by" in root.other_values:
                    defeated_by = root.other_values["defeated by"]
                    if defeated_by == "heracles":
                        print("name: ", root.value)
                __defeated_by_heracles(root.right)

        __defeated_by_heracles(self.root)


    def captured_by_heracles(self):
        def __captured_by_heracles(root):
            if root is not None:
                __captured_by_heracles(root.left)
                if root.other_values and "captured by" in root.other_values:
                    defeated_by = root.other_values["captured by"]
                    if defeated_by == "heracles":
                        print("name: ", root.value)
                        print("Defeated by:", root.other_values.get("defeated by", "-"))
                        print("Description:", root.other_values.get("description", "-"))
                        print()
                __captured_by_heracles(root.right)

        __captured_by_heracles(self.root)

    def not_defeated(self):
            def __not_defeated(root):
                if root is not None:
                    __not_defeated(root.left)
                    if root.other_values and "defeated by" in root.other_values:
                        defeated_by = root.other_values["defeated by"]
                        if defeated_by == "-":
                            print("name: ", root.value)
                    __not_defeated(root.right)

            __not_defeated(self.root)

