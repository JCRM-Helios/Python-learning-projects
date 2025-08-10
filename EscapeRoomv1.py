# Clase para objetos interactivos
class GameObject:
    def __init__(self, name, appearance, feel, smell):
        self.name = name          # Nombre
        self.appearance = appearance  # Descripción visual
        self.feel = feel          # Descripción táctil
        self.smell = smell        # Descripción olfativa

    def look(self):   # Mirar
        return f"Mirando {self.name}. {self.appearance}\n"

    def touch(self):  # Tocar
        return f"Tocando {self.name}. {self.feel}\n"

    def sniff(self):  # Oler
        return f"Oliendo {self.name}. {self.smell}\n"


# Clase para la habitación
class Room:
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code    # Código correcto
        self.game_objects = game_objects  # Lista de objetos

    def check_code(self, code):  # Verifica código
        return self.escape_code == code

    def get_game_object_names(self):  # Lista de nombres
        return [obj.name for obj in self.game_objects]


# Clase principal del juego
class Game:
    def __init__(self):
        self.attempts = 0  # Intentos usados
        objects = self.create_objects()
        self.room = Room(731, objects)  # Código: 731

    def create_objects(self):  # Crea los objetos
        return [
            GameObject('El suéter',
                'Es un suéter azul que tenía el número 12 cosido.',
                'Alguien ha descosido el segundo número, dejando solo el 1.',
                'El suéter huele a detergente.'),
            GameObject('La silla',
                'Es una silla con solo tres patas.',
                'Alguien ha roto a propósito una de las patas.',
                'Huele a madera vieja.'),
            GameObject('El diario',
                'La última entrada indica que el tiempo debería ser en horas, minutos y segundos.',
                'La tapa está desgastada y varias páginas han sido arrancadas.',
                'Huele a cuero usado.'),
            GameObject('El bol de sopa',
                'Parece ser caldo de pollo.',
                'Se ha enfriado a temperatura ambiente.',
                'Detectas 7 hierbas y especias distintas.'),
            GameObject('El reloj',
                'La manecilla de las horas apunta a la sopa, la de los minutos hacia la silla, y la de los segundos al suéter.',
                'El compartimiento de las pilas está abierto y vacío.',
                'Huele a plástico.')
        ]

    def get_room_prompt(self):  # Menú principal
        prompt = "\nIntroduce el código de 3 dígitos o elige un objeto:\n"
        for i, name in enumerate(self.room.get_game_object_names(), 1):
            prompt += f"{i}. {name}\n"
        return prompt

    def select_object(self, index):  # Interacción con objeto
        selected_object = self.room.game_objects[index]
        interaction = input(f"\n¿Cómo quieres interactuar con {selected_object.name}?\n1. Mirar\n2. Tocar\n3. Oler\nElige (1-3): ")
        
        if interaction == "1":
            print(selected_object.look())
        elif interaction == "2":
            print(selected_object.touch())
        elif interaction == "3":
            print(selected_object.sniff())
        else:
            print("Opción no válida.")

    def take_turn(self):  # Un turno de juego
        print(f"\nIntentos restantes: {3 - self.attempts}")
        selection = input(self.get_room_prompt())
        
        if selection.isdigit() and len(selection) == 3:  # Si es código
            if self.room.check_code(int(selection)):
                print("¡Correcto! Has escapado.")
                return True
            else:
                self.attempts += 1
                print("Código incorrecto.")
                if self.attempts >= 3:
                    print("Sin intentos. Game over.")
                    return True
        elif selection.isdigit() and 1 <= int(selection) <= len(self.room.game_objects):  # Si es objeto
            self.select_object(int(selection) - 1)
        else:
            print("Entrada no válida.")
        
        return False


# Bucle principal
if __name__ == "__main__":
    game = Game()
    game_over = False
    while not game_over:
        game_over = game.take_turn()
