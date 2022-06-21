import pandas as pd
links = pd.read_csv('links.csv')
t_link = []
for i in range(links):
    t_link.append(i)
    print(list(t_link))