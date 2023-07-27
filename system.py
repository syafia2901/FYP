import numpy as np
import ray
ray.init()
import modin.pandas as pd
import os

def calculate(id):
    df_test=pd.read_csv("df_test.csv")
    df_test=pd.DataFrame(df_test)
    df_test.drop(columns=['Unnamed: 0'],axis=1)
    print(df_test.columns)

    matrix=df_test.pivot_table(index='customer_id', columns='product_id', values='review_score', fill_value=0)
    print(matrix)

    X=matrix.T.corr()
    X.head()

    from sklearn.decomposition import TruncatedSVD
    SVD = TruncatedSVD(n_components=10)
    decomposed_matrix = SVD.fit_transform(X)
    decomposed_matrix.shape
    correlation_matrix = np.corrcoef(decomposed_matrix)
    correlation_matrix.shape
    correlation_matrix

    n = id

    i=n
    customer_ID = list(X.index)
    customer_indx = customer_ID.index(i)
    customer_indx

    correlation_customer_ID = correlation_matrix[customer_indx]
    correlation_customer_ID.shape

    Recommend = list(X.index[correlation_customer_ID > 0.5])

    #remove the customer in list
    Recommend.remove(i) 

    #top 10 similar users to customer
    list2=Recommend[0:10]

    result = df_test[df_test['customer_id'].isin(list2)]
    #print('These are some item categories recommendations for you,\n', result['product_category_name_english'].sample(n=5))
    return  [category for index, category in result['product_category_name_english'].sample(n=5).items()]  


