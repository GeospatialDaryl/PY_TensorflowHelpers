#  Class for Image stuff
#       Daryl Van Dyke GeospatialDaryl@github.com
##  `take` from :
#  
#https://stackoverflow.com/questions/7971618/python-return-first-n-keyvalue-pairs-from-dict
from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

class TF_ImageDataset:
    """  A class for TF Image Datasets:  listImagePaths, listLabels , datasetName = 'generic'  """
    def __init__(self,listImagePaths, listLabels, datasetName):
        if len(listImagePaths) != len(listLabels):
            print("BAD BAD")
        
        self.dictDS = {}
        self.datasetName = datasetName
        self.listImagePaths = listImagePaths
        self.listLabels = listLabels

        for i in range(len(listImagePaths)):
            key = listImagePaths[i]
            val = listLabels[i]
            self.dictDS[key] = val
            
    def summarize(self,topN = 5):
        print("summary :",self.datasetName)
        print("length of listImagePaths: ", len(self.listImagePaths))
        print("length of listLabels: ", len(self.listLabels))
        print(take(topN, self.dictDS.items() ))
            
    def __add__(self, otherClassImgDS, datasetName = "merged"):
        newDict =  {**self.dictDS, **otherClassImgDS.dictDS}
        outKeys = []
        outVals = []
        for key in newDict:
            outKeys.append(key)
            outVals.append(newDict[key])
        return TF_ImageDataset(outKeys, outVals, datasetName)
    
    def n(self):
        lenSamp = len(self.dictDS)
        self.n = lenSamp
        return lenSamp
            