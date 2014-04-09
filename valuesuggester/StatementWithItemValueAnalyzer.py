from collections import defaultdict

from StatementWithItemValueFile import StatementWithItemValueFile

class StatementWithItemValueAnalyzer:

    def analyze(self, inFile, outFilePrefix):
        statementsFile = StatementWithItemValueFile(inFile, "read")

        print "\n\n#step1: count statement occurences\n"
        statementGroups = defaultdict()
        numOfStatements = self.countStatementOccurences(statementsFile, statementGroups)

        print "\n\n#step2: apply selection of relevant statements\n"
        relevantStatementGroups = defaultdict()
        maxEntries = numOfStatements**0.5
        self.applyCutoff(statementGroups, relevantStatementGroups, maxEntries)

        print "{0} of {1} statements do show a sufficient coverage\n".format(len(relevantStatementGroups),len(statementGroups))
        statementGroups.clear() #free memory

        print "\n\n#step3: build cross product\n"
        statementPairGroups = defaultdict()
        self.initializeStatementPairGroups(relevantStatementGroups.keys(), statementPairGroups)

        print "\n\n#step4: count statement pair appearences\n"
        self.countStatementPairOccurences(statementsFile, statementPairGroups)

        print "\n\n#step5: apply selection of relevant statements\n"
        relevantStatementPairGroups = defaultdict()
        self.applyCutoff(statementPairGroups, relevantStatementPairGroups, coverage)
        print "{0} of {1} statements do show a sufficient coverage\n".format(len(relevantStatementPairGroups),len(statementPairGroups))
        statementPairGroups.clear()

        print "\n\n#step6: write Things to disk\n"
        self.writeInfo(relevantStatementGroups, outFilePrefix)
        self.writeRules(relevantStatementPairGroups, outFilePrefix)

    def countStatementOccurences(self, statementsFile, statementGroups):
        statements = statementsFile.statements()
        i = 0
        for statement in statements:
            key = (statement[1], statement[2])
            statementGroups[key] = statementGroups.get(key, 0) + 1
            i += 1
            if 0 == (i % 5000000): print "read {0} statements\n".format(i)
                
        return i

    def applyCutoff(self, inList, outList, maxEntries):
        i = 0
        for k, v in sorted(inList.items(), key=lambda x:x[1]):
            outList[k] = v 
            i += 1
            if i >= maxEntries:
                break

    def initializeStatementPairGroups(self, keyValuePairs, statementPairGroup):
        for pair1 in keyValuePairs:
            for pair2 in keyValuePairs:
                if pair1 != pair2:
                    keyPair = (pair1, pair2)
                    statementPairGroup[keyPair] = 0 

    def countStatementPairOccurences(self, statementsFile, statementPairGroups):
        groups = statementsFile.groupsOfStatementsOfAnItem()

        currentItemId = None
        statementsOfCurrentItem = ()
        i = 0
        for group in groups:
            for pair1 in group:
                for pair2 in group:
                    keyPair = (pair1, pair2)
                    if keyPair in statementPairGroups:
                        statementPairGroups[keyPair] += 1
            i += 1
            if 0 == (i % 1000000): print "processed {0} items\n".format(i)

    def writeInfo(self, relevantStatementGroups, outFilePrefix):
        fs = open(outFilePrefix+"statement_occurences.data", "w")
        for sg in relevantStatementGroups:
            fs.write(sg+"\n")

    def writeRules(self, relevantStatementPairGroups, outFilePrefix):
        fs = open(outFilePrefix+"statement_pair_occurences.data", "w")
        for spg in relevantStatementPairGroups:
            fs.write(spg+"\n")