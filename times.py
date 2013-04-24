times
====
%times
def f1(b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s):
    a = matrix(4,4)
    a[0,0] = b
    a[0,1] = c
    a[0,2] = d
    a[0,3] = e
    a[1,0] = f
    a[1,1] = h
    a[1,2] = i
    a[1,3] = j
    a[2,0] = k
    a[2,1] = l
    a[2,2] = m
    a[2,3] = n
    a[3,0] = o
    a[3,1] = p
    a[3,2] = q
    a[3,3] = s
 
def f2(b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1,s1):
    aa = matrix(4,4)
    aa[0,0] = b1
    aa[0,1] = c1
    aa[0,2] = d1
    aa[0,3] = e1
    aa[1,0] = f1
    aa[1,1] = h1
    aa[1,2] = i1
    aa[1,3] = j1
    aa[2,0] = k1
    aa[2,1] = l1
    aa[2,2] = m1
    aa[2,3] = n1
    aa[3,0] = o1
    aa[3,1] = p1
    aa[3,2] = q1
    aa[3,3] = s1
  
 a*aa


%time
%cython
def f1(b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s):
    a = matrix(4,4)
    a[0,0] = b
    a[0,1] = c
    a[0,2] = d
    a[0,3] = e
    a[1,0] = f
    a[1,1] = h
    a[1,2] = i
    a[1,3] = j
    a[2,0] = k
    a[2,1] = l
    a[2,2] = m
    a[2,3] = n
    a[3,0] = o
    a[3,1] = p
    a[3,2] = q
    a[3,3] = s
 
def f2(b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1,o1,p1,q1,s1):
    aa = matrix(4,4)
    aa[0,0] = b1
    aa[0,1] = c1
    aa[0,2] = d1
    aa[0,3] = e1
    aa[1,0] = f1
    aa[1,1] = h1
    aa[1,2] = i1
    aa[1,3] = j1
    aa[2,0] = k1
    aa[2,1] = l1
    aa[2,2] = m1
    aa[2,3] = n1
    aa[3,0] = o1
    aa[3,1] = p1
    aa[3,2] = q1
    aa[3,3] = s1
  
 a*aa
