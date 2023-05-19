
import json
from collections import namedtuple

filename = "Story1.json"
with open(filename, "w") as f:
  while True:
    user_input = f.write(input("Add your story text here: "))
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

class SceneFileReader(object):
    # attempting to read the filename and set it to filename
    def __init__(self,filename):

        self.filename = filename

    # reading the file and attributing scene nodes
    def readFile(self):

        with filename as data_file:
            data = json.load(data_file)

        scene_nodes = [namedtuple('SceneNode',node.keys())(*node.values()) for node in data["scene_nodes"]]

        return scene_nodes