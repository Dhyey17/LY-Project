from pymedtermino.snomedct import *
from pymedtermino.umls import *
from pymetamap import MetaMap

note1 = ["Mrs. Jones came in today complaining of a lot of chest pain. She denies shortness of breath and fevers."]
#
# note2 = "Mr. Smith has been having pain in his knee for many weeks. It hurts when he walks. There is no swelling, erythema, or micromotion tenderness."
#
# note3 = "Sandy Lemon has been having headaches for two months that are associated with blurry vision and numbness in her right arm."
#
# # Put them all together in a list
# note_list = [note1, note2, note3]
#

# file = open("Sentences.txt")
# data = file.read()
# file.close()

mm = MetaMap.get_instance("/home/dhyey/Downloads/public_mm/bin/metamap")

concepts, error = mm.extract_concepts(note1, composite_phrase=1)

for concept in concepts:
    print(concept)

# # cui = "C0013404"
#
# print(SNOMEDCT[302509004])
