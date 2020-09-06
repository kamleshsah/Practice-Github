#!/usr/bin/env python
# coding: utf-8

# In[7]:


# def ok(a,b,x,y,n):
#     diff = a - x
#     if n>=diff:
#         n = n - diff
#     else:
#         a=a-n
#         return a*b
#     a=x
#     if n<=0:
#         return a*b
#     diff1=b-y
#     if n>=diff1:
#         b=y
#         return a*b
#     else:
#         b=b-n
#     return a*b
    
    

# n=int(input())
# for i in range(n):
#     a,b,x,y,n=map(int,input().split())
#     ans=min(ok(a,b,x,y,n),ok(b,a,y,x,n))
#     print(ans)


# In[57]:
 
    
# New Question 

def ok(n,x,y):
    if n==2:
        return [x,y]
    b=[1000000000 for x in range(n)]
    for i in range(n-1):
        arr=[-1 for p in range(n)]
        for j in range(i+1,n):
            arr[i]=x
            diff=y-x
            dis=j-i
            
            if diff%dis==0:
                arr[j]=y
                diff=diff//dis
                for k in range(i-1,-1,-1):
                    arr[k]=arr[k+1]-diff
                for k in range(i+1,n):
                    arr[k]=arr[k-1]+diff
            
                if arr[0]>0 and arr[-1]<b[-1]:
                    b=arr
    return b
        
n=int(input())
for i in range(n):
    n,x,y=map(int,input().split())
    ans=ok(n,x,y)
    for i in ans:
        print(i,end=' ')


# In[ ]:





# In[ ]:




