from random import randint
from datetime import datetime, timedelta

from jchart import Chart
from jchart.config import Axes, DataSet, rgba



class BarChart(Chart):
    chart_type = 'bar'
    options = {'title': {
            'display': True,
            'text': 'Number of risk by Zone',
            'position': 'bottom',
            'fontStyle':'bold',
            'fontSize':20
        }, 
        'legend':{
        'display':True
        }

        }


    def get_labels(self, **kwargs):
        return ["BPCS Zone", "Plant Information Zone", "DMZ Zone", "SIS Zone"]

    def get_datasets(self, **kwargs):
        data = [30,20,10,40]
        colors = [
            "green",
             "blue",
            "orange",
             "brown"

        ]
        
       

        return [DataSet(label="Number of risk by zone",
                        data=data,
                        borderWidth=1,
                        backgroundColor=colors,
                        borderColor=colors,
                        )]


class PieChart(Chart):
    chart_type = 'pie'
    options = {'title': {
            'display': True,
            'text': 'Risk class matrix management chart',
            'position': 'bottom',
            'fontStyle':'bold',
            'fontSize':20
        },
        'legend':{
        'display':True
        }
    }
    def get_labels(self, **kwargs):
        return ["Class I", "Class II", "Class III","Class IV"]

    def get_datasets(self, **kwargs):
        data = [10, 20, 30,40]
        colors = [
            "green",
            "yellow",
            "orange",
            "red"
        ]
        return [DataSet(data=data,
                        label="Number of risk",
                        backgroundColor=colors,
                       )]


class LineChart(Chart):
    chart_type = 'line'
    options = {'scale': {
        'xAxes': [{'type':'time','distribution':'series','unit':'year'}]
    },
    'showLines':True,
    'tension':0,
    'legend':True,
    'title': {
            'display': True,
            'text': 'Hazard event by month',
            'position': 'bottom',
            'fontStyle':'bold',
            'fontSize':20
        },
    }

    def get_labels(self, **kwargs):
        return ["Jan -2017", "Feb -2017", "Mar -2017","Apr -2017","May-2017"]

    def get_datasets(self, **kwargs):
        data = [{'y': 45, 'x': '2017-01-31'}, {'y': 40, 'x': '2017-02-28'}, {'y': 50, 'x': '2017-03-31'}, 
         {'y': 30, 'x': '2017-04-30'}, {'y': 50, 'x': '2017-05-30'}, ]

       
        return [DataSet(data=data,
                        label="Number of hazard event",
                        borderColor = 'green',
                        fill = False,

                        
                       )]