import numpy as np 

'''
klasa zawierająca algorytm weryfikacji poprawności 
działania filtra na podstawie jego tłumień 
'''
class VerifyModule(): 

    '''
    Konstruktor klasy przyjmuje dane graniczne 
    fitra
    '''
    def __init__(self, filterList):
        

        self.filterList = filterList 
        
        self.result = False
        self.counter = 0

        self.outList = list()

        '''
        Przekształcenie danych na macierz klasy np 
        '''
        self.rowAndCols = np.shape(self.filterList)
        self.arrayOfVals = np.zeros(shape=self.rowAndCols[0], dtype=np.int8)
         

    '''
    metoda wykonująca algorytm weryfikacyjny 
    Polega on na porównywaniu, dla konkretnych wartości 
    częstotliowośc, wartości tłumienia pod względem jej 
    położenia między wartościami granicznymi 
    '''
    def verFun(self, damps, frequency):
        
        self.counter = 0

        '''
        Algorytm wykonywany jest w pętli for 
        każda iteracja oznacza kolejne wartości częstotliowści
        dla których porównywane są wartości tłumienia 
        '''        
        for i in range(len(frequency)):
        #for freq, damp in zip(frequency, damps): 
            
            if self.counter < self.rowAndCols[0]:
                
                
                if (frequency[i] == self.filterList[self.counter,0]).any():
                    
                    
                    
                    if damps[i] <= self.filterList[self.counter,1] and damps[i] >= self.filterList[self.counter,2]: 
                       
                        self.arrayOfVals[self.counter] = 1
                        self.counter = self.counter + 1
                        #print(f'{damps[i]}, {frequency[i]}')
                        self.outList.append([damps[i], frequency[i]])
                        
                    else: 

                        self.arrayOfVals[self.counter] = 0
                        self.counter = self.counter + 1
                        #print(f'{damps[i]}, {frequency[i]}')
                        self.outList.append([damps[i], frequency[i]])
                        
                else: 
                    
                    continue
                    
        
        
        #print(self.arrayOfVals)
        '''
        Weryfikacja zawartości wektora 
        zgodności danych
        oraz wrócenie rezulatatu z funkcji 
        '''
        if np.all((self.arrayOfVals == 0)):

            result = False

        else:    
            result = np.max(self.arrayOfVals) == np.min(self.arrayOfVals)
        
        

        return result, self.outList


# if __name__ == "__main__":


#     f= np.array([[0, 5, -5],[30, 5, -5],[40, 4, -6],[50, 1, -9]])
#     d = [1,2,3,4,3,1,7,8,9,10]
#     fr = [0,10,20,30,40,50,60,70,80,90]

#     ver = VerifyModule(f)

#     res = ver.verFun(d,fr)
#     print(res)
#     print(ver.arrayOfVals)

