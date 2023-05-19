"""Text File to JSON file conversion code."""
import  jpype     
# import asposecells     
jpype.startJVM() 
from asposecells.api import Workbook

# load TXT file
workbook = Workbook("C:\\Users\\gforc\\TWU_AnimaChaotic\\src\\Story1")

# save as JSON
workbook.Save("Story1.json")

jpype.shutdownJVM()