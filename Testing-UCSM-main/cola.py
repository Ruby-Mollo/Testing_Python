class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return "Cola vacia"

    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return "Vacia Cola"

    def tamano(self):
        return len(self.items)