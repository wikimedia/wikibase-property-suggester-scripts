from collections import defaultdict

from StatementWithItemValueFile import StatementWithItemValueFile

class StatementWithItemValueAnalyzer:

    def analyze(self, inFile, outFilePrefix):
        statementsFile = StatementWithItemValueFile(inFile, "read")

        print "\n\n#step1: count statement occurences\n"
        statementGroups = defaultdict()
        numOfStatements = self.countStatementOccurences(statementsFile, statementGroups)
    	
        coverage = self.calculateMinCoverage(len(statementGroups), numOfStatements)
        print "coverage = {0}\n".format(coverage)

        print "\n\n#step2: apply selection of relevant statements\n"
        relevantStatementGroups = defaultdict()
        self.applyThreshold(statementGroups, relevantStatementGroups, coverage)
        print "{0} of {1} statements do show a sufficient coverage\n".format(len(relevantStatementGroups),len(statementGroups))
        statementGroups.clear() #free memory

        print "\n\n#step3: build cross product\n"
        statementPairGroups = defaultdict()
        self.initializeStatementPairGroups(relevantStatementGroups.keys(), statementPairGroups)

        print "\n\n#step4: count statement pair appearences\n"
        numOfStatementPairs = self.countStatementPairOccurences(statementsFile, statementPairGroups)

        print "\n\n#step5: apply selection of relevant statements\n"
        avgStatementsPerGroup = numOfStatementPairs/len(statementPairGroups)
        coverage = 4*avgStatementsPerGroup
        relevantStatementPairGroups = defaultdict()
        self.applyThreshold(statementPairGroups, relevantStatementPairGroups, coverage)
        print "{0} of {1} statement pairs do show a sufficient coverage\n".format(len(relevantStatementPairGroups),len(statementPairGroups))
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

    def calculateMinCoverage(self, numOfGorups, numOfStatements):
        """ select threshold so that n will be so that we'll select n statement groups as relevant where n x n = numOfStatements."""
        # todo find adequate distribution
        avg = numOfStatements*1.0/numOfGorups
        # proportion = numOfStatements**-0.5
        return avg * 20

    def applyThreshold(self, inList, outList, threshold):
        for k, v in inList.items():
            if v >= threshold:
                outList[k] = v 

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
                        if 0 == (i % 1000000): print "processed {0} relevant property pair occurences\n".format(i)
        return i

    def writeInfo(self, relevantStatementGroups, outFilePrefix):
        fs = open(outFilePrefix+"statement_occurrences.data", "w")
        for key, value in relevantStatementGroups.items():
            fs.write( ",".join([key[0], key[1], str(value)]) + "\n" )

    def writeRules(self, relevantStatementPairGroups, outFilePrefix):
        fs = open(outFilePrefix+"statement_pair_occurrences.data", "w")
        for key, value in relevantStatementPairGroups.items():
            fs.write( ",".join([key[0][0], key[0][1], key[1][0], key[1][1], str(value)]) + "\n" )