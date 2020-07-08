class SecureList:
    def __init__(self, messages: list):
        self.__messages = []
        for message in messages:
            self.__messages.append(message)

    def __str__(self):
        s = str(self.__messages)
        self.__messages.clear()
        return s

    def __getitem__(self, item: int):
        s = self.__messages[item]
        del self.__messages[item]
        return s

    def __repr__(self):
        s = str(self.__messages)
        self.__messages.clear()
        return f"{s}"

    def __len__(self):
        return len(self.__messages)
