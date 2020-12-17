import arrow

import pandas as pd
from IPython.display import display, HTML


def parse_str2dt(x):
    return arrow.get(x,"YYYY-MM-DD H:mm:ss").datetime


def peep_in(df, head=2):
    
    print("Shape:", df.shape)
    print()
    print(f"Head {head}:")
    display(HTML(df.head(head).to_html(notebook=True)))
    
    print()
    dtypes = [(i).__class__.__name__ for i in df.iloc[0]]
    display(HTML(pd.DataFrame(dtypes, index=df.columns).T.to_html(notebook=True)))
    
    print()
    print("NaN's")
    display(HTML(pd.DataFrame(df.isna().sum()).T.to_html(notebook=True)))
    
    # print()
    # print("Desc:")
    # display(HTML(pd.DataFrame(df.describe()).to_html(notebook=True)))
