# coding=utf-8
"""
Auswertungen:

wieviele eigenschaften wurden positiv, negativ, ... bewertet?
durchschnittliche anzahl positiver, negativer bewertungen pro item?
für jede eigenschaft x die durchschnittliche bewertung ermitteln

"""

__author__ = 'Virginia'
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
                entity_id = i
                # for checking
                properties = row[4]
                suggestions = row[5]
                missing = row[6]
                if properties[-1] != "]" or suggestions[-1] != "]" or missing[-1] != "]":
                    skipped += 1
                    skipped_ids.append(row[3])
                    continue
                entity = Entity(row, entity_id)
                evaluation_list.append(entity)
            print "Skipped Items due to invalid data: " + str(skipped) + " Items: " + str(skipped_ids)
            return evaluation_list

    def analyse_count(self, eval_list):
        ratings_dict = {}
        positive = 0
        negative = 0
        neutral = 0
        question = 0
        totalAmountRatings = 0
        totalEntities = 0
        for entity in eval_list:
            for suggestion in entity.suggestions:
                prob = (int(float(suggestion.probability) * 50))
                if prob not in ratings_dict:
                    ratings_dict[prob] = {"pos": 0, "neutral": 0, "neg": 0}
                if suggestion.rating == -1:
                    negative += 1
                    ratings_dict[prob]["neg"] += 1
                if suggestion.rating == 0:
                    neutral += 1
                    ratings_dict[prob]["neutral"] += 1
                if suggestion.rating == 1:
                    positive += 1
                    ratings_dict[prob]["pos"] += 1
                if suggestion.rating == -2:
                    question += 1
                totalAmountRatings += 1
            totalEntities += 1
        with open("average_csv.csv", "wb") as csv_file:
            rating_writer = csv.writer(csv_file, delimiter=';',
                                       quotechar='|')
            rating_writer.writerow(["probability", "positive", "neutral", "negative"])
            for proba, amount in ratings_dict.items():
                rating_writer.writerow([proba, amount["pos"], amount["neutral"], amount["neg"]])
        print str(totalAmountRatings) + " total ratings in " + str(totalEntities) + " Entities"
        print "Positive: " + str(positive)
        print "Negative: " + str(negative)
        print "Neutral: " + str(neutral)
        print "Do not know: " + str(question)

    def analyse_average_per_entity(self, eval_list):

        entity_ratings = {}
        entity_probabilities = {}

        for entity in eval_list:
            if not entity.entity in entity_ratings:
                entity_ratings[entity.entity] = []
            if not entity.entity in entity_probabilities:
                entity_probabilities[entity.entity] = []

            for suggestion in entity.suggestions:
                if not suggestion.rating == -2:
                    entity_ratings[entity.entity].append(suggestion.rating)
                entity_probabilities[entity.entity].append(suggestion.probability)
        total_rating_average = 0
        total_rating_counter = 0
        for entity_id, entity_data in entity_ratings.items():
            print "Entity: " + str(entity_id)
            summe = 0
            counter = 0
            if entity_data == []:
                print "Can't determine average (only '?' provided), skip to  next item"
                continue
            for rating in entity_data:
                summe += rating
                counter += 1

            print "Average: " + str(float(summe) / counter) + " out of " + str(counter) + " ratings"
            total_rating_average += float(summe) / counter
            total_rating_counter += 1

        print "Total average over all items " + str(total_rating_average / total_rating_counter)
        for entity_id, entity_probability in entity_probabilities.items():
            summe = 0
            counter = 0
            for probability in entity_probability:
                summe += float(probability)
                counter += 1
            print "Average probability Item (" + str(entity_id) + ") " + str(float(summe) / counter)

    def determine_amount_entities(self, eval_list):
        entity_dict = {}
        for entity in eval_list:
            if not entity.entity in entity_dict:
                entity_dict[entity.entity] = 1
                continue
            entity_dict[entity.entity] += 1
        sorted = [(entity_amount,entity_entry) for entity_entry, entity_amount in entity_dict.items()]
        sorted.sort(reverse=True)

        with open("amount_per_entity.csv", "wb") as csv_file:
            amount_writer = csv.writer(csv_file, delimiter=';',
                                       quotechar='|')
            for entity_amount, entity_entry in sorted:
                print str(entity_entry) + " amount: " + str(entity_amount)
                amount_writer.writerow([entity_entry, entity_amount])

    def determine_precision(self, eval_list):
        precision_sum = 0
        precision_counter = 0

        for entity in eval_list:
            relevant_set = set()
            retrieved_set = set()
            with open("precision_per_entity_per_position.csv", "wb") as position_csv:
                precision_position_writer = csv.writer(position_csv, delimiter=';',
                                   quotechar='|')
                for suggestion in entity.suggestions:
                    retrieved_set.add(suggestion.suggestion_id)

                    if suggestion.rating == 1 or suggestion.rating == 0:
                        relevant_set.add(suggestion.suggestion_id)
                # second round
                relevance_counter = 0

                for suggestion in entity.suggestions:
                    if suggestion.suggestion_id in relevant_set:
                        relevance_counter += 1
                        precision = (float(relevance_counter))/(int(suggestion.position)+1)
                    print "calculation: precision position #"+ str(suggestion.position) + "  "+ str(precision)
                    precision_position_writer.writerow([entity.entity, suggestion.position, precision])


                result_set = retrieved_set.intersection(relevant_set)
                if len(relevant_set) == 0:
                    print "null relevance, skip " + str(entity.entity)
                    continue
        precision = float(len(result_set)) / len(retrieved_set)
        precision_sum += precision
        precision_counter += 1
        with open("precision_per_entity.csv", "wb") as csv_file:
            precision_writer = csv.writer(csv_file, delimiter=';',
                               quotechar='|')
            precision_writer.writerow([entity.entity, precision])
            print "precision for: " + str(entity.entity) + str(" ") + str(precision)
        print "Average precision over all items: " + str(float(precision_sum / precision_counter))

    def determine_recall_per_position(self, eval_list):
        for entity in eval_list:
            relevant_set = set()
            retrieved_set = set()
            for suggestion in entity.suggestions:
                retrieved_set.add(suggestion.suggestion_id)

                if suggestion.rating == 1 or suggestion.rating == 0:
                    relevant_set.add(suggestion.suggestion_id)
            # second round
            relevance_counter = 0
            print entity.entity
            for suggestion in entity.suggestions:


                if suggestion.suggestion_id in relevant_set:
                    relevance_counter += 1
                    rel_length= len(relevant_set)
                    recall = (float(relevance_counter))/rel_length
                print "Recall at  position #"+ str(suggestion.position) + "  "+ str(recall)


    def analyse_suggestion_properties(self, eval_list):
        property_dict ={}

        for entity in eval_list:
            for suggestion in entity.suggestions:
                property_id = suggestion.suggestion_id
                if property_id not in property_dict:
                    property_dict[property_id] = {"pos": 0, "neutral": 0, "neg": 0,"question" : 0}
                if suggestion.rating == -1:
                    property_dict[property_id]["neg"] += 1
                if suggestion.rating == 0:
                    property_dict[property_id]["neutral"] += 1
                if suggestion.rating == 1:
                    property_dict[property_id]["pos"] += 1
                if suggestion.rating == -2:
                    property_dict[property_id]["question"] += 1
        for prop_id, prop in property_dict.items():
            print "prop id " + str(prop_id) + " " + str(prop)
luser = UserFeedbackEvaluation()
eval_list = luser.preprocess_file()
#print (" ##### Amount of ratings")
#luser.analyse_count(eval_list)
print (" ##### Average rating per entity")
#luser.analyse_average_per_entity(eval_list)
print (" ###### Amount of entities")
luser.determine_amount_entities(eval_list)

#luser.determine_precision(eval_list)
luser.determine_precision(eval_list)
#luser.determine_recall_per_position(eval_list)
#luser.analyse_suggestion_properties(eval_list)