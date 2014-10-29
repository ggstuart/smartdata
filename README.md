smartdata
=========

Simple library to access open data from http://smartspaces.dmu.ac.uk as a pandas dataframe

Example usage
---

    from smartdata import SmartspacesCSVAdapter
    adapter = SmartspacesCSVAdapter()
    queens_building_electricity_dataframe = adapter.dataframe(3, 'all')
    queens_building_electricity_dataframe.plot()

Real world example
---
See [the baseload repository](https://github.com/ggstuart/baseload) for an example of usage of the data adapter.

Ipython notebook example
---
Also included is an older version of the baseload calculations as an ipython notebook (Baseload calculations.ipynb) which also uses the data adapter. The notebook can be viewed directly [here](http://nbviewer.ipython.org/github/ggstuart/smartdata/blob/master/Baseload%20calculations.ipynb)

