from pymedtermino.snomedct import *
from pymetamap import MetaMap
import pandas as pd


def get_keys_from_mm(concept, klist):
    conc_dict = concept._asdict()
    conc_list = [conc_dict.get(kk) for kk in klist]
    return (tuple(conc_list))


file = open("../SnowmedMetaMap/Sentences.txt")
data = file.read()
file.close()

mm = MetaMap.get_instance("/home/dhyey/Files/Python/LY-Project/Docs/public_mm/bin/metamap")

concepts, error = mm.extract_concepts(data, composite_phrase=1)

for concept in concepts:
    print(concept)

# keys_of_interest = ['preferred_name', 'cui', 'semtypes', 'pos_info']
# cols = [get_keys_from_mm(cc, keys_of_interest) for cc in concepts]
# results_df = pd.DataFrame(cols, columns=keys_of_interest)
#
# print(results_df)
