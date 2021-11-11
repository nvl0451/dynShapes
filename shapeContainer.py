import shape


class ShapeContainer:
    def __init__(self):
        self.size = 0
        self.container = []

    def initRandom(self, _size):
        self.size = int(_size)
        for i in range(self.size):
            self.container.append(shape.Shape())

    def addShape(self, _shapeType, _shapeSides, _shapeDens):
        self.size += 1
        self.container.append(shape.Shape(False, _shapeType, _shapeSides, _shapeDens))

    def shapeRepresent(self, _n):
        return f"{_n + 1}: {self.container[_n].content.representIntoString()}"

    def readFile(self, _fileName):
        inFile = open(_fileName, "r")
        while True:
            line = inFile.readline().split(' ')
            if line == ['']:
                break
            elif line[0] == '1':
                self.addShape(line[0], [line[1], 0, 0], line[2])
            elif line[0] == '2':
                self.addShape(line[0], [line[1], line[2], line[3]], line[4])
            elif line[0] == '3':
                self.addShape(line[0], [line[1], 0, 0], line[2])
        inFile.close()

    def outputContainer(self, _fileName):
        outFile = open(_fileName, "w")
        for i in range(self.size):
            outFile.write(self.shapeRepresent(i))
            outFile.write('\n')
        outFile.close()

    def bubbleSort(self):
        for i in range(self.size - 1):
            for j in range(self.size - i - 1):
                if self.container[j].content.volume > self.container[j + 1].content.volume:
                    temp = self.container[j]
                    self.container[j] = self.container[j+1]
                    self.container[j + 1] = temp