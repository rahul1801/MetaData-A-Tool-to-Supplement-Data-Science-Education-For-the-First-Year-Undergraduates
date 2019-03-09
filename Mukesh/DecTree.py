import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DTClassifier:
    
    def entropy(self, y):
        
        """Returns the Shannon entropy of a target feature."""
        
        classes, counts = np.unique(y,return_counts=True)
        ent = 0
        sum_counts = np.sum(counts)
        for i in range(len(counts)):
            prob = (counts[i]/sum_counts)
            ent += (prob*np.log2(prob))
        ent *= -1
        return ent
    
    def info_gain(self, X, split_attr_name, target_attr_name):
        
        """Returns the Information Gain if X is split based on split_attr_name."""
        
        initial_ent = self.entropy(X[target_attr_name])
        classes, counts = np.unique(X[split_attr_name], return_counts=True)
        sum_counts = np.sum(counts)
        split_ent = 0
        for i in range(len(counts)):
            split_ent += (counts[i]/sum_counts)*self.entropy(X.where(X[split_attr_name]==classes[i]).dropna()[target_attr_name])
        IG = initial_ent - split_ent
        return IG
    
    def build(self, X, org_X, attr_names, target_attr_name, parent_node_class=None):
        
        """Build a decision tree using the ID3 algorithm."""
        
        X_classes, X_counts = np.unique(X[target_attr_name],return_counts=True)
        org_classes, org_counts = np.unique(org_X[target_attr_name],return_counts=True)
        
        # Only one target class is present
        if len(X_classes) <= 1:
            return X_classes[0]
        
        #No data examples
        if len(X)==0:
            return org_classes[np.argmax(org_counts)]
        
        # No more features to split
        if len(attr_names)==0:
            return parent_node_class
        
        # Set mode of target_attr
        parent_node_class = X_classes[np.argmax(X_counts)]
        
        # Find the feature with max. Info Gain
        info_gain_values = []
        for attr in attr_names:
            info_gain_values.append(self.info_gain(X, attr, target_attr_name))
        split_attr = attr_names[np.argmax(info_gain_values)]
        
        # Create subtree structure
        tree = {split_attr:{}}
        
        # Remove splitting attribute from list of attributes
        attr_names = [attr for attr in attr_names if attr != split_attr]
        
        # Add branch for each unique value of splitting attribute
        for val in np.unique(X[split_attr]):
            
            # Create sub dataset
            sub_X = X.where(X[split_attr]==val).dropna()
            
            # Build each subtree
            subtree = self.build(sub_X, org_X, attr_names, target_attr_name, parent_node_class)
            
            # Add this subtree to original tree
            tree[split_attr][val] = subtree
            
        return tree
    
    def evaluate(self, query, tree, default=None):
        
        """Predicts the Target attr value for a given instance, which is a dictionary {attr_name:attr_val,...}."""
        
        for attr in query.keys():
            if attr in tree.keys():
                
                try:
                    subtree = tree[attr][query[attr]]
                except:
                    return default
                
                # Check if next hop has a subtree or leaf node
                if isinstance(subtree,dict):
                    return self.evaluate(query, subtree, default)
                else:
                    return subtree
                
    def predict(self, X, tree, target_attr_name, default=None):
        
        """Predicts the target features for a given dataframe X."""
        
        predicted = []
        X_dict = X.to_dict("records")
        for i in range(len(X_dict)):
            query = X_dict[i]
            query.pop(target_attr_name, None)
            predicted.append(self.evaluate(query, tree, default))
        return np.array(predicted)
                
    def fit(self, X, attr_names, target_attr_name):
        
        """Fits a decision tree to an X(dataframe) and returns it."""
        
        attr_names = [attr for attr in attr_names if attr != target_attr_name]
        tree = self.build(X, X, attr_names, target_attr_name)
        return tree