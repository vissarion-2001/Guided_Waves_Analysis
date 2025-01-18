# Importing Required Modules in order for the Program to

import numpy as np
import pandas as pd
import sklearn.preprocessing

class Preprocessing_data(sklearn.preprocessing.StandardScaler):

    def __init__(self, modes, freqs):

        self.modes = modes
        self.freqs = freqs

    def constructing_pandas_dataframes(self, ids):
        
        dict_data = {self.modes[0]:{self.freqs[0]:None, self.freqs[1]:None, self.freqs[2]:None, self.freqs[3]:None, self.freqs[4]:None},self.modes[1]:{self.freqs[0]:None, self.freqs[1]:None, self.freqs[2]:None, self.freqs[3]:None}}
        
        for mode in self.modes:
            
            for freq in self.freqs:
                
                data = []
                
                for i in ids: 
                    
                    path = f"UGW monitoring signals (Database)/Window-1.G4-288-{i}-V-0-waveform.xls"
                    
                    if mode == 0 and freq == 24: 
                        
                        df = pd.read_excel(path, sheet_name=0)
                        data.append(df["Unnamed: 1"].iloc[:].values) 
                    
                    elif mode == 0 and freq == 30: 
                        
                        df = pd.read_excel(path, sheet_name=1) 
                        data.append(df["Unnamed: 1"].iloc[:].values) 
                    
                    elif mode == 0 and freq == 37: 
                        
                        df = pd.read_excel(path, sheet_name=2)
                        data.append(df["Unnamed: 1"].iloc[:].values) 
                        
                    elif mode == 0 and freq == 14: 
                        
                        df = pd.read_excel(path, sheet_name=3)
                        data.append(df["Unnamed: 1"].iloc[:].values) 
                    
                    elif mode == 0 and freq == 18:  
                        
                        df = pd.read_excel(path, sheet_name=4)
                        data.append(df["Unnamed: 1"].iloc[:].values) 
                    
                    elif mode == 1 and freq == 24: 
                        
                        df = pd.read_excel(path, sheet_name=0) 
                        data.append(df["Unnamed: 2"].iloc[:].values) 
                    
                    elif mode == 1 and freq == 30: 
    
                        df = pd.read_excel(path, sheet_name=1) 
                        data.append(df["Unnamed: 2"].iloc[:].values) 
                    
                    elif mode == 1 and freq == 37: 
                        df = pd.read_excel(path, sheet_name=2) 
                        data.append(df["Unnamed: 2"].iloc[:].values) 
                    
                    elif mode == 1 and freq == 14: 
                        df = pd.read_excel(path, sheet_name=3) 
                        data.append(df["Unnamed: 2"].iloc[:].values) 
                    
                    elif mode == 1 and freq == 18: 
                        df = pd.read_excel(path, sheet_name=4) 
                        data.append(df["Unnamed: 2"].iloc[:].values) 
                    
                    elif mode == 2 and freq == 24: 
                        df = pd.read_excel(path, sheet_name=0) 
                        data.append(df["Unnamed: 3"].iloc[:].values) 
                    
                    elif mode == 2 and freq == 30: 
                        df = pd.read_excel(path, sheet_name=1) 
                        data.append(df["Unnamed: 3"].iloc[:].values) 
                    
                    elif mode == 2 and freq == 37: 
                        df = pd.read_excel(path, sheet_name=2) 
                        data.append(df["Unnamed: 3"].iloc[:].values) 
                    
                    elif mode == 2 and freq == 14: 
                        df = pd.read_excel(path, sheet_name=3) 
                        data.append(df["Unnamed: 3"].iloc[:].values) 
                    
                    elif mode == 2 and freq == 18: 
                        df = pd.read_excel(path, sheet_name=4) 
                        data.append(df["Unnamed: 3"].iloc[:].values) 
                    
                D = np.array(data).T 
                
                dict_data[mode][freq] = D[1:,:]
        
        return dict_data

def scaling_the_data(self, ids):  
    
    SC = self.MinMaxScaler() 
    
    scaled_dict = {self.modes[0]:{self.freqs[0]:None, self.freqs[1]:None, self.freqs[2]:None, self.freqs[3]:None, self.freqs[4]:None},self.modes[1]:{self.freqs[0]:None, self.freqs[1]:None, self.freqs[2]:None, self.freqs[3]:None}}
    
    for mode in self.modes: 
        
        for freq in self.freqs: 
            
            scaled_dict[mode][freq] = SC.fit_transform(self.constructing_pandas_dataframes(self.modes,self.freqs,ids)[0][mode][freq])
            
    return scaled_dict