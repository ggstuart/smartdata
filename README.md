smartdata
=========

Simple library to access open data from http://smartspaces.dmu.ac.uk as a pandas dataframe

Example usage
---

    from smartdata import SmartspacesCSVAdapter
    adapter = SmartspacesCSVAdapter()
    queens_building_electricity_dataframe = adapter.dataframe(3, 'all')
    queens_building_electricity_dataframe.plot()
