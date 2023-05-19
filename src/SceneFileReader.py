
import json
from collections import namedtuple
class SceneFileReader(object):


    def get_inputs():
    #user input text to animate
        text = input("please add the text you would like to animate: ")
        return(text)

    out = {}
    # generate the json file with the user text
    with open('Story1.json','w') as filename:
        json.dump(out, filename, indent=2)

    # attempting to read the filename and set it to filename
    def __init__(self,filename):

        self.filename = filename

    # reading the file and attributing scene nodes
    def readFile(self):

        with open(self.filename) as data_file:
            data = json.load(data_file)

        scene_nodes = [namedtuple('SceneNode',node.keys())(*node.values()) for node in data["scene_nodes"]]

        return scene_nodes