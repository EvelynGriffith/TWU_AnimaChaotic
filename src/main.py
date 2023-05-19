from SceneFileReader import SceneFileReader
from SceneManager import SceneManager
from DataBaseManager import DataBaseManager as db_manager

FILENAME = r"C:\Users\rachm\Downloads\TWU_AnimaChaotic-master\TWU_AnimaChaotic-master\src\story.json"
#FILENAME = "../../sample_stories/simplified_street.json"


if __name__=="__main__":

    #Connect to the database
    db_manager("mongodb://localhost:27017/").connect()
    #Read the output of the NLP module
    scene_file_reader = SceneFileReader(FILENAME) # May be change that to a string
    scene_nodes = scene_file_reader.readFile()
    #Create the scene manager
    app = SceneManager(scene_nodes)
    #run the application
    app.run()



