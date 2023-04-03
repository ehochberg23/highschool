
def main():

    file = "mbox-short.txt"
    print(file)
    handle = open(file)
    
    d = dict()
    l=[]
    
    for line in handle: 
        words = line.split()
        if len(words) > 2 and words[0] == 'From':
            h= words[5].split(':')
            d[h[0]]= d.get(h[0], 0) +1
        else: 
            continue
            
    for k,v in d.items():
        l.append((k,v))
    l.sort()
    for k,v in l:
        print(k,v)
        
if __name__ == '__main__':
        main()
