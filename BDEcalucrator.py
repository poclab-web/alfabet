from alfabet import model
import os
import pandas as pd

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model.predict(['CC', 'NCCO'])

