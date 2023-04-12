
def main():

    file = "mbox-short.txt"
    print(file)
    handle = open(file)      #open file
    
    d = dict()      #create dictionary 
    l=[]           #create list
    
    for line in handle:        #each line in file 
        words = line.split()                #split by word
        if len(words) > 2 and words[0] == 'From':            #find lines that start with From
            h= words[5].split(':')                        #split time by :
            d[h[0]]= d.get(h[0], 0) +1                      #get time
        else: 
            continue
            
    for k,v in d.items():              #for k and v in dictionary  
        l.append((k,v))            #append the k and v in the dictionary into a list
    l.sort()                           #sort list        
    for k,v in l:                 #for k and v in list
        print(k,v)                    #print
        
if __name__ == '__main__':
        main()
