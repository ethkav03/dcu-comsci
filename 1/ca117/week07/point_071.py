class Point(object):
    def set_attributes(self, x, y):
        self.x = x
        self.y = y

    def print_attributes(self):
        print(f'x: {self.x:.2f}')
        print(f'y: {self.y:.2f}')

    def reflect(self):
        self.x *= -1
        self.y *= -1
