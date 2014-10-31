import logging
from smartdata import SmartspacesCSVAdapter, SmartspacesJSONAdapter

#log = logging.getLogger('test')
logging.basicConfig(level=logging.INFO)

csv = SmartspacesCSVAdapter()
json = SmartspacesJSONAdapter()

for org in json.organisations():
    for b in json.buildings(org):
        print "%s: %s" % (org['name'], b['name'])
        for m in json.meters(b):
            print "\t%s (%s)" % (m['commodity'], m['name'])
            data = csv.dataframe(m['id'], 'all')

