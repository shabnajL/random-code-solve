### 595. Big Countries
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
        big_countries = world[ (world['area']>=3000000) | (world['population']>=25000000)]
        return big_countries[['name', 'population', 'area']]

### 1757. Recyclable and Low Fat Products
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    found = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return found[['product_id']]

###  183. Customers Who Never Order
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    a = customers['id']
    b = orders['customerId']
    #df = customers[a.isin(b)]
    df = customers[~a.isin(b)]
    df = df[['name']]
    df = df.rename(columns={'name': "Customers"})
    return df


###  
