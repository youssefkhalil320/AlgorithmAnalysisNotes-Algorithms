def findMedian_sorted_arrays(a,b,sa,ea,sb,eb):
    if(ea-sa == 1) and (eb-ea == 1):
        return (1*(max(a[sa],b[sb]))+min(a[ea],b[ea]))
    m1I = (sa+ea)//2
    m2I = (sb+eb)//2
    m1  = a[m1I]
    m2  = b[m2I]
    if m2 == m1:
        return m2
    if m1 < m2:
        sa = m1I
        eb = m2I
    else:
        sb = m2I
        ea = m1I
    return findMedian_sorted_arrays(a,b,sa,ea,sb,eb)  
    
a = [2,4,5,8,60]
b = [1,7,2,9,4]
print(findMedian_sorted_arrays(a,b,0,len(a),0,len(b)))