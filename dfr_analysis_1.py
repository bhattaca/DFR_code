import pandas as pd
import numpy as np
import statistics
import scipy.stats as stats
from statsmodels.stats.api import DescrStatsW, CompareMeans
from queryrunner_client import Client
qr = Client(user_email='arindam@uber.com')  # Enter your uber email here

# data import
def data_pull(user_name, query):
    qr = Client(user_email = user_name)  #specify user email for accessing tables
    print ("INFO ", query)
    cursor1 = qr.execute('hive-secure', query, pii=True, timeout=30000)
    df = 0
    df = pd.DataFrame.from_dict(cursor1.fetchall())
    print('Shape of the pulled data:', df.shape)
    return df


sql = """
SELECT * FROM secure_cv.mcx_did_city_id_5_time_window_080208 where defect_name = 'infra_app_freeze_ui'
"""
raw_df = data_pull('arindam@uber.com', sql)