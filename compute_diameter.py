#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


def compute_diameter(tree): 
    '''
    This function computes a diameter path (i.e. a longest path between any two nodes) of a tree and its length
    :param tree: the tree
    :return: a list d_path containing the diameter path and a floating point number d_length storing the diameter length
    '''
    d_path = []
    d_length = 0
    import treeswift as ts
    ml = []
    md = {}
    ct = 0
    for node in tree.traverse_postorder():
        w1 = list([j.get_edge_length() for j in node.traverse_ancestors()])
        w2 = list([j.label for j in node.traverse_ancestors()])
        md[ct] = {w2[i]: w1[i] for i in range(len(w1))}  
        ct += 1
    
    mo = 0
    for i in range(0,len(md.keys())):
        dd = {}
        dd = {**md[0], **md[i]}
        dl = list(dd.values())
        dl.remove(None)
        if sum(dl) > mo:
            mo = sum(dl)
            be = i
    mu = 0
    fl = []
    for i in range(0,len(md.keys())):
        dd = {}
        sl = list(md[be].keys())
        ssl = list(md[i].keys())
        ssl.reverse()
        sl.extend(ssl)
        dd = {**md[be], **md[i]}
        dl = list(dd.values())
        dl.remove(None)
        if sum(dl) > mu:
            mu = sum(dl)
            fl = sl
    ffl = []
    for i in fl:
        if i not in ffl:
            ffl.append(i)
    d_length = mu
    d_path = ffl

    return d_path,d_length


# In[ ]:




