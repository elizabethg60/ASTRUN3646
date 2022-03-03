import pandas as pd
import random
import numpy as np
import statistics
import matplotlib.pyplot as plt   

#importing dataframes with all information from website
transits = pd.read_csv('transits.csv')
non_transits = pd.read_csv('non_transits.csv') 

#creating 5 random samples dataframes of 100 exoplanets each 
#these can be found in the github 
for i in range(1,6):
    df_transits = transits.sample(n=100)
    df_non_transits = non_transits.sample(n=100)
    df_transits.to_csv('100_transits{}.csv'.format(i))  
    df_non_transits.to_csv('100_non_transits{}.csv'.format(i)) 
    
#analysis of transit, rv, and image method: Planets' Distance vs Planets' Radius
#bias boundaries for radius and distance for each method
transit_max_radii = 1 #jup radii
rv_min_radii = 1
image_min_radii = 1
image_max_radii = 1.5
transit_max_distance = 1500
rv_max_distance = 300
image_max_distance = 300
#plotting Distance vs Radius coded for transiting vs non
for i in range(1, 6):
    df_transits = pd.read_csv('100_transits{}.csv'.format(i))
    df_non_transits = pd.read_csv('100_non_transits{}.csv'.format(i)) 
    plt.scatter(np.log10(df_transits['Distance']), np.log10(df_transits['Rp']), color = 'r', label = 'Transits')
    plt.scatter(np.log10(df_non_transits['Distance']), np.log10(df_non_transits['Rp']), color = 'b', alpha = 0.1, label = 'No Transits')
    plt.legend()
    plt.xlabel('Distance to Host Stars (Log PC)')
    plt.ylabel('Planet Radius (Log Jupiter Radii)')
    plt.title('Distance v Planet Radius {}'.format(i))
    plt.savefig('distancevradius{}.png'.format(i))
    plt.show()
    #collecting planets outside bias for each method for each property 
    if i == 1:
        df_non_transits['method'] = [1, 3, 1, 1, 2, 1, 6, 1,1,1,1,1,3,1,1,1,1,2,1,1,2,1,2,1,1,3,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,4,1,1,1,1,1,3,1,1,3,1,1,1,1,3,1,2,3,1,1,1,1,1,5,2,4,1,1,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        df_non_RV = df_non_transits.loc[df_non_transits['method'] == 1]
        df_non_imaging = df_non_transits.loc[df_non_transits['method'] == 2]
        df_non_RV.loc[df_non_RV['Rp'] < rv_min_radii].to_csv('df_RV_Rp.csv') 
        df_non_imaging.loc[df_non_imaging['Rp'] > image_max_radii].to_csv('df_image_Rp_max.csv') 
        df_non_imaging.loc[df_non_imaging['Rp'] < image_min_radii].to_csv('df_image_Rp_min.csv') 
        df_non_RV.loc[df_non_RV['Distance'] > rv_max_distance].to_csv('df_RV_distance_max.csv')
        df_non_imaging.loc[df_non_imaging['Distance'] > image_max_distance].to_csv('df_image_distance_max.csv')
    df_transits.loc[df_transits['Distance'] > transit_max_distance].to_csv('df_transit_distance_max{}.csv'.format(i))
    df_transits.loc[df_transits['Rp'] > transit_max_radii].to_csv('df_transit_Rp_max{}.csv'.format(i))  
    
#analysis of transit, rv, and image method: period and planet mass
#bias boundaries for mass and period for each method
transit_max_period = 100 #days -outliers will be planets with higher duration 
rv_min_period = 10
rv_max_period = 10**4
image_min_period = 10**4
image_max_period = 10**5
transit_min_mass = 10**(-3) #jup mass
transit_max_mass = 13
rv_min_mass = 10**(-2)
rv_max_mass = 13
image_min_mass = 1
image_max_mass = 13
#plotting Period vs Mass coded for transiting vs non
for i in range(1, 6):
    df_transits = pd.read_csv('100_transits{}.csv'.format(i))
    df_non_transits = pd.read_csv('100_non_transits{}.csv'.format(i)) 
    plt.scatter(np.log10(df_transits['Period']), np.log10(df_transits['Mp']), color = 'r', label = 'Transits')
    plt.scatter(np.log10(df_non_transits['Period']), np.log10(df_non_transits['Mp']), color = 'b', alpha = 0.1, label = 'No Transits')
    plt.legend()
    plt.xlabel('Period (Log Days)')
    plt.ylabel('Planet Mass (Log Jupiter Masses)')
    plt.title('Period v Planet Mass {}'.format(i))
    plt.savefig('periodvmass{}'.format(i))
    plt.show()
    #collecting planets outside bias for each method for each property 
    if i == 1:
        df_non_transits['method'] = [1, 3, 1, 1, 2, 1, 6, 1,1,1,1,1,3,1,1,1,1,2,1,1,2,1,2,1,1,3,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,4,1,1,1,1,1,3,1,1,3,1,1,1,1,3,1,2,3,1,1,1,1,1,5,2,4,1,1,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        df_non_RV = df_non_transits.loc[df_non_transits['method'] == 1]
        df_non_imaging = df_non_transits.loc[df_non_transits['method'] == 2]
        df_non_RV.loc[df_non_RV['Period'] > rv_max_period].to_csv('df_RV_period_max.csv')
        df_non_RV.loc[df_non_RV['Period'] < rv_min_period].to_csv('df_RV_period_min.csv')
        df_non_imaging.loc[df_non_imaging['Period'] > image_max_period].to_csv('df_image_period_max.csv')
        df_non_imaging.loc[df_non_imaging['Period'] < image_min_period].to_csv('df_image_period_min.csv')
        df_non_RV.loc[df_non_RV['Mp'] > rv_max_mass].to_csv('df_RV_Mp_max.csv')
        df_non_RV.loc[df_non_RV['Mp'] < rv_min_mass].to_csv('df_RV_Mp_min.csv')
        df_non_imaging.loc[df_non_imaging['Mp'] > image_max_mass].to_csv('df_image_Mp_max.csv')
        df_non_imaging.loc[df_non_imaging['Mp'] < image_min_mass].to_csv('df_image_Mp_min.csv')
    df_transits.loc[df_transits['Period'] > transit_max_period].to_csv('df_transit_period_max{}.csv'.format(i))
    df_transits.loc[df_transits['Mp'] > transit_max_mass].to_csv('df_transit_Mp_max{}.csv'.format(i))
    df_transits.loc[df_transits['Mp'] < transit_min_mass].to_csv('df_transit_Mp_min{}.csv'.format(i)) 
    
#analysis of transit method: transit duration 
transit_max_duration = 12 #hours - outliers will be planets with higher duration 
#Transiting Planets' Duration Histograms 
for i in range(1, 6):
    df_transits = pd.read_csv('100_transits{}.csv'.format(i))
    plt.hist((df_transits['Transit_Duration']), color = 'r', label = 'Transits')
    plt.xlabel('Transit Duration (Hr)')
    plt.ylabel('Frequency')
    plt.title('Transit Duration {}'.format(i))
    plt.savefig('transitduration{}.png'.format(i))
    plt.show()
    df_transits.loc[df_transits['Transit_Duration'] > transit_max_duration].to_csv('df_transit_duration{}.csv'.format(i))
    
#plots of non transiting methods for sample one only
df_transits = pd.read_csv('100_transits1.csv')
df_non_transits = pd.read_csv('100_non_transits1.csv') 
#RV, imaging, microlensing, pulsar, ttv, (orbital brightness modulation - not plotted, missing info)
df_non_transits['method'] = [1, 3, 1, 1, 2, 1, 6, 1,1,1,1,1,3,1,1,1,1,2,1,1,2,1,2,1,1,3,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,1,1,1,1,4,1,1,1,1,1,3,1,1,3,1,1,1,1,3,1,2,3,1,1,1,1,1,5,2,4,1,1,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
df_non_RV = df_non_transits.loc[df_non_transits['method'] == 1]
df_non_imaging = df_non_transits.loc[df_non_transits['method'] == 2]
df_non_lensing = df_non_transits.loc[df_non_transits['method'] == 3]
df_non_pulsar = df_non_transits.loc[df_non_transits['method'] == 4]
df_non_ttv = df_non_transits.loc[df_non_transits['method'] == 5]
df_non_bright = df_non_transits.loc[df_non_transits['method'] == 6]
plt.scatter(np.log10(df_transits['Period']), np.log10(df_transits['Mp']), color = 'r', alpha = 0.1, label = 'Transits')
plt.scatter(np.log10(df_non_RV['Period']), np.log10(df_non_RV['Mp']), color = 'b', label = 'RV')
plt.scatter(np.log10(df_non_imaging['Period']), np.log10(df_non_imaging['Mp']), color = 'g',label = 'Image')
plt.scatter(np.log10(df_non_lensing['Period']), np.log10(df_non_lensing['Mp']), color = 'm', label = 'G Microlensing')
plt.scatter(np.log10(df_non_pulsar['Period']), np.log10(df_non_pulsar['Mp']), color = 'y', label = 'Pulsar')
plt.scatter(np.log10(df_non_ttv['Period']), np.log10(df_non_ttv['Mp']), color = 'k', label = 'TTV')
plt.legend()
plt.xlabel('Period (Log Days)')
plt.ylabel('Planet Mass (Log Jupiter Masses)')
plt.title('Period v Planet Mass 1')
plt.savefig('periodvmass_method')
plt.show()

plt.scatter(np.log10(df_transits['Distance']), np.log10(df_transits['Rp']), color = 'r', alpha = 0.1, label = 'Transits')
plt.scatter(np.log10(df_non_RV['Distance']), np.log10(df_non_RV['Rp']), color = 'b', label = 'RV')
plt.scatter(np.log10(df_non_imaging['Distance']), np.log10(df_non_imaging['Rp']), color = 'g',label = 'Image')
plt.scatter(np.log10(df_non_lensing['Distance']), np.log10(df_non_lensing['Rp']), color = 'm', label = 'G Microlensing')
plt.scatter(np.log10(df_non_pulsar['Distance']), np.log10(df_non_pulsar['Rp']), color = 'y', label = 'Pulsar')
plt.scatter(np.log10(df_non_ttv['Distance']), np.log10(df_non_ttv['Rp']), color = 'k', label = 'TTV')
plt.legend()
plt.xlabel('Distance to Host Stars (Log PC)')
plt.ylabel('Planet Radius (Log Jupiter Radii)')
plt.title('Distance v Planet Radius 1')
plt.savefig('distancevradius_method.png')
plt.show()
