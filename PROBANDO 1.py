#%%
a = "hola"
print(a)

#%%
import pandas as pd

pd.DataFrame([2,3,4,2,3,4], [4,5,6,3,2,5])


#%%
import rpy2.rinterface
%load_ext rpy2.ipython


#%%
%R a <- c(3,2,1,2,3,4)

#%%
%R b <- c(5,3,4,6,2,3)

#%%
%R plot(a,b)


#%%
%R print(summary(lm(a~b)))

#%%
%R unclass(lm(a~b))

#%%
%R print(list(lm(a~b)))