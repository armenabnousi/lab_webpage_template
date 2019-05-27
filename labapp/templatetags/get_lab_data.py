from django import template
import pandas as pd

register = template.Library()

@register.simple_tag(name="labdata")
def get_lab_data():
	filename = "labapp/data/labdata.txt"
	data = pd.read_csv(filename, sep = "\t", header = None)
	labdata = {}
	for row in range(data.shape[0]):
		k, v = data.iloc[row, 0], data.iloc[row, 1]
		labdata[k] = v
	return labdata

#print(get_lab_data())
