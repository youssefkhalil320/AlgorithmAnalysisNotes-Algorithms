TA = [ 2.00, 2.10, 3.00, 3.20, 3.50, 5.00 ]
TD = [ 2.30, 3.40, 3.20, 4.30, 4.00, 5.20 ]
TAD = list(zip(TA, TD))
print(TAD)
def is_overlapping(x1,x2,y1,y2):
    return max(x1,y1) <= min(x2,y2)
overlaps = 1   
for r in range(len(TAD)):
    count =1
    for l in range(r+1,len(TAD)):
        if is_overlapping(TAD[r][0],TAD[r][1],TAD[l][0],TAD[l][1]) == True:
            count +=1
    overlaps = max(overlaps, count)   
print(overlaps)            

#Find the full article here https://takeuforward.org/data-structure/minimum-number-of-platforms-required-for-a-railway/