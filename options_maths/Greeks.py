# imports
from math import *
from scipy.stats import norm
    
# constants
#spotPrice = 32519.75
#strikePrice = 33000
#RiskFreeRate = 0.1
#volatility = 0.2596
#DividendYield = 0
#ExpiryTime = (14/365)
#target = 530


def D1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return (log(spotPrice/strikePrice) + ((RiskFreeRate-DividendYield+(0.5*(volatility**2)))*ExpiryTime))/(volatility*ExpiryTime**0.5) 

def D2(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return (D1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)- volatility*ExpiryTime**0.5)
    
def ND1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return norm.cdf(D1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))
  
def ND2(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return norm.cdf(D2(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))
    
def n_d1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return (1/(2*pi)**0.5*(exp(-(D1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)**2)/2)))

def callValue(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return exp(-DividendYield*ExpiryTime)*(spotPrice*ND1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))-(strikePrice*exp(-RiskFreeRate*ExpiryTime)*ND2(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

print("Call",callValue(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def putValue(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return exp(-RiskFreeRate*ExpiryTime)*strikePrice*norm.cdf(-D2(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))-exp(-DividendYield*ExpiryTime)*spotPrice*norm.cdf(-D1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

print("put",putValue(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def callDelta(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return (ND1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)*exp(-DividendYield*ExpiryTime))*100

print("callDelta",callDelta(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def putDelta(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return ((ND1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)-1)*exp(-DividendYield*ExpiryTime))*100

print("putDelta",putDelta(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def callGamma(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return ((n_d1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)*exp(-DividendYield*ExpiryTime))/(spotPrice*volatility*(ExpiryTime**0.5)))*100

print("Gamma",callGamma(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def putGamma(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return callGamma(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)
    

def callVega(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return (spotPrice*(ExpiryTime**0.5)*n_d1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)*exp(-DividendYield*ExpiryTime))

print("vega",callVega(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def putVega(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return callVega(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)
    
    
def callTheta(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return ((-1)*(spotPrice*n_d1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)*volatility*exp(-DividendYield*ExpiryTime))/(2*(ExpiryTime**0.5))+(DividendYield*spotPrice*ND1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)*exp(-DividendYield*ExpiryTime))-(RiskFreeRate*strikePrice*exp(-RiskFreeRate*ExpiryTime)*ND2(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)))*(100/365)

print("callTheta",callTheta(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def putTheta(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return ((-1)*(spotPrice*n_d1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)*volatility*exp(-DividendYield*ExpiryTime))/(2*(ExpiryTime**0.5))-(DividendYield*spotPrice*strikePrice*norm.cdf(-D1(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))*exp(-DividendYield*ExpiryTime))+(RiskFreeRate*strikePrice*exp(-RiskFreeRate*ExpiryTime)*norm.cdf(-D2(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))))*(100/365)
    
print("putTheta",putTheta(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def callRho(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return 0.01*strikePrice*ExpiryTime*exp(-RiskFreeRate*ExpiryTime)*ND2(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime)
    
print("callRHO",callRho(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def putRHO(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime):
    return -0.01*strikePrice*ExpiryTime*exp(-RiskFreeRate*ExpiryTime)*(1-ND2(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

print("putRHO",putRHO(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime))

def ICV(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime,target):
    high=5
    low = 0
    while((high-low)>0.0001):
        if callValue(spotPrice,strikePrice,RiskFreeRate,DividendYield,(high+low)/2,ExpiryTime)>target:
            high = (high+low)/2
        else:
            low = (high+low)/2
    return ((high+low)/2)*100
 
#print(ICV(spotPrice,strikePrice,RiskFreeRate,DividendYield,volatility,ExpiryTime,target))

