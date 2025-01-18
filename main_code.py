# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:50:19 2024

@author: velis
"""

import Preprocessing_class
import Plotting_class
import Analysis_Class
import numpy as np

ids_healthy = [1622, 1623,1624,1625,1626,1628,1629,1630,1631,
       1632,1673,1674,1675,1676,1677,1699,1700,1701,
       1702,1703,1704,1705,1707,1708,1709,1710,1711,
       1712,1713,1714,1715,1716,1717,1718,1719,1720,
       1721,1722,1723,1724,1725,1726,1727,1728,1729,
       1733,1734,1735,1736,1737,1738,1739,1740,1741,
       1742,1749,1750,1751,1752,1753,1754,1755,1756,
       1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,
       1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,
       1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,
       1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,
       1797,1798,1799,1800,1801,1802,1803,1804,1805,1806,1807,
       1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,
       1821,1822,1823,1825,1826,1827,1828,1829,1830,1831,1832,1833,1834,
       1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,
       1848,1849,1850,1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,
       1862,1863,1864,1865,1866,1867,1868,1869,1870,1871,1872,1873,1874,1875,
       1876,1877,1878,1879,1880,1881,1882,1883,1884,1885,1886,1887,1888,1889,
       1890,1891,1892,1893,1894,1895,1896,1897,1898,1899,1900,1901,1902]

ids_damaged = [1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,
               1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,
               1927,1928,1929,1930]

modes = [0, 1]
freqs = [24, 30, 37, 14, 18]
sampling_freq = 195e3
samples = 2507
time = np.linspace(0,(1/sampling_freq)*(samples-1),2507)
print(len(time))

if __name__ == "__main__": 
    
    obj_preprocessing = Preprocessing_class.Preprocessing_data(modes=modes, freqs=freqs) 
    healthy_dictionaries =  obj_preprocessing.constructing_pandas_dataframes(ids_healthy) 
    damaged_dictionaries =  obj_preprocessing.constructing_pandas_dataframes(ids_damaged)
    
    obj_analysis = Analysis_Class.Time_freq_domain_chars(samples, sampling_freq, healthy_dictionaries, damaged_dictionaries, ids_healthy, ids_damaged, modes, freqs)
    obj_plotting = Plotting_class.Plotting_the_data(ids_healthy, ids_damaged, healthy_dictionaries, damaged_dictionaries, modes, freqs, sampling_freq)
    
    choice = int(input("Please select what you want to do - 0-1-2"))
    
    
    
    match choice:
        
        case 0: 
            
            rmsd_values = obj_analysis.rmsd_analysis()
            obj_plotting.plotting_rmsd(rmsd_values[1], rmsd_values[2], rmsd_values[3], rmsd_values[4], rmsd_values[0])
        
        case 1: 
            
            fourier_values = obj_analysis.fourier_analysis()
            obj_plotting.plotting_fourier_series(samples, fourier_values[0], fourier_values[1], fourier_values[2], fourier_values[3], fourier_values[4])
        
        case 3: 
            
            cwt_values = obj_analysis.cwt_calculations()
            print(cwt_values[0].shape)
            print(cwt_values[1].shape)
            obj_plotting.plotting_cwt(time, cwt_values[0], cwt_values[1])
        
        case 4:
            
            obj_plotting.plotting_over_cases_same_frequency()







        
        

    


