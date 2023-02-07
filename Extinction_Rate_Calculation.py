""" Author: Shayan Firouzian
file is also located at Google Colabratoary Notebook by this address:
    https://colab.research.google.com/drive/1sRhGNpAaxcm9VMqM-Dzh_PZRlAQFgB-L?usp=sharing
"""

# 'n' is the number of all Species of a specific Family of Organisms
# 't' is the average time in which any of that Family's species exist before going Extinct
def extinction_rate(t,n):
    # it calculates the 'Extinction Rate' for a Family of Organisms
    unit=' per million species-years'
    if type(n)==int:
        if t>0:
            r=((10**6)/(t*n))
            r=str(r)+unit
    else:
        if t<=0:
            r='Existing time interval for species (t) can not be negative or zero'
        elif type(n)!=int:
            r='Number of Species in a Family (n) must be integer'
        else:
            r='''
            Existing time interval for species (t) can not be negative or zero
            &
            Number of Species in a Family (n) must be integer
            '''
    return r
# Note that 'Specie' and 'Family' are pre-defined terms in biological taxonomy
