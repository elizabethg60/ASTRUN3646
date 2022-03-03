import pandas as pd
import random
import numpy as np
import statistics
import matplotlib.pyplot as plt  

#gaussian bell curve
def pdf(x, mean,std):
    y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
    return y_out

#Transit Distance: outliers = 2 std higher than mean
df_transit_distance_max1 = pd.read_csv('df_transit_distance_max1.csv')
df_transit_distance_max2 = pd.read_csv('df_transit_distance_max2.csv')
df_transit_distance_max3 = pd.read_csv('df_transit_distance_max3.csv')
df_transit_distance_max4 = pd.read_csv('df_transit_distance_max4.csv')
df_transit_distance_max5 = pd.read_csv('df_transit_distance_max5.csv')    
# To generate an array of x-values
df_transits1 = pd.read_csv('100_transits1.csv')
df_transits2 = pd.read_csv('100_transits2.csv')
df_transits3 = pd.read_csv('100_transits3.csv')
df_transits4 = pd.read_csv('100_transits4.csv')
df_transits5 = pd.read_csv('100_transits5.csv')
x = list(df_transits1['Distance']) 
x.extend(df_transits2['Distance'])
x.extend(df_transits3['Distance'])
x.extend(df_transits4['Distance'])
x.extend(df_transits5['Distance'])
mean = np.nanmean(x)
std = np.nanstd(x)
print(mean, std)
# To generate an array of
# y-values using corresponding x-values
y = pdf(x, mean, std)
# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6)) 
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.axvline(x=mean, color='r')
plt.axvline(x=mean+std, color='b')
plt.axvline(x=mean+std*2, color='b')
plt.scatter(list(df_transit_distance_max1['Distance']), [0.0004]*len(list(df_transit_distance_max1['Distance'])), color='b')
plt.scatter(list(df_transit_distance_max2['Distance']), [0.0004]*len(list(df_transit_distance_max2['Distance'])), color='b')
plt.scatter(list(df_transit_distance_max3['Distance']), [0.0004]*len(list(df_transit_distance_max3['Distance'])), color='b')
plt.scatter(list(df_transit_distance_max4['Distance']), [0.0004]*len(list(df_transit_distance_max4['Distance'])), color='b')
plt.scatter(list(df_transit_distance_max5['Distance']), [0.0004]*len(list(df_transit_distance_max5['Distance'])), color='b')
plt.xlabel('Distance (PC)')
plt.savefig('transitdistancestd')
plt.show()

#Transit Rp: outliers = 1.5 std higher than mean
df_transit_distance_max1 = pd.read_csv('df_transit_Rp_max1.csv')
df_transit_distance_max2 = pd.read_csv('df_transit_Rp_max2.csv')
df_transit_distance_max3 = pd.read_csv('df_transit_Rp_max3.csv')
df_transit_distance_max4 = pd.read_csv('df_transit_Rp_max4.csv')
df_transit_distance_max5 = pd.read_csv('df_transit_Rp_max5.csv')   
# To generate an array of x-values
df_transits1 = pd.read_csv('100_transits1.csv')
#print(np.nanmean(list(df_transits1['Rp'])), np.nanstd(list(df_transits1['Rp'])))
df_transits2 = pd.read_csv('100_transits2.csv')
df_transits3 = pd.read_csv('100_transits3.csv')
df_transits4 = pd.read_csv('100_transits4.csv')
df_transits5 = pd.read_csv('100_transits5.csv')
x = list(df_transits1['Rp']) 
x.extend(df_transits2['Rp'])
x.extend(df_transits3['Rp'])
x.extend(df_transits4['Rp'])
x.extend(df_transits5['Rp'])
mean = np.nanmean(x)
std = np.nanstd(x)
print(mean,std)
# To generate an array of
# y-values using corresponding x-values
y = pdf(x, mean, std) 
# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6))  
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.axvline(x=mean, color='r')
plt.axvline(x=mean+std, color='b')
plt.axvline(x=mean+std*2, color='b')
plt.scatter(list(df_transit_distance_max1['Rp']), [0.4]*len(list(df_transit_distance_max1['Rp'])), color='b')
plt.scatter(list(df_transit_distance_max2['Rp']), [0.4]*len(list(df_transit_distance_max2['Rp'])), color='b')
plt.scatter(list(df_transit_distance_max3['Rp']), [0.4]*len(list(df_transit_distance_max3['Rp'])), color='b')
plt.scatter(list(df_transit_distance_max4['Rp']), [0.4]*len(list(df_transit_distance_max4['Rp'])), color='b')
plt.scatter(list(df_transit_distance_max5['Rp']), [0.4]*len(list(df_transit_distance_max5['Rp'])), color='b')
plt.xlabel('Planet Radius (Jup Radii)')
plt.savefig('transitradiusstd')
plt.show()

#Transit Mp: outliers = 2 std highers than mean
df_transit_distance_max1 = pd.read_csv('df_transit_Mp_max1.csv')
df_transit_distance_max2 = pd.read_csv('df_transit_Mp_max2.csv')
df_transit_distance_max3 = pd.read_csv('df_transit_Mp_max3.csv')
df_transit_distance_max4 = pd.read_csv('df_transit_Mp_max4.csv')
df_transit_distance_max5 = pd.read_csv('df_transit_Mp_max5.csv')   
# To generate an array of x-values
df_transits1 = pd.read_csv('100_transits1.csv')
#print(np.nanmean(list(df_transits1['Mp'])), np.nanstd(list(df_transits1['Mp'])))
df_transits2 = pd.read_csv('100_transits2.csv')
df_transits3 = pd.read_csv('100_transits3.csv')
df_transits4 = pd.read_csv('100_transits4.csv')
df_transits5 = pd.read_csv('100_transits5.csv')
x = list(df_transits1['Mp']) 
x.extend(df_transits2['Mp'])
x.extend(df_transits3['Mp'])
x.extend(df_transits4['Mp'])
x.extend(df_transits5['Mp'])
mean = np.nanmean(x)
std = np.nanstd(x)
print(mean,std)
# To generate an array of
# y-values using corresponding x-values
y = pdf(x, mean, std)
# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6))
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.axvline(x=mean, color='r')
plt.axvline(x=mean+std, color='b')
plt.axvline(x=mean+std*2, color='b')
plt.scatter(list(df_transit_distance_max1['Mp']), [0.02]*len(list(df_transit_distance_max1['Mp'])), color='b')
plt.scatter(list(df_transit_distance_max2['Mp']), [0.02]*len(list(df_transit_distance_max2['Mp'])), color='b')
plt.scatter(list(df_transit_distance_max3['Mp']), [0.02]*len(list(df_transit_distance_max3['Mp'])), color='b')
plt.scatter(list(df_transit_distance_max4['Mp']), [0.02]*len(list(df_transit_distance_max4['Mp'])), color='b')
plt.scatter(list(df_transit_distance_max5['Mp']), [0.02]*len(list(df_transit_distance_max5['Mp'])), color='b')
plt.xlabel('Planet Mass (Jup Mass)')
plt.savefig('transitmasstd')
plt.show()

#Transit Period: outliers = 1.5 std higher than mean
df_transit_distance_max1 = pd.read_csv('df_transit_period_max1.csv')
df_transit_distance_max2 = pd.read_csv('df_transit_period_max2.csv')
df_transit_distance_max3 = pd.read_csv('df_transit_period_max3.csv')
df_transit_distance_max4 = pd.read_csv('df_transit_period_max4.csv')
df_transit_distance_max5 = pd.read_csv('df_transit_period_max5.csv')  
# To generate an array of x-values
df_transits1 = pd.read_csv('100_transits1.csv')
#print(np.nanmean(list(df_transits1['Mp'])), np.nanstd(list(df_transits1['Mp'])))
df_transits2 = pd.read_csv('100_transits2.csv')
df_transits3 = pd.read_csv('100_transits3.csv')
df_transits4 = pd.read_csv('100_transits4.csv')
df_transits5 = pd.read_csv('100_transits5.csv')
x = list(df_transits1['Period']) 
x.extend(df_transits2['Period'])
x.extend(df_transits3['Period'])
x.extend(df_transits4['Period'])
x.extend(df_transits5['Period'])
mean = np.nanmean(x)
std = np.nanstd(x)
print(mean,std)
# To generate an array of
# y-values using corresponding x-values
y = pdf(x, mean, std)
# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6))
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.axvline(x=mean, color='r')
plt.axvline(x=mean+std, color='b')
plt.axvline(x=mean+std*2, color='b')
plt.scatter(list(df_transit_distance_max1['Period']), [0.002]*len(list(df_transit_distance_max1['Period'])), color='b')
plt.scatter(list(df_transit_distance_max2['Period']), [0.002]*len(list(df_transit_distance_max2['Period'])), color='b')
plt.scatter(list(df_transit_distance_max3['Period']), [0.002]*len(list(df_transit_distance_max3['Period'])), color='b')
plt.scatter(list(df_transit_distance_max4['Period']), [0.002]*len(list(df_transit_distance_max4['Period'])), color='b')
plt.scatter(list(df_transit_distance_max5['Period']), [0.002]*len(list(df_transit_distance_max5['Period'])), color='b')
plt.xlabel('Period (Days)')
plt.savefig('transitperiodtd')
plt.show()

#Transit Period: outliers = 3 std higher than mean
df_transit_distance_max1 = pd.read_csv('df_transit_duration1.csv')
df_transit_distance_max2 = pd.read_csv('df_transit_duration2.csv')
df_transit_distance_max3 = pd.read_csv('df_transit_duration3.csv')
df_transit_distance_max4 = pd.read_csv('df_transit_duration4.csv')
df_transit_distance_max5 = pd.read_csv('df_transit_duration5.csv')   
# To generate an array of x-values
df_transits1 = pd.read_csv('100_transits1.csv')
#print(np.nanmean(list(df_transits1['Mp'])), np.nanstd(list(df_transits1['Mp'])))
df_transits2 = pd.read_csv('100_transits2.csv')
df_transits3 = pd.read_csv('100_transits3.csv')
df_transits4 = pd.read_csv('100_transits4.csv')
df_transits5 = pd.read_csv('100_transits5.csv')
x = list(df_transits1['Transit_Duration']) 
x.extend(df_transits2['Transit_Duration'])
x.extend(df_transits3['Transit_Duration'])
x.extend(df_transits4['Transit_Duration'])
x.extend(df_transits5['Transit_Duration'])
mean = np.nanmean(x)
std = np.nanstd(x)
print(mean,std)
# To generate an array of
# y-values using corresponding x-values
y = pdf(x, mean, std)
# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6))  
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.axvline(x=mean, color='r')
plt.axvline(x=mean+std, color='b')
plt.axvline(x=mean+std*2, color='b')
plt.axvline(x=mean+std*3, color='b')
plt.scatter(list(df_transit_distance_max1['Transit_Duration']), [0.1]*len(list(df_transit_distance_max1['Transit_Duration'])), color='b')
plt.scatter(list(df_transit_distance_max2['Transit_Duration']), [0.1]*len(list(df_transit_distance_max2['Transit_Duration'])), color='b')
plt.scatter(list(df_transit_distance_max3['Transit_Duration']), [0.1]*len(list(df_transit_distance_max3['Transit_Duration'])), color='b')
plt.scatter(list(df_transit_distance_max4['Transit_Duration']), [0.1]*len(list(df_transit_distance_max4['Transit_Duration'])), color='b')
plt.scatter(list(df_transit_distance_max5['Transit_Duration']), [0.1]*len(list(df_transit_distance_max5['Transit_Duration'])), color='b')
plt.xlabel('Transit Duration (Hour)')
plt.savefig('transitdurationstd')
plt.show()

#RV Distance: outliers = 2 std higher than mean
df_transit_distance_max1 = pd.read_csv('df_RV_distance_max.csv')   
# To generate an array of x-values
df_non_transits = pd.read_csv('100_non_transits1.csv') 
#RV, imaging, microlensing, pulsar, ttv, (orbital brightness modulation - not plotted, missing info)
df_non_transits['method'] = [1, 3, 1, 1, 2, 1, 6, 1,1,1,1,1,3,1,1,1,1,2,1,1,2,1,2,1,1,3,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,4,1,1,1,1,1,3,1,1,3,1,1,1,1,3,1,2,3,1,1,1,1,1,5,2,4,1,1,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
df_non_RV = df_non_transits.loc[df_non_transits['method'] == 1]
x = list(df_non_RV['Distance']) 
mean = np.nanmean(x)
std = np.nanstd(x)
print(mean, std)
# To generate an array of
# y-values using corresponding x-values
y = pdf(x, mean, std)
# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6)) 
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.axvline(x=mean, color='r')
plt.axvline(x=mean+std, color='b')
plt.axvline(x=mean+std*2, color='b')
plt.scatter(list(df_transit_distance_max1['Distance']), [0.0015]*len(list(df_transit_distance_max1['Distance'])), color='b')
plt.xlabel('RV Distance (PC)')
plt.savefig('RVdistancestd')
plt.show()

#RV Rp: outliers = under mean
df_transit_distance_max1 = pd.read_csv('df_RV_Rp.csv')  
# To generate an array of x-values
df_non_transits = pd.read_csv('100_non_transits1.csv') 
#RV, imaging, microlensing, pulsar, ttv, (orbital brightness modulation - not plotted, missing info)
df_non_transits['method'] = [1, 3, 1, 1, 2, 1, 6, 1,1,1,1,1,3,1,1,1,1,2,1,1,2,1,2,1,1,3,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,4,1,1,1,1,1,3,1,1,3,1,1,1,1,3,1,2,3,1,1,1,1,1,5,2,4,1,1,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
df_non_RV = df_non_transits.loc[df_non_transits['method'] == 1]
x = list(df_non_RV['Rp'])
mean = np.nanmean(x)
std = np.nanstd(x)
print(mean,std)
# To generate an array of
# y-values using corresponding x-values
y = pdf(x, mean, std)
# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6)) 
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.axvline(x=mean, color='r')
plt.axvline(x=mean-std, color='b')
plt.axvline(x=mean-std*2, color='b')
plt.scatter(list(df_transit_distance_max1['Rp']), [0.4]*len(list(df_transit_distance_max1['Rp'])), color='b')
plt.xlabel('RV Planet Radius (Jupiter Radii)')
plt.savefig('RVradiistd')
plt.show()

#RV Mp: outlier = 5 std higher than mean
df_transit_distance_max1 = pd.read_csv('df_RV_Mp_max.csv')
# To generate an array of x-values
df_non_transits = pd.read_csv('100_non_transits1.csv') 
#RV, imaging, microlensing, pulsar, ttv, (orbital brightness modulation - not plotted, missing info)
df_non_transits['method'] = [1, 3, 1, 1, 2, 1, 6, 1,1,1,1,1,3,1,1,1,1,2,1,1,2,1,2,1,1,3,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,4,1,1,1,1,1,3,1,1,3,1,1,1,1,3,1,2,3,1,1,1,1,1,5,2,4,1,1,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
df_non_RV = df_non_transits.loc[df_non_transits['method'] == 1]
x = list(df_non_RV['Mp'])
mean = np.nanmean(x)
std = np.nanstd(x)
print(mean,std)
# To generate an array of
# y-values using corresponding x-values
y = pdf(x, mean, std)
# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6)) 
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.axvline(x=mean, color='r')
plt.axvline(x=mean+std, color='b')
plt.axvline(x=mean+std*2, color='b')
plt.axvline(x=mean+std*3, color='b')
plt.axvline(x=mean+std*4, color='b')
plt.axvline(x=mean+std*5, color='b')
plt.scatter(list(df_transit_distance_max1['Mp']), [0.04]*len(list(df_transit_distance_max1['Mp'])), color='b')
plt.xlabel('RV Planet Mass (Jupiter Mass)')
plt.savefig('RVmassstd')
plt.show()

#RV Period: outlier = 8 std higher than mean
df_transit_distance_max1 = pd.read_csv('df_RV_period_max.csv')  
# To generate an array of x-values
df_non_transits = pd.read_csv('100_non_transits1.csv') 
#RV, imaging, microlensing, pulsar, ttv, (orbital brightness modulation - not plotted, missing info)
df_non_transits['method'] = [1, 3, 1, 1, 2, 1, 6, 1,1,1,1,1,3,1,1,1,1,2,1,1,2,1,2,1,1,3,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,4,1,1,1,1,1,3,1,1,3,1,1,1,1,3,1,2,3,1,1,1,1,1,5,2,4,1,1,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
df_non_RV = df_non_transits.loc[df_non_transits['method'] == 1]
x = list(df_non_RV['Period'])
mean = np.nanmean(x)
std = np.nanstd(x)
print(mean,std)
# To generate an array of
# y-values using corresponding x-values
y = pdf(x, mean, std)
# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6))  
plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.axvline(x=mean, color='r')
plt.axvline(x=mean+std, color='b')
plt.axvline(x=mean+std*2, color='b')
plt.axvline(x=mean+std*3, color='b')
plt.axvline(x=mean+std*4, color='b')
plt.axvline(x=mean+std*5, color='b')
plt.axvline(x=mean+std*6, color='b')
plt.axvline(x=mean+std*7, color='b')
plt.axvline(x=mean+std*8, color='b')
plt.scatter(list(df_transit_distance_max1['Period']), [0.00004]*len(list(df_transit_distance_max1['Period'])), color='b')
plt.xlabel('RV Period (Days)')
plt.savefig('RVperiodstd')
plt.show()
