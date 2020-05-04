#!/usr/bin/env python
# coding: utf-8

# In[2]:


def find_LCAs(parent):
    LCA = dict() # This is the nested dictionary
    def lca(u, v):    
        if u in list(LCA.keys()):
            if v in list(LCA[u].keys()):
                return
        for i in list(parent[u]):
            lca(i,v)
        ul = [u]
        def isu(u):
            for i in list(parent.keys()):
                if i in parent[u]:
                    ul.append(i)
        isu(u)
        for i in ul:
            isu(i)
        for i in ul:
            if u in LCA.keys():
                LCA[u].update({v : set(v)})
            else:    
                LCA[u] = ({v : set(v)})
                
        vl = [v]
        def isv(v):
            for i in list(parent.keys()):
                if i in parent[v]:
                    vl.append(i)
        isv(v)
        for i in vl:
            isv(i)
        for i in vl:
            if v in LCA.keys():
                LCA[v].update({u : set(u)})
            else:    
                LCA[v] = ({u : set(u)})

        cal = list((set(ul) & set(vl)))
        sl = []
        for i in cal:
            sl.extend(parent[i])

        fl = []
        for i in cal:
            if i not in sl:
                fl.append(i)
                
        if u in LCA.keys():
            LCA[u].update({v : set(fl)})
        else:    
            LCA[u] = ({v : set(fl)})
        if v in LCA.keys():
            LCA[v].update({u : set(fl)})
        else:    
            LCA[v] = ({u : set(fl)})
    # This calls the recursive "lca" function on all pairs of nodes to populate the "LCA" dictionary
    for u in parent:
        for v in parent:
            lca(u,v)
    return LCA


# In[ ]:




