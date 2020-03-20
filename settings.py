class Settings():
    def __init__(self,name):
        self.__name = name

    def __read(self):
        file = []
        try:
            f = open(self.__name)
            lines = f.readline()
            while len(lines) > 0:
                lines = lines.replace("\n", "")
                lines = lines.split("=")
                file.append(lines)
                lines = f.readline()
            f.close()
        except IOError:
            print("File error !")
        return file[:]

    def configurations(self):
        file = self.__read()
        if len(file) == 0:
            return None
        try:
            return (file[0][1], file[1][1], file[2][1])
        except IndexError:
            print("File error!")