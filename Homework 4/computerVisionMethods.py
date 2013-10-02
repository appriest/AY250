
class imageToClassify:
    
    '''
    This class takes an image to be operated on and the member functions compute image characteristics.
    
    Member functions:
    
        imageToClassify.colors(color):
            'color' is a string that chooses which color layer (RGB) to return and the return is an array containing the layer requested
            
        imageToClassify.shape():
            Returns the shape of the image in 3 dimensions
            
        imageToClassify.cross_corr():
            Returns a 3D array of cross correlations between each of the color layers in the order RG, RB, GB.
            
        imageToClassify.corner_det():
            Corner detection in the image.  Returns an array of tuples with the locations of corners.
    '''
    
    def __init__(self,image):
        
        self.image = image
        #self.reds,self.greens,self.blues = np.empty(np.size(self.image[...,0])),np.empty(np.size(self.image[...,1])),\
        #    np.empty(np.size(self.image[...,2]))
        
    def colors(self,color):
        
        '''Returns the RGB layers of the image based on the color flag.  'Color' can be 'r' or 'red', 'g' or 'green',
        'b' or 'blue'.'''
        
        import numpy as np
        
        reds = self.image[...,0]
        greens = self.image[...,1]
        blues = self.image[...,2]
        
        if color == 'red' or color == 'r':
            return np.mean(reds)
        elif color == 'g' or color == 'green':
            return np.mean(greens)
        elif color == 'b' or color == 'bue':
            return np.mean(blues)
        
    def size(self):
        
        '''Returns a tuple of the shape of the image array, in 3-dimensions.'''
        
        shp = np.shape(self.image)
        for dimsize in shp:
            sz *= dimsize
        return sz
    
    def cross_corr(self):
        
        '''Computes and returns the cross correlation of the three color channels as an array.'''
        
        import scipy.signal as sg
        import numpy as np
        corr_rg = sg.fftconvolve(self.image[...,0],self.image[::-1,::-1,1],mode = 'same')
        corr_rb = sg.fftconvolve(self.image[...,0],self.image[::-1,::-1,2],mode = 'same')
        corr_gb = sg.fftconvolve(self.image[...,1],self.image[::-1,::-1,2],mode = 'same')
        
        return np.ndarray([corr_rg,corr_rb,corr_gb])
    
    def corner_det(self):
        
        '''Finds corners within the image and returns the locations of the detected corners.'''
        
        import skimage.feature as ft
        
        corners = ft.corner_foerstner(median(self.image,axis=2))
        
        return len(corners)
    
    def extract_hog(self):
        
        '''Returns the histogram of oriented gradients for the image.'''
        
        import skimage.feature as ft
        import numpy as np
        
        hog = ft.hog(np.median(self.image,axis=2))
        
        return hog
    
    def extract_canny(self):
        
        '''Returns the number of edges as calculated with a canny filter.'''
        
        import skimage.feature as ft
        
    def delete_im(self):
        
        self.im = none
    

import os
import os.path
import scipy.ndimage as img
import sklearn as skl
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import skimage.data as skiData
import numpy as np

path = os.getcwd()
path += '/50_categories/'
features = []
i = 0

for dirs in os.listdir(path):
    if dirs[0] != '.':
        cat_path = path + dirs +'/'
        print 'Loading files from path:', cat_path
        for files in os.listdir(cat_path):
            if files[0] != '.' and os.path.isfile(cat_path+'/'+files):
                i += 1
                im_path = cat_path + '/' + files
                im = skiData.imread(im_path)
                im_obj = imageToClassify(im)
                features[i,0] = dirs
                features[i,1] = imageToClassify.size()
                
featSize = np.shape(features)[0]
rf1 = randomForestClassifier(n_estimators=1000,n_jobs=-1)
rf1.fit(features[0:0.9*featSize,1],features[0:0.9*featSize,0])
c_predict = rf1.predict(features[0.9*featSize:featSize,1])
metrics.accuracy_score(features[0.9*featSize:featSize,0],c_predict)