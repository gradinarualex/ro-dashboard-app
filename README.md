# **Romania in Numbers: Dashboard**

--- 

#### A selected list of facts about my home country displayed on a web dashboard using data from the World Data Bank.  
#### This simple dashboard uses 8 descriptive plots that give you a general idea of how Romania is doing economically, socially and from a sustainability standpoint.

**Link to Dashboard: https://ro-dashboard-app.herokuapp.com/**

## **Technologies Used:**
--- 
* Front-end: `HTML`, `CSS` and `Bootstrap`
* Back-end: `python`, `flask`
* Data procesing & Visualization: `pandas`, `plotly`
* Hosting: `heroku`


## **Methodology**
--- 
#### **Country Selection:**

The list of 5 countries was selected in order to keep the graphs readable.

Selection Criteria:
 1. All countries are part of the EU
 2. Have at least 3 similar countries to Romania to compare
 3. Provide a benchmark using the biggest country in the EU
 
Similar Country Selection Criteria:  
The 3 similar countries similar to Romania were selected based on the shortest Euclidean distance between Romania and all other using 3 size dimensions:
* country total area
* population size
* % of urban population  

The closest three countries resulting are:
* Slovak Republic
* Poland
* Austria  

The biggest country was selected as the country with the highest sum of normalized values of the three features mentioned previously:
* France

#### **Measures Selection:**

The measures were selected from the [World Data Bank](https://data.worldbank.org/) based on:
1. latest data availability for all countries (how actual is the data?)
2. ease of interpretation (how easy is it to understand?)
3. relevance (how important is this?)


--- 

Thanks for taking an interest! If you find anything in this that could be improved, I'd love some feedback at gradinaru.alex@gmail.com.