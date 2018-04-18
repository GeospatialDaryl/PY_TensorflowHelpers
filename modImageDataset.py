from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

class TF_ImageDataset:
    def __init__(self,dataSetName,listImagePaths, listLabels):
        if len(listImagePaths) != len(listLabels):
            print("BAD BAD")
        
        self.dictDS = {}

        for i in range(len(listImagePaths)):
            key = listImagePaths[i]
            val = listLabels[i]
            self.dictDS[key] = val
    def summarize(self):
        print("summary :")
        print("length of listImagePaths: " len(listImagePaths))
        print("length of listLabels: " len(listLabels))
            
                    
                
                