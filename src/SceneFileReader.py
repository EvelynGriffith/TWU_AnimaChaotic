"""This bit of green is the original code, my original code is below."""
# import json
# from collections import namedtuple
# class SceneFileReader(object):

#     def __init__(self,filename):

#         self.filename = filename


#     def readFile(self):

#         with open(self.filename) as data_file:
#             data = json.load(data_file)

#         scene_nodes = [namedtuple('SceneNode',node.keys())(*node.values()) for node in data["scene_nodes"]]

#         return scene_nodes

"""This file is generating the story1 json file based off of a user input, it then attempts to read that
file and assign tokens to the important words, i believe."""
import json
from collections import namedtuple
import spacy
nlp = spacy.load('en_core_web_sm')
nlp1 = spacy.load('en_core_web_lg')
from pathlib import Path
import numpy as np
from numpy import dot
from numpy.linalg import norm
from tabulate import tabulate

filename = "Story1.json"
with open(filename, "w") as f:
  while True:
    # adds a user input text into a generated json file, in a string format!
    user_input = input("Please add your story text here: ")
    file_contents = (f.write('"' + user_input + '"'))
    x = len(user_input)
    # print(x)
    # print(user_input)
    #       f.write("\n")
    #   except EOFError:
    break
  
# trying to sort the words into the below lists so they can be made into a dictionary.
noun_list = []
verb_list=[]
adjective_list=[]
propernoun_list=[]

with open(filename) as filedata:
   # Traverse in each line of the file
    for textline in filedata:
      # Splitting the text file content into list of words
        wordsList = textline.split()
        string_words = Path(filename).read_text()

        noun=0
        punctuation=0
        adposition=0
        verb=0
        propernoun=0
        determiner=0
        coordinatingconjunction=0
        subordinatingconjunction=0
        auxiliary=0
        adjective=0
        time=0


        doc = nlp(string_words)
        #doc = nlp("They had it on the top of a hill, ina  sloping field that looked down into a sunny valley. Anne did not very much like a big brown cow who came up close and stared at her, but it went away when told it to.")

        x=string_words.split(".")
        print(x)

        for token in doc:
            # print(token, "|", spacy.explain(token.pos_))
            # table = [[token.text, spacy.explain(token.pos_)]]
            if spacy.explain(token.pos_) != "punctuation":
                time+=0.5
            if spacy.explain(token.pos_) == "noun":
                noun+=1
                noun_list.append(token.text)
            elif spacy.explain(token.pos_) == "punctuation":
                punctuation+=1
            elif spacy.explain(token.pos_) == "adposition":
                adposition+=1
            elif spacy.explain(token.pos_) == "verb":
                verb+=1
                verb_list.append(token.text)
            elif spacy.explain(token.pos_) == "proper noun":
                propernoun+=1
                propernoun_list.append(token.text)
            elif spacy.explain(token.pos_) == "determiner":
                determiner+=1
            elif spacy.explain(token.pos_) == "coordinating conjunction":
                coordinatingconjunction+=1
            elif spacy.explain(token.pos_) == "subordinating conjunction":
                subordinatingconjunction+=1
            elif spacy.explain(token.pos_) == "auxiliary":
                auxiliary+=1
            elif spacy.explain(token.pos_) == "adjective":
                adjective+=1
                adjective_list.append(token.text)
            # print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        break

    print("noun: "+ str(noun))
    print("punctuation: "+ str(punctuation))
    print("adposition: "+ str(adposition))
    print("verb: "+ str(verb))
    print("proper noun: "+ str(propernoun))
    print("determiner: "+ str(determiner))
    print("coordinating conjuction: "+ str(coordinatingconjunction))
    print("subordinating conjunction: "+ str(subordinatingconjunction))
    print("auxiliary: "+ str(auxiliary))
    print("adjective: "+ str(adjective))
    print("time: "+ str(time))

nouns = str(noun_list)
verbs = str(verb_list)
propernouns = str(propernoun_list)
adjectives = str(adjective_list)
# def get_inputs():
# #user input text to animate
#     text = input("please add the text you would like to animate: ")
#     return(text)

# This prints the nouns from whatever input is entered into a dictionary format within the json file.
noun_dict = {}
values = noun_list
keys = [i for i in range(len(values))]
# print(values)
# print(keys)
for i in keys:
    noun_dict[i] = values[i]
print(noun_dict)

verb_dict = {}
values = verb_list
keys = [i for i in range(len(values))]
# print(values)
# print(keys)
for i in keys:
    verb_dict[i] = values[i]
print(verb_dict)

# this is reopening the created Story1 file and replacing the text with the appropriate dictionaries
filename = "Story1.json"
with open(filename, "w") as f:
  while True:
    # adds a user input text into a generated json file, in a string format!
    left_brace = (f.write("["))
    noun_dictionary = (f.write(json.dumps(noun_dict)))
    comma1 = (f.write(","))
    verb_dictionary = (f.write(json.dumps(verb_dict)))
    right_brace = (f.write("]"))
    break
# out = {user_input}
# # # generate the json file with the user text
# filename = open(r'Story1.json','w')
# with filename:
#     json.dump(out, filename, indent=2)

class SceneFileReader():
    filename = "Story1.json"
    with open(filename, "r") as f:
    
        # def __init__(self,f):

        #     self.f = f

    # reading the file and attributing scene nodes
        def readFile(self):
            # data_file = open("Story1.json")
            # f = open(r"C:\Users\gforc\TWU_AnimaChaotic\Story1.json")
            with open(filename, "r"):
                data = json.load(self.f)
                # print(type(data))
                scene_nodes = [namedtuple('SceneNode',node.keys())(*node.values()) for node in data[0-x]]
                # scene_nodes = [namedtuple('SceneNode',node.keys())(*node.values()) for node in data[0 - x]]
                # scene_nodes = [namedtuple('SceneNode', node.keys())(*node.values())]

                return scene_nodes