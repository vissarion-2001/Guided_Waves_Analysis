import matplotlib.pyplot as plt
from scipy.fft import fftfreq

class Plotting_the_data: 
    
    def __init__(self, ids_healthy, ids_damaged, data_healthy, data_damaged, modes, freqs, sampling_freq):
        
        self.ids_healthy = ids_healthy
        self.ids_damaged = ids_damaged
        self.data_healthy = data_healthy
        self.data_damaged = data_damaged
        self.sampling_freq = sampling_freq
        self.modes = modes
        self.freqs = freqs
    
    def plotting_over_cases_same_frequency(self): 
        
        while True:
            
            while True:
                
                try:
                    
                    cf = input("Please give the case of the first signal, 'H' for Healthy and 'D': for Damage \n")
                
                except ValueError:
                    
                    print("Invalid Input\n")
                    continue
                
                else:
                    
                    break
            
            if cf in ["H", "D"] :
                
                break
            
            else:
                
                print("No correct case was given\n")
                continue 
        
        while True:
            
            while True:
                
                try:
                    
                    nf = int(input("Please give the num of the first signal:\n"))
                
                except ValueError:
                    
                    print("Invalid Input\n")
                    continue
                
                else:
                    
                    break
            
            if (cf == "H") and (nf in range(1,len(self.ids_healthy)+1)):
            
                break
            
            elif (cf == "D") and (nf in range(1,len(self.ids_damaged)+1)):
                
                break
            
            else:
                
                print("No correct case was given\n")
                continue 
        
        
        while True:
            
            while True:
                
                try:
                    
                    cs = input("Please give the case of the second signal, 'H' for Healthy and 'D': for Damage \n")
                
                except ValueError:
                    
                    print("Invalid Input\n")
                    continue
                
                else:
                    
                    break
            
            if cs in ["H", "D"] :
                
                break
            
            else:
                
                print("No correct case was given\n")
                continue 
        
        while True:
            
            while True:
                
                try:
                    
                    ns = int(input("Please give the num of the second signal:\n"))
                
                except ValueError:
                    
                    print("Invalid Input\n")
                    continue
                
                else:
                    
                    break
            
            if (cs == "H") and (ns in range(1,len(self.ids_healthy)+1)):
            
                break
            
            elif (cs == "D") and (ns in range(1,len(self.ids_damaged)+1)):
                
                break
            
            else:
                
                print("No correct case was given\n")
                continue 
        
        while True:
            
            while True:
                
                try:
                    
                    mode_p = int(input("Please give mode, 0 (Torsional) or (1) for (Flexural)   for:\n"))
                
                except ValueError:
                    
                    print("Invalid Input\n")
                    continue
                
                else:
                    
                    break
            
            if mode_p in self.modes:
            
                break
            
            else:
                
                print("This mode is not in the available modes\n")
                
                continue
            
        while True:
            
            while True:
                
                try:
                    
                    freq_p = int(input("Please give mode frequency (24,30,37,14,18):\n"))
                
                except ValueError:
                    
                    print("Invalid Input\n")
                    continue
                
                else:
                    
                    break
            
            if freq_p in self.freqs:
            
                break
            
            else:
                
                print("This freq is not in the available frequencies\n")
                
                continue
        
        if cf == "H":
            
            d1 = self.data_healthy[mode_p][freq_p][:, nf]
            label_1 = "Healthy"
            
        elif cf == "D":
            
            d1 = self.data_damaged[mode_p][freq_p][:, nf]
            label_1 = "Damaged"
        
        
        if cs == "H":
            
            d2 = self.data_healthy[mode_p][freq_p][:, ns]
            label_2 = "Healthy"
        
        elif cs == "D":
            
            d2 = self.data_damaged[mode_p][freq_p][:, ns]
            label_2 = "Damaged"
            
            
        fig, ax = plt.subplots(figsize=(16, 8)) 
        
        ax.plot(d1, label=f"{label_1}_case {nf}-Frequency at {freq_p} kHz-{mode_p} Mode")  
        ax.plot(d2, label=f"{label_2}_case {ns}-Frequency at {freq_p} kHz-{mode_p} Mode")
        
        plt.legend() 
        plt.minorticks_on() 
        plt.title(f"{nf} {label_1} case and {ns} {label_2} case - Frequency at {freq_p} kHz - {mode_p} Mode") 
        plt.xlabel("Samples") 
        plt.ylabel("Voltage(V)") 

        

    def plotting_rmsd(self, cr, nr, mf, fr, r_s):
        
        d = {f"{cr}-{nr} case with mode {mf} and frequency {fr}":r_s}
        
        fig, ax = plt.subplots(figsize=(12,6))
        ax.bar(d.keys(), d.values(), 0.2)
        ax.set_xlabel("Pairs")
        ax.set_ylabel("RMSD") 
        ax.set_title(f"{cr}-{nr} case with mode {mf} and frequency {fr}")
        plt.show()
    
    def plotting_cwt(self, time, cwt_s, freqs):
            
        fig, axs = plt.subplots()
        pcm = axs.pcolormesh(time, freqs, cwt_s)
        axs.set_yscale("log")
        axs.set_xlabel("Time (s)")
        axs.set_ylabel("Frequency (Hz)")
        axs.set_title("Continuous Wavelet Transform (Scalogram)")
        fig.colorbar(pcm, ax=axs)
    
    def plotting_fourier_series(self, samples, signal, cf, nf, mf, ff):
        
                    
        Xf = fftfreq(samples, 1/self.sampling_freq)[1:samples//2]
        
        fig, ax = plt.subplots()
        ax.plot(Xf, signal[1:samples//2], label=f"{cf}-{nf} case - {mf} mode - {ff} frequency")
        ax.set_xlabel("Frequency(Hz)")
        plt.legend()
        ax.set_title(f"{cf}-{nf} case - {mf} mode - {ff} frequency")
        plt.show()