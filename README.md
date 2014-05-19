smartdata
=========

Simple library to access open data from http://smartspaces.dmu.ac.uk as a pandas dataframe

Example usage
---

    from smartdata import SmartspacesCSVAdapter
    adapter = SmartspacesCSVAdapter()
    queens_building_electricity_dataframe = adapter.dataframe(3, 'all')
    queens_building_electricity_dataframe.plot()

ipython notebook example
---
Also included is an example ipython notebook (Baseload calculations.ipynb) which uses the dat adapter. The notebook can be viewed directly [here](http://nbviewer.ipython.org/github/ggstuart/smartdata/blob/master/Baseload%20calculations.ipynb)
