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

# def get_inputs():
# #user input text to animate
#     text = input("please add the text you would like to animate: ")
#     return(text)

# out = {user_input}
# # # generate the json file with the user text
# filename = open(r'Story1.json','w')
# with filename:
#     json.dump(out, filename, indent=2)

class SceneFileReader():
    # attempting to read the filename and set it to filename
    # def __init__(self,filename):

    #     self.filename = filename

    # reading the file and attributing scene nodes
    def readFile(self):
        # data_file = open("Story1.json")
        # f = open(r"C:\Users\gforc\TWU_AnimaChaotic\Story1.json")
        data = json.loads(f)
        # print(type(data))
        scene_nodes = [namedtuple('SceneNode',node.keys())(*node.values()) for node in data[0-x]]
        # scene_nodes = [namedtuple('SceneNode',node.keys())(*node.values()) for node in data[0 - x]]
        # scene_nodes = [namedtuple('SceneNode', node.keys())(*node.values())]

        return scene_nodes