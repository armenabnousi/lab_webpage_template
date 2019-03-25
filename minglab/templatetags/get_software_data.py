from django import template
import pandas as pd

register = template.Library()

@register.simple_tag(name="softwares")
def get_software_names():
	filename = "minglab/data/software.txt"
	data = pd.read_csv(filename, sep = "\t")
	softwares = list(data['software_name'])
	#softwares = {'a': 'check'}
	#print(softwares)
	return softwares

#register.tag("softwares", get_software_names)