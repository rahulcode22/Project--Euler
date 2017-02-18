import sys
def fermat(n):
    if n==2:
        return True
    if not n and 1:
        return False
    return pow(2,n-1,n)==1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lis=[]
    for i in range(2,n+1):
        if fermat(i):
            if n%i==0:
                lis.append(i)
    print(max(lis))
    
    
    #My cpp Solution to PE-3 problem
    #include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
int main(){
    int t;
    cin>>t;
    unsigned long long n,max,count,fac;
    bool x;
    while(t--){
        max=1;
        cin>>n;
        x=0;
    while (n%2 == 0)
            {
                n=n/2;
                x=1;
            }
        if(x) max=2;
        
    for (fac = 3; fac<= sqrt(n)+2; fac = fac+2)
    {
                x=0;
                while (n%fac == 0)
                {
                    x=1;
                    n=n/fac;
                    
                }
                if(x) if(fac>max) max=fac;  
   }
   if (n > 2){
                if(n>max) max=n;
            } 
                
     cout<<max<<endl;       
    }
    return 0;
}
