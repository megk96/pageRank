# Project Title

Implementation of HITS Algorithm

## Getting Started

The implementation utlizes Python. Ensure you have python installed on your system. Several libraries have been used like numpy, scipy, networkx, and matplotlab. 

### Prerequisites and Installation

python

```
https://www.python.org/downloads/

Select the right package
```

numpy

```
sudo apt-get install python-numpy
```
scipy

```
sudo apt-get install python-scipy
```
matplotlab

```
sudo apt-get install python-matplotlib
```
networkx

```
pip install networkx
```


## Running the tests
...
python hits.py
...
Runs the HITS Algorithm and plots the hubs and authorities for the wiki election votes from page to page. Returns top 20 most reliable 'experts' i.e 'voters'.(hubs) And top 20 most reliable pages. (authorities)


...
python time.py
...
Runs the HITS Algorithm and plots the hubs and authorities with enhancement by considering the age of the vote for the wiki election votes from page to page. Returns top 20 most reliable 'experts' i.e 'voters'.(hubs) And top 20 most reliable pages. (authorities)

### Break down into end to end tests

The two codes are run simultaneously and the graphs are compared.

```
The hubs aren't varied because experts remain experts, but relevant documents are altered with respect to time. 
```

## Built With

* [Python](https://www.python.org/downloads/) - The Language Used

## Contributing

Meghana Kumar 2014B5A70932H
Kshitij Grovor 2015A7PS0070H
Bhavathi Reddy 2015A7PS0020H




## Acknowledgments

http://www.naturalspublishing.com/files/published/18b08bx6bs19wc.pdf

