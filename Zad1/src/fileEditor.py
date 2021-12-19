import os


def isString(word):
    if isinstance(word, str):
        return True
    else:
        raise TypeError('Argument musi być typu string')


class fileEditor:

    def readFile(self, file):
        return file.read()

    def editFile(self, file, text):
        if isString(file) and isString(text):
            with open(file, 'a') as f:
                f.write(text)
                f.close()
            return text

    def deleteFile(self, file):
        if isString(file):
            if os.path.exists(file):
                os.remove(file)
            else:
                raise Exception("Plik nie istnieje")
