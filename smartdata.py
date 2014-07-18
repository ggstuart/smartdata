import logging
import os.path
import shutil
import csv
from datetime import datetime
from pandas import DataFrame, Series
import requests

log = logging.getLogger('smartdata')

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

class SmartspacesCSVAdapter():
    def __init__(self, base_url="smartspaces.dmu.ac.uk", tmp_folder='.data_cache'):
        self.base_url = base_url
        self.tmp_folder = tmp_folder
        if not os.path.exists(self.tmp_folder):
            os.makedirs(self.tmp_folder)
        
    def data_url(self, meter_id, period):
        url = "http://%s/meter_%i/%s/download" % (self.base_url, meter_id, period)
        return url
    
    def _response(self, meter_id, period):
        url = self.data_url(meter_id, period)
        log.info("Downloading from %s..." % url)
        result = requests.get(url)
        log.info("Download complete...")
        return result
    
    def raw(self, meter_id, period):
        response = self._response(meter_id, period)
        return response.text
    
    def data(self, meter_id, period):
        raw = StringIO(self.raw(meter_id, period))
        log.info("Processing...")
        reader = csv.DictReader(raw)
        data, fmt = [], '%d-%m-%y %H:%M:%S'
        for row in reader:
            for key in row.keys():
                if key == 'date_time':
                    row[key] = datetime.strptime(row[key], fmt)#.isoformat()
                else:
                    row[key] = float(row[key])
            data.append(row)
        raw.close()
        log.info("done")
        return data

    def dataframe(self, meter_id, period, force=False):
        tmp_file = os.path.join(self.tmp_folder, "meter_%02i_%s.csv" % (meter_id, period))
        if force or not os.path.exists(tmp_file):
            data = self.data(meter_id, period)
            log.debug("saving to cache...")
            with open(tmp_file, 'w', newline="") as f:
                writer = csv.DictWriter(f, data[0].keys())
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
        else:
            log.info("loading from cache (%s)..." % tmp_file)
            with open(tmp_file, 'r') as f:
                reader = csv.DictReader(f)
                data = []
                for row in reader:
                    row['date_time'] = datetime.strptime(row['date_time'], '%Y-%m-%d %H:%M:%S')
                    row['consumption (kWh)'] = float(row['consumption (kWh)'])
                    data.append(row)
        df = DataFrame(data)
        df.set_index('date_time', inplace=True)
        return df
