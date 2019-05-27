from django import template
import pandas as pd

register = template.Library()

@register.simple_tag(name="softwares")
def get_software_names():
	filename = "labapp/data/software.txt"
	data = pd.read_csv(filename, sep = "\t")
	softwares = list(data['software_name'])
	return softwares

