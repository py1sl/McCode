import re
'''
Generic Node and data types for assembling a graph that can be plotted 
using various mcplot frontend implementations.
'''
class Data1D(object):
    def __init__(self):
        self.component = ''
        self.filename = ''
        self.title = ''
        self.xlabel = ''
        self.ylabel = ''
        
        self.xvar = ''
         
        self.yvar = () # pair
        self.values = () # triplet
        self.statistics = ''
        
        self.statistics_title = '' # generated from the three above
        
    def load(self, text):
        try:
            '''# component: Ldetector'''
            m = re.search('\# component: ([\w]+)\n', text)
            self.component = m.group(1)
            
            '''# filename: Edet.dat'''
            m = re.search('\# filename: ([\w\.]+)\n', text)
            self.filename = m.group(1)
            
            '''# title: Wavelength monitor'''
            m = re.search('\# title: ([\w ]+)\n', text)
            self.title = m.group(1)
            
            '''# xlabel: Wavelength [AA]'''
            m = re.search('\# xlabel: ([\[\]\w ]+)\n', text)
            self.xlabel = m.group(1)
            
            '''# ylabel: Intensity'''
            m = re.search('\# ylabel: ([\w]+)\n', text)
            self.ylabel = m.group(1)
            
            '''# yvar: (I,I_err)'''
            m = re.search('\# xvar: ([\w]+)\n', text)
            self.xvar = m.group(1)
            
            '''# yvar: (I,I_err)'''
            m = re.search('\# yvar: \(([\w]+),([\w]+)\)\n', text)
            self.yvar = (m.group(1), m.group(2))
            
            '''# values: 6.72365e-17 4.07766e-18 4750'''
            m = re.search('\# values: ([\d\-\.e]+) ([\d\-\.e]+) ([\d\-\.e]+)\n', text)
            self.values = (float(m.group(1)), float(m.group(2)), float(m.group(3)))
            
            '''# statistics: X0=5.99569; dX=0.0266368;'''
            m = re.search('\# statistics: X0=([\d\.\-e]+); dX=([\d\.\-e]+);\n', text)
            self.statistics = 'X0=%f; dX=%f;' % (float(m.group(1)), float(m.group(2)))
                        
        except:
            print('Data1D load error.)
            raise e

class Data2D(object):
    ''' not implemented '''
    def __init__(self):
        self.title = ''

class DataMultiHeader(object):
    ''' not implemented '''
    def __init__(self):
        self.title = ''

'''
Plot graph node types have parent, primaries and secondaries, corresponding to whether 
"back", "click" or "ctr-click" is used to navigate.
Descendents also have a data pointer, which is an instance or a list.
'''
class PlotNode(object):
    ''' 
    Base class for plot graph nodes. 
    Parent is set implicitly on "primary" and "secondary" child node lists.
    '''
    def __init__(self):
        self.parent = None
    
    def set_primaries(self, node_lst):
        self.primaries = node_lst
        for node in node_lst:
            node.parent = self
    def get_primaries(self):
        return self.primaries
    
    def set_secondaries(self, node_lst):
        self.secondaries = node_lst
        for node in node_lst: 
            node.parent = self
    def get_secondaries(self):
        return self.secondaries
    
    def get_parent(self):
        return self.parent

class PNMultiple(PlotNode):
    def __init__(self, header, data_lst):
        self.header = header
        self.data_lst = data_lst

class PNSingle(PlotNode):
    def __init__(self, data):
        self.data = data

