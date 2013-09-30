
import sklearn as skl
import skimage as ski
import numpy as np

class imageToClassify:
    
    def __init__(self,image):
        
        self.image = image
        #self.reds,self.greens,self.blues = np.empty(np.size(self.image[...,0])),np.empty(np.size(self.image[...,1])),\
        #    np.empty(np.size(self.image[...,2]))
        
    def colors(self,color):
        
        '''Returns the RGB layers of the image based on the color flag.  'Color' can be 'r' or 'red', 'g' or 'green',
        'b' or 'blue'.'''
        
        reds = self.image[...,0]
        greens = self.image[...,1]
        blues = self.image[...,2]
        
        if color == 'red' or color == 'r':
            return reds
        elif color == 'g' or color == 'green':
            return greens
        elif color == 'b' or color == 'bue':
            return blues
        
    def shape(self):
        
        '''Returns a tuple of the shape of the image array, in 3-dimensions.'''
        
        shp = np.shape(self.image)
        return shp
    
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
        
        corners = ft.corner_foerstner(self.image)
        
        return corners