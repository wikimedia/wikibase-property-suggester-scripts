# coding=utf-8
"""
Auswertungen:

wieviele eigenschaften wurden positiv, negativ, ... bewertet?
durchschnittliche anzahl positiver, negativer bewertungen pro item?
für jede eigenschaft x die durchschnittliche bewertung ermitteln

"""

__author__ = 'Virginia'

import json
import csv
from Entity import Entity

class UserFeedbackEvaluation():
    def __init__(self):
        pass
    def preprocess_file(self):
        filename = 'C:\Users\Virginia\Documents\GitHub\PropertySuggester-Python\propertysuggester\evaluator\manuell\python_excel.csv'
        skipped = 0
        skipped_ids = []
        with open(filename, 'r') as csvfile:
            csvfile.readline()
            eval_reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
            evaluation_list = []
            for i, row in enumerate(eval_reader):
                id = i
                # for checking
                properties = row[4]
                suggestions = row[5]
                missing = row[6]
                if properties[-1]  != "]" or suggestions[-1]  != "]" or missing[-1] != "]":
                    skipped+=1
                    skipped_ids.append(row[3])
                    continue
                entity = Entity(row, id)
                evaluation_list.append(entity)
            print "Skipped Items due to invalid data: " + str(skipped) +". Items: " + str(skipped_ids)
            return evaluation_list
    def analyse_count(self, eval_list):
        positive = 0
        negative = 0
        neutral = 0
        question = 0
        totalAmountRatings = 0
        totalEntities = 0
        for entity in eval_list:
            for suggestion in entity.suggestions:

                if suggestion.rating == -1:
                    negative +=1
                if suggestion.rating == 0:
                    neutral += 1
                if suggestion.rating == 1:
                    positive += 1
                if suggestion.rating == -2:
                    question += 1
                totalAmountRatings += 1
            totalEntities+=1

        print str(totalAmountRatings) + " total ratings in " + str(totalEntities) + " Entities"
        print "Positive: " + str(positive)
        print "Negative: " + str(negative)
        print "Neutral: " + str(neutral)
        print "Do not know: " + str(question)

    def analyse_average_per_entity(self, eval_list):
        entity_dict = {}
        for entity in eval_list:
            if not entity.entity in entity_dict:
                entity_dict[entity.entity] = []
            for suggestion in entity.suggestions:
                if not suggestion.rating == -2:
                    entity_dict[entity.entity].append(suggestion.rating)
        total_average = 0
        total_counter = 0
        for entity_id, entity_data in entity_dict.items():
            print "Entity: " + str(entity_id)
            summe = 0
            counter = 0
            if entity_data ==[]:
                print "Can't determine average (only '?' provided), skip to  next item"
                continue
            for rating in entity_data:
                summe += rating
                counter += 1

            print "Average: " + str(float(summe)/counter) +" out of " + str(counter) +" ratings"
            total_average += float(summe)/counter
            total_counter += 1
        print "Total average over all items " + str(total_average/total_counter)

luser = UserFeedbackEvaluation()
eval_list = luser.preprocess_file()
luser.analyse_count(eval_list)
#luser.analyse_average_per_entity(eval_list)