import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import bisect


class PrCA():
        
    def centre_scale(self,X):
        """Returns a centre-scaled matrix (column-wise)."""
        self.X_mean = np.mean(X,axis=0)
        X = X - self.X_mean
        return X
    
    def find_cov(self,X,m):
        """Returns a covariance matrix corresponding to X."""
        return np.dot(X.T,X)/m
    
    def find_eigen(self,cov):
        """Returns eigen values and eigen vectors for a given matrix."""
        eval, evec = np.linalg.eigh(cov)
        idx = np.argsort(abs(eval))[::-1]
        evec = evec[:,idx]
        eval = eval[idx]
        return (eval,evec)
    
    def fit(self,X):
        """Finds out the eigen values and eigen vectors of the corresponding covariance matrix."""
        self.X = X
        self.XS = self.centre_scale(self.X)
        self.cov = self.find_cov(self.XS,self.XS.shape[0])
        self.eval, self.evec = self.find_eigen(self.cov)
    
    def eigen_analysis(self):
        """(No. of components VS Variance retained) plot."""
        self.var_ret = np.array([])
        self.var_ret = np.append(self.var_ret,[self.eval[0]])
        for each in self.eval[1:]:
            self.var_ret = np.append(self.var_ret,[each + self.var_ret[-1]])
        self.var_ret = np.divide(self.var_ret,sum(self.eval))
        self.var_ret = np.append([0],self.var_ret)
        eval_ret = np.arange(0,len(self.eval)+1)
        self.line_plot(eval_ret,self.var_ret,0, "No. of components retained", "Variance% Retained")
            
    def line_plot(self, x, y, y_bottom, xlabel, ylabel):
        """Draws a line plot for the given info."""
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x,y)
        ax.set_ylim(bottom=y_bottom)
        ax.set(xlabel=xlabel,ylabel=ylabel)
        text=ax.text(0,0, "", va="bottom", ha="left")
        cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
    
    def onclick(self,event):
        """Displays x and y co-ordinates corresponding to the location of the mouse."""
        tx = 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % (event.button, event.x, event.y, event.xdata, event.ydata)
        text.set_text(tx)
    
    def retain_var(self,num):
        """Returns the eigen coefficients by retaining 'num' variance."""
        self.idx = bisect.bisect_left(self.var_ret,num)
        self.Xh = np.dot(self.XS,self.evec[:,:self.idx+1])
        return self.Xh
    
    def save_eigenfaces(self,path,width,height):
        """Save the eigen faces in a new folder."""
        for i in range(self.idx+1):
            plt.imsave(path+str(i)+'.png',self.evec[:,i].reshape((width,height)),cmap=cm.gray)
            
    def save_coeff(self,path):
        """Save the coeff corresponding to each image."""
        np.save(path+'coeff',self.Xh)
    
    def load_coeff(self,path):
        """Load the coeff corresponding to each image."""
        self.Xh = np.load(path+'coeff.npy')
    
    def restore(self):
        """Reconstruct new X."""
        self.Xr = np.dot(self.Xh,self.evec[:,:self.idx+1].T)
        self.Xr = self.Xr + self.X_mean
        return self.Xr
    
    def error(self):
        """Returns reconstruction error per element."""
        self.err = 0
        for i in range(self.Xr.shape[0]):
            for j in range(self.Xr.shape[1]):
                self.err += abs(self.Xr[i][j] - self.X[i][j])
        self.err /= (self.Xr.shape[0]*self.Xr.shape[1])
        return self.err