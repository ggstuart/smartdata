from pandas import DataFrame, Series
import requests
import StringIO
import csv
from datetime import datetime

class SmartspacesCSVAdapter():
    def __init__(self, base_url="smartspaces.dmu.ac.uk"):
        self.base_url = base_url
        
    def data_url(self, meter_id, period):
        url = "http://%s/meter_%i/%s/download" % (self.base_url, meter_id, period)
        return url
    
    def _response(self, meter_id, period):
        url = self.data_url(meter_id, period)
        return requests.get(url)
    
    def raw(self, meter_id, period):
        response = self._response(meter_id, period)
        return response.text
    
    def data(self, meter_id, period):
        raw = StringIO.StringIO(self.raw(meter_id, period))
        reader = csv.DictReader(raw)
        data, fmt = [], '%d-%m-%y %H:%M:%S'
        for row in reader:
            for key in row.keys():
                if key == 'date_time':
                    row[key] = datetime.strptime(row[key], fmt)
                else:
                    row[key] = float(row[key])
            data.append(row)
        return data

    def dataframe(self, meter_id, period):
        data = self.data(meter_id, period)
        df = DataFrame(data)
        df.set_index('date_time', inplace=True)
        return df
