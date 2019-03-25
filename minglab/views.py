from django.shortcuts import render
import pandas as pd
# Create your views here.
datadir = "minglab/data/"


def home(request):
	profile_paragraphs = [list(dict(x).values())[0] for x in dict(pd.read_csv(datadir + "profile_paragraphs.txt", sep = "\n", header = None).T).values()]
	return(render(request, 'minglab/home.html', {'profile_paragraphs' : profile_paragraphs}))

def software(request):
	software = pd.read_csv(datadir + "software.txt", sep = "\t")
	software = software.fillna("$$$")
	software = [dict(x) for x in dict(software.T).values()]	
	print(software)
	return(render(request, 'minglab/software.html', {'software_info' : software}))

def people(request):
	people = pd.read_csv(datadir + "people.txt", sep = "\t")
	people = people.fillna("$$$")
	people = [dict(x) for x in dict(people.T).values()]	
	return(render(request, 'minglab/people.html', {'people' : people}))

def publications(request):
	papers = pd.read_csv(datadir + "papers.txt", sep = "\t", encoding="ISO-8859-1")
	papers = papers.fillna("$$$")
	papers = [dict(x) for x in dict(papers.T).values()]	
	return(render(request, 'minglab/publications.html', {'papers' : papers}))

def research(request):
	research_paragraphs = [list(dict(x).values())[0] for x in dict(pd.read_csv(datadir + "research_paragraphs.txt", sep = "\n", header = None).T).values()]
	return(render(request, 'minglab/research.html', {'research_paragraphs' : research_paragraphs}))

def contact(request):
	return(render(request, 'minglab/contact.html'))
