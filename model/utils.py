import pickle
import json
import numpy as np
import pandas as pd
#import config

class flowerModel():
    def __init__(self,SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
        
        self.SepalLengthCm= SepalLengthCm 
        self.SepalWidthCm = SepalWidthCm 
        self.PetalLengthCm= PetalLengthCm 
        self.PetalWidthCm = PetalWidthCm 

    def load_model(self):
        with open(r"C:\Users\Rahul\Desktop\logictics\flower\flower\model\flower.json", "r") as f:
            self.json_data=json.load(f)

        with open(r"C:\Users\Rahul\Desktop\logictics\flower\flower\model\Flower.pkl", "rb") as f:
            self.model=pickle.load(f)

    def get_flower_prediction(self):
        self.load_model()

        array=np.zeros(len(self.json_data["column_names"]))

        array[0]=self.SepalLengthCm
        array[1]=self.SepalWidthCm
        array[2]=self.PetalLengthCm
        array[3]=self.PetalWidthCm

        print("Array ::",array )

        result=self.model.predict([array])[0]
        return result
        
       
if __name__ == "__main__":
    SepalLengthCm = 5.0
    SepalWidthCm = 4.5
    PetalLengthCm = 2.4
    PetalWidthCm = 0.5


    Obj = flowerModel(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    output = Obj.get_flower_prediction()
    print()
    print(f"Predicted species is: {output}♥")
