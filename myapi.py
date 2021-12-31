from fastapi import FastAPI,Path,Body, requests
from typing import Optional
import uvicorn
import pandas as pd
from pandas.io.stata import precision_loss_doc
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib
import Data
# from fastapi.responses import HTMLResponse
# import pickle


app = FastAPI()

test = pd.read_csv("Data\Test.csv",usecols=[1, 4])
train = pd.read_csv("Data\Data.csv", usecols=[1, 4])


class Demand(BaseModel):
    # item_name: str
    # price: int
    Number_Of_Sales: int
    Highes_Temperature: int
    # Jan_code: int

    
class Demand_Model:
    def __init__(self):
        self.df = pd.read_csv('Data.csv') 
        self.model_fname_ = 'demand_model_pkl'
        try: 
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model =self._train_model()
            joblib.dump(self.model, self.model_fname_)
            
    def _train_model(self):
        X = self.model
        y = self.df       
        rfc = RandomForestClassifier()
        model = rfc.fit(X, y)
        return model
    

# categolys_teas = {
#     "おーいお茶":{
#         "name": "おーいお茶",
#         "price": 98,
#         "Jan_code": 67990022,
#         # "salle":print("Test.csv[Number_Of_Sales]")
#     },    
# }
   


@app.get("/")
def index(): 
    return{"name" : "First Data"}

@app.get("/Categolys/{Categoly_id}")
def read_Ctegoly(Categoly_id: int, q : Optional[str] = None):
    return {"Categoly_id": Categoly_id, "q": q}

@app.get("/item_id/{Jan_code}")
def read_Ctegoly(Jan_code: int, q : Optional[str] = None):
    return{"Jan_code":Jan_code, "q": q}

# @app.post('/predict')
# def predict_demand(Data):
#     data = Data.dict()
#     prediction, probability = model.predict_demand(
    
#     )
     
#     return
    

# @app.get("/get-categolys_tea/{tea_id}")
# def get_categolys_teas(tea_name : str = Path(None, description="The ID of Categolys want To view")):
#     return categolys_teas[tea_name]    

# @app.get("/get-by-salles/{tea_Jan_code}")
# def get_categolys_tea(*,Jan_code:Optional[int] = None):
#     for categolys_tea in categolys_teas:
#         if categolys_teas[categolys_tea]["Jan_code"] == Jan_code:
#             return categolys_teas[categolys_tea]
#         return {"Data":"Not Found"}
    
        
        
        
# if __name__ == "__main__":
#     app.run()
    


