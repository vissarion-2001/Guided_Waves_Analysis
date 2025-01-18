import numpy as np
from scipy.fft import fft
import pywt

class Time_freq_domain_chars:
    
    def __init__(self, samples, sampling_period, healthy_data, damaged_data, ids_healthy, ids_damaged, modes, freqs):
        
        self.samples = samples
        self.sampling_period = sampling_period 
        self.healthy_data = healthy_data
        self.damaged_data = damaged_data
        self.ids_healthy = ids_healthy
        self.ids_damaged = ids_damaged
        self.modes = modes
        self.freqs = freqs
    
    def rmsd_analysis(self):
        
        while True:
            
            while True:
                
                try:
                    
                    c = input("Please give the case you want to examine, 'H' for Healthy and 'D' for Damage\n")
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if c in ['H','D']:
                
                break
            
            else:
                
                print("Incorrect input state")
                continue
        
        while True:
            
            while True:
                
                try:
                    
                    n = int(input("Please give the number of case you want:\n"))
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if  (c == "H" ) and (n in range(len(self.ids_healthy))):
                
                break
            
            elif (c == "D" ) and (n in range(len(self.ids_damaged))):
                
                break
            
            else:
                
                print("No correct id")
                continue
        
        while True:
            
            while True:
                
                try:
                    
                    ma = int(input("Please give the mode you want to Analyze:\n"))
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if ma in self.modes:
                
                break
            
            else:
                
                print("Incorrect mode\n")
                continue
            
        
        while True:
            
            while True:
                
                try:
                    
                    fa = int(input("Please give the frequency you want to Analyze:\n"))
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if fa in self.freqs:
                
                break
            
            else:
                
                print("Incorrect freq\n")
                continue   
            
        healthy_data_c = self.healthy_data[ma][fa][:,n]
            
        if c == "H":
                
            selected_data = self.healthy_data[ma][fa][:,n]
            
        elif c == "D":
                
            selected_data = self.damaged_data[ma][fa][:,n]
                
        RMSD = np.sqrt((1.0/len(healthy_data_c))*(np.sum((healthy_data_c-selected_data)**2)))
        return RMSD, c, n, ma, fa
    
    def fourier_analysis(self):
        
        while True:
            
            while True:
                
                try:
                    
                    cf = input("Please give the case you want to examine, 'H' for Healthy and 'D' for Damage")
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if cf in ['H','D']:
                
                break
            
            else:
                
                print("Incorrect input state")
                continue
        
        while True:
            
            while True:
                
                try:
                    
                    nf = int(input("Please give the number of case you want:\n"))
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if  (cf == "H" ) and (nf in range(1,len(self.ids_healthy)+1)):
                
                break
            
            elif (cf == "D" ) and (nf in range(1,len(self.ids_damaged)+1)):
                
                break
            
            else:
                
                print("No correct id")
                continue
        
        while True:
            
            while True:
                
                try:
                    
                    mf = int(input("Please give the mode you want to Analyze:\n"))
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else: 
                    
                    break
            
            if mf in self.modes:
                
                break
            
            else:
                
                print("Incorrect mode\n")
                continue
            
        
        while True:
            
            while True:
                
                try:
                    
                    ff = int(input("Please give the frequency you want to Analyze:\n"))
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if ff in self.freqs:
                
                break
            
            else:
                
                print("Incorrect mode\n")
                continue
            
        if cf == "H":
                
            Y = self.healthy_data[mf][ff][:,nf]
            
        elif cf == "D":
                
            Y = self.damaged_data[mf][ff][:,nf]
        
        
        Yf = fft(Y)
        return np.abs(Yf), cf, nf, mf, ff
    
    def cwt_calculations(self, wavelet="cmor1.5-1.0", widths=np.geomspace(1, 1024, num=100)):
        
        while True:
            
            while True:
                
                try:
                    
                    cw = input("Please give the case you want to examine, 'H' for Healthy and 'D' for Damage")
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
                
            
            if cw in ['H','D']:
                
                break
            
            else:
                
                print("Incorrect input state")
                continue
        
        while True:
            
            while True:
                
                try:
                    
                    nw = int(input("Please give the number of case you want:\n"))
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if  (cw == "H" ) and (nw in range(1,len(self.ids_healthy)+1)):
                
                break
            
            elif (cw == "D" ) and (nw in range(1,len(self.ids_damaged)+1)):
                
                break
            
            else:
                
                print("No correct id")
                continue
        
        while True:
            
            while True:
                
                try:
                    
                    mw = int(input("Please give the mode you want to Analyze:\n"))
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if mw in self.modes:
                
                break
            
            else:
                
                print("Incorrect mode\n")
                continue
            
        
        while True:
            
            while True:
                
                try:
                    
                    fw = int(input("Please give the frequency you want to Analyze:\n"))
                
                except ValueError:
                    
                    print("Invalid Input")
                    continue
                
                else:
                    
                    break
            
            if fw in self.freqs:
                
                break
            
            else:
                
                print("Incorrect mode\n")
                continue
            
        if cw == "H":
                
            ys = self.healthy_data[mw][fw][:,nw]
            
        elif cw == "D":
                
            ys = self.damaged_data[mw][fw][:,nw]
        
        cwtmatr, freqs = pywt.cwt(ys, widths, wavelet, sampling_period=1/self.sampling_period) 
        
        # absolute take absolute value of complex result 
        
        cwtmatr = np.abs(cwtmatr[:-1,:-1])
        return cwtmatr, freqs, cw, nw, mw, fw
