import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

print loansData['Interest.Rate'][0:5] 
print loansData['Loan.Length'][0:5]
print loansData['FICO.Range'][0:5]
#print type(loansData['FICO.Range'][0:5])

#x = loansData['Interest.Rate'][0:5].values[1]


#x = x.rstrip('%') # Removes the % from the end
#print "no %"
#print x 


###x = float(x) # Convert x to a number
###print "float change"
###print x 
###print type(x)

#x = x / 100 # because this is a percentage
#print "percentage transfer"
#print x 

#x = round(x, 4) # We don't need that much precision, round to 4 digits
#print "round x"
#print x

#print
#print 

# Now we know what we have to do. Combine the above into a single lambda function
y = lambda x: round(float(x.rstrip('%')) / 100, 4)

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
#print type(cleanInterestRate)
cleanLoanLength = loansData['Loan.Length'].map(lambda x: x.strip('months'))

#print cleanInterestRate[0:5]
#print cleanLoanLength[0:5]
#Now this is the final piece to cleaning both Interest.Rate and Loan.Length
loansData['Loan.Length'] = cleanLoanLength
loansData['Interest.Rate'] = cleanInterestRate



cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
#print cleanFICORange[0:5]
#print cleanFICORange[0:5].values[0]
#print type(cleanFICORange[0:5].values[0])
#print cleanFICORange[0:5].values[0][0]
#print type(cleanFICORange[0:5].values[0][0])

#Using List Comprehensions, Convert all the string to integers
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
#print cleanFICORange[0:5]
#print cleanFICORange[0:5].values[0]
#print type(cleanFICORange[0:5].values[0][0])
# We have successfully converted the strings inside the list to integers

#Now we can replace the column in our data frame with the cleaned data
loansData['FICO.Score'] = cleanFICORange

print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Score'][0:5]

#print type(loansData['FICO.Score'][0:5].values[0][0])


#Plot a histogram of FICO scores.
plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()

#Create a scatterplot matrix.
a=pd.scatter_matrix(loansData, alpha=0.05, figure=(10,10))
plt.show()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()













