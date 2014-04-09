
class StatementWithItemValueFile:
    def __init__(self, fileName, mode):
        self.mode = mode 
        if mode == "write":
            m = "w"
        elif mode == "read":
            m = "r"
        else:
            raise Exception("use 'write' or 'read'")
        
        self.stream = open(fileName, m)
        
    def statements(self):
        if self.mode != "read":
            raise Exception("use 'read' if you want to read")
        for line in self.stream:
            yield line.strip().split(",")

    def groupsOfStatementsOfAnItem(self):
        statements = self.statements()

        currentItemId = None
        statementsOfCurrentItem = ()

        for statement in statements:
            if currentItemId != statement[0]:
                if currentItemId != None:
                    yield statementsOfCurrentItem
                currentItemId = statement[0]
                statementsOfCurrentItem = ()
            statementsOfCurrentItem.append((statement[1],statement[2]))

    def writeStatement(self, itemId, propertyId, itemValueId):
        if self.mode != "write":
            raise Exception("use 'read' if you want to read")

        statement = ",".join([itemId, propertyId, itemValueId])
        self.stream.write(statement+"\n")
