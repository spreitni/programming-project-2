import random


def bestFit(physicalArray, arrayOfValuesToAdd):
    #adds the next 40 block requests
    count = 0
    memoryUlitilization = 0
    numOfPids = 40
    processArray = [0 for x in range(numOfPids)]
    #print(processArray)
    for i in range(numOfPids):
        value= random.randint(1,8)
    # vertical print of the processes print(value)
        processArray[i] = value
    #print(processArray)
    
    #start of bestFit
    #remove call
    #print("start of remove and allocations")
    for i in range(0,40):                      
        release = random.randint(1,8)           # release
        try:
            while True:
                physicalArray.remove(release)
        except ValueError:
            pass
        #print(physicalArray)                    # release
                                                
        #print(release)
                                                # allocate
        processToAllocate = 0
        allcoate = processArray[processToAllocate]
        spot= random.randint(0,63)
        for a in range(0,processArray[i]):
            count = count + 1
            memoryUlitilization = memoryUlitilization + physicalArray.count(0)
            physicalArray.insert(spot,processArray[i])
    print("best fit steps ")
    print(count)
    print("best fit memory ulitiliation ")
    print(memoryUlitilization / count)
    #physicalArray.remove(release)
        
        #for i in range(len(physicalArray)):
        #    if(physicalArray[i]==release):
        #        physicalArray[i] = 0
        #for i in range(len(processArray)):
            #allocateSpot = random.randint(0,63)
            #finds a spot where it fits
            
                
            #for a in range(0,processArray[i]):            
                #physicalArray.insert(allocateSpot,processArray[i]) 
   
    
    
def worstFit(physicalArray,  arrayOfValuesToAdd):
    count = 0
    memoryUlitilization = 0
    numOfPids = 40
    processArray = [0 for x in range(numOfPids)]
    #print(processArray)
    for i in range(numOfPids):
        value= random.randint(1,8)
    # vertical print of the processes print(value)
        processArray[i] = value
    #print(processArray)
    
    #start of bestFit
    #remove call
    #print("start of remove and allocations")
    for i in range(0,40):                      
        release = random.randint(1,8)           # release
        try:
            while True:
                physicalArray.remove(release)
        except ValueError:
            pass
        #print(physicalArray)                    # release
                                                
        #print(release)
                                                # allocate
        processToAllocate = 0
        allcoate = processArray[processToAllocate]
        spot= random.randint(0,63)
        if(physicalArray[spot] == 0):
            for a in range(0,processArray[i]):
                count = count + 1
                memoryUlitilization = memoryUlitilization +  physicalArray.count(0)
                physicalArray.insert(spot,processArray[i])
                
        else:
            T=True
            while(T==True):
                spot= random.randint(0,63)
                if(physicalArray[spot] == 0):
                    for a in range(0,processArray[i]):
                        physicalArray.insert(spot,processArray[i])
                        count = count + 1
                        memoryUlitilization = memoryUlitilization +  physicalArray.count(0)
                        T=False
                memoryUlitilization = memoryUlitilization +  physicalArray.count(0)
                  
    print("worst fit steps ")
    print(count)
    print("worst fit memory ulitization" )
    print(memoryUlitilization /count  )
def arrayBuilder(physicalMemoryArray, processArray): #creates an array of pid size
    #print (physicalMemory)
    #print (processArray)
    #spotInArray = 0
    
    for i in range(len(processArray)):
        spot= random.randint(0,63)
        for a in range(0,processArray[i]):
            
            physicalMemoryArray.insert(spot,processArray[i])
            #spotInArray = spotInArray + 1
    #print("****************start of memory allocation*********************")
    #print(physicalMemoryArray)
    #print("****************end of memory allocation***********************")
    bestFit(physicalMemoryArray,processArray)
    worstFit(physicalMemoryArray,processArray)    
        #physicalMemoryArray.insert(spotInArray,processArray[i] )
        #spotInArray = spotInArray + 1
    #print(physicalMemoryArray)


#starts building necessary info
physicalMemory = [0 for x in range(64)]
numOfPids = 10
processArray = [0 for x in range(numOfPids)]
#print(processArray)
for i in range(numOfPids):
    value= random.randint(1,8)
    # vertical print of the processes print(value)
    processArray[i] = value
#print(processArray)

arrayBuilder(physicalMemory,processArray) 