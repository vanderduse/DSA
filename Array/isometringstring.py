s=sorted('egg')
t=sorted('add')

from numpy import unique
# sn=set(s)
# tn=set(t)
# for i in range ip(s,t)
# print(char)
# print (sn)
# print(tn)

# if len(sn)==len(tn):
#     print("true")
# else:
#     print ("false")

        
# Define lambda functions for mapping characters
map_st = lambda s, t: dict(zip(s, t))
map_ts = lambda s, t: dict(zip(t, s))
        
        # Create mappings
mapping_st = (map_st(s, t))
mapping_ts = (map_ts(s, t))
if len(mapping_ts)!=len(mapping_st):
    print("fasle")

print (mapping_st,mapping_ts)