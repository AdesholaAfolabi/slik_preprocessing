from .general_utils import Read_file
import pandas as pd
import numpy as np


class Clean(Read_file):
    
    '''
    This is where the data is cleaned at first. The typical issues of 
    outliers, NaN and normalization will be handled here
    
    '''
    
    def __init__(self, path, input_cols):
        
        Read_file.__init__(self, path, input_cols)
        
    def identify_cat(self, high_dim=100):
        
        """
        
        This funtion takes in the data, identify the numerical and categorical
        attributes and stores them in a list
        
        """
        
        self.read_data()
        self.num_attributes = self.data.select_dtypes(include=[np.number]).columns.tolist()
        self.cat_attributes = self.data.select_dtypes(exclude=[np.number]).columns.tolist()
        
        self.low_cat = []
        self.hash_features = []
        for item in self.cat_attributes:
            if self.data[item].nunique() > high_dim:
                #print('\n {} has a high cardinality. It has {} unique attributes'.format(item, self.data[item].nunique()))
                self.hash_features.append(item)
            else:
                self.low_cat.append(item)
        
    def remove_outliers(self):
        
        '''
        This function takes in the numerical data and removes outliers
        
        '''
        self.identify_cat()
        
        for column in self.num_attributes:
            
            self.data[column] = abs(self.data[column])
            mean = self.data[column].mean()

            #calculate the interquartlie range
            q25, q75 = np.percentile(self.data[column].dropna(), 25), np.percentile(self.data[column].dropna(), 75)
            iqr = q75 - q25

            #calculate the outlier cutoff
            cut_off = iqr * 1.5
            lower,upper = q25 - cut_off, q75 + cut_off

            #identify outliers
            outliers = [x for x in self.data[column] if x < lower or x > upper]
            
            derived_columns = ['investment_score', 'ctr_score', 'interactions_sms', 
                               'interactions_click', 'interaction_conversion', 
                               'loan_propensity']
            if column in derived_columns:
                pass
            else:
                self.data[column] = self.data[column].apply(lambda x : mean 
                                                            if x < lower or x > upper else x)
                
        return self.data
    
    def check_nan(self):
        
        """
        
        Function checks if NaN values are present in the dataset for both categorical
        and numerical variables
    
        
        """
        missing_values = self.data.isnull().sum()
        count = missing_values[missing_values>1]
#         print('\n Features       Count of missing value')
#         print('{}'.format(count))
    
    def handle_nan(self,strategy='mean',fillna='mode'):
        
        """
        
        Function handles NaN values in a dataset for both categorical
        and numerical variables
    
        Args:
            strategy: Method of filling numerical features
            fillna: Method of filling categorical features
        """
        self.identify_columns()
        self.remove_outliers()
        #self.check_nan()
        
        if strategy=='mean':
            for item in self.data[self.num_attributes]:
                self.data[item] = self.data[item].fillna(self.data[item].mean())
        if fillna == 'mode':
            for item in self.data[self.cat_attributes]:
                self.data[item] = self.data[item].fillna(self.data[item].value_counts().index[0])
        else:
            for item in self.data[self.num_attributes]:
                self.data[item] = self.data[item].fillna(fillna)
                
        return self.data
