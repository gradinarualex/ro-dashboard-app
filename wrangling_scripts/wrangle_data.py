import pandas as pd
import numpy as np
import plotly.graph_objs as go


def cleandata(dataset, idvars=['Country Name', 'Series Name'], keepcolumns=['Country Name', 'Series Name', '2018 [YR2018]'], value_variables=['2018 [YR2018]']):
    """Clean world bank data for a visualizaiton dashboard

    Keeps data range of dates in keep_columns variable and data for the 5 countries analyzed
    Reorients the columns into a year, country and value
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file
        idvars (list of str): list of columns to keep as ID when melting the dataframe
        keepcolumns (list of str): list of columns to keep in (all others will be removed)
        value_variables (list of str): list of columns that represent values

    Returns:
        dfmelt (pandas.DataFrame): dataframe containing clean data

    """    
    df = pd.read_csv(dataset)

    # Keep only the columns of interest (years and country name)
    df = df[keepcolumns]
    
    # melt year columns  and convert year to int
    df_melt = df.melt(id_vars=idvars, value_vars = value_variables)
    df_melt.columns = ['country', 'measure', 'year', 'value']
    df_melt['year'] = df_melt['year'].str.split().apply(lambda x: int(x[0]))

    # output clean csv file
    return df_melt


def get_development_data(measures=None):
    """Get local world bank development data for a visualizaiton dashboard

    Args:
        measures (list of str): list of measures to get from dataset. if empty, returns all

    Returns:
        df (pandas.DataFrame): dataframe containing clean development data

    """  
    
    file_path = './data/development_data.csv'

    id_vars = ['Country Name', 'Series Name']

    keep_cols = ['Country Name', 'Series Name', '2009 [YR2009]', '2010 [YR2010]',\
                '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]',\
                '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]']

    year_cols = ['2009 [YR2009]', '2010 [YR2010]', '2011 [YR2011]', '2012 [YR2012]',\
                 '2013 [YR2013]', '2014 [YR2014]', '2015 [YR2015]', '2016 [YR2016]', \
                 '2017 [YR2017]', '2018 [YR2018]']

    df = cleandata(file_path, idvars=id_vars, keepcolumns=keep_cols, value_variables=year_cols)
    
    if measures == None:    
        return df
    else:
        return df[df['measure'].isin(measures)]
    

def get_education_data(measures=None):
    """Get local world bank education data for a visualizaiton dashboard

    Args:
        measures (list of str): list of measures to get from dataset. if empty, returns all

    Returns:
        df (pandas.DataFrame): dataframe containing clean education data

    """  
    
    dev_path = './data/education_data.csv'

    id_vars = ['Country Name', 'Series']

    keep_cols = ['Country Name', 'Series', '2009 [YR2009]', '2010 [YR2010]',\
                 '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]',\
                 '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]']

    year_cols = ['2009 [YR2009]', '2010 [YR2010]', '2011 [YR2011]', '2012 [YR2012]',\
                 '2013 [YR2013]', '2014 [YR2014]', '2015 [YR2015]', '2016 [YR2016]', \
                 '2017 [YR2017]', '2018 [YR2018]']

    df = cleandata(file_path, idvars=id_vars, keepcolumns=keep_cols, value_variables=year_cols)
    
    if measures == None:    
        return df
    else:
        return df[df['measure'].isin(measures)]
    
    
def get_sustainability_data(measures=None):
    """Get local world bank sustainability data for a visualizaiton dashboard

    Args:
        measures (list of str): list of measures to get from dataset. if empty, returns all

    Returns:
        df (pandas.DataFrame): dataframe containing clean sustainability data

    """  
    
    file_path = './data/sustainability_data.csv'

    id_vars = ['Country Name', 'Series Name']

    keep_cols = ['Country Name', 'Series Name', '2007 [YR2007]', '2008 [YR2008]',\
                 '2009 [YR2009]', '2010 [YR2010]', '2011 [YR2011]', '2012 [YR2012]',\
                 '2013 [YR2013]', '2014 [YR2014]', '2015 [YR2015]', '2016 [YR2016]']

    year_cols = ['2007 [YR2007]', '2008 [YR2008]', '2009 [YR2009]', '2010 [YR2010]',\
                 '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]', \
                 '2015 [YR2015]', '2016 [YR2016]']

    df = cleandata(file_path, idvars=id_vars, keepcolumns=keep_cols, value_variables=year_cols)
    
    if measures == None:    
        return df
    else:
        return df[df['measure'].isin(measures)]


def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    
    def get_color(country):
        if country == 'Romania':
            return '#1F77B4'
        elif country == 'France':
            return '#17BECF'
        else:
            return '#7F7F7F'
        
    def get_size(country):
        if country == 'France':
            return 30
        else:
            return 20
        
    def get_linewidth(country):
        if country in ['France', 'Romania']:
            return 4
        else:
            return 2

    
    # first chart plot
    # as a bar chart
    
    graph_one = []
    df = get_development_data(measures=['GDP per capita (current US$)'])
    df.drop(['measure'], axis=1, inplace=True)
    df = df[df['year'] == 2018]
    df.columns = ['country','year','gdp_per_capita_usd']
    
    graph_one.append(
        go.Bar(
            x = df['country'].tolist(),
            y = df['gdp_per_capita_usd'].tolist(),
            marker = dict(color = [
                '#7F7F7F',
                '#7F7F7F',
                '#7F7F7F',
                '#1F77B4',
                '#7F7F7F'
            ])
        )
    )

    layout_one = dict(title = 'GPD per capita (current USD) in 2018',
                      xaxis = dict(title = 'country',),
                      yaxis = dict(title = 'GDP per capita'),
                     )

    
    # second chart plot
    # as a line chart
    
    graph_two = []
    df = get_development_data(measures=['Consumer price index (2010 = 100)'])
    df.drop(['measure'], axis=1, inplace=True)
    df.columns = ['country','year','consumer_price_index']
    df['consumer_price_index'] = pd.to_numeric(df['consumer_price_index'])
    df.sort_values('year', ascending=False, inplace=True)
    countrylist = df['country'].unique().tolist()

    for country in countrylist:
        x_val = df[df['country'] == country]['year'].tolist()
        y_val = df[df['country'] == country]['consumer_price_index'].tolist()
        graph_two.append(
            go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines',
                name = country,
                line = dict(
                    color = get_color(country),
                    width = get_linewidth(country)
                )
            )
        )

    layout_two = dict(title = 'Consumer Price Index (2010=100)',
                      xaxis = dict(title = 'country'),
                      yaxis = dict(title = 'consumer price index')
                     )
    
    
    # third chart plot
    # as a bar chart
    
    graph_three = []
    df = get_development_data(measures=['Population growth (annual %)'])
    df.drop(['measure'], axis=1, inplace=True)
    df.columns = ['country','year','population_growth']
    df = df[df['year'] == 2018]
    df['population_growth'] = pd.to_numeric(df['population_growth'])

    graph_three.append(
        go.Bar(
            x = df['country'].tolist(),
            y = df['population_growth'].tolist(),
            marker = dict(color = [
                '#7F7F7F',
                '#7F7F7F',
                '#7F7F7F',
                '#D62728',
                '#7F7F7F'
            ])
        )
    )

    layout_three = dict(title = 'Population Growth (annual %) in 2018',
                      xaxis = dict(title = 'year',),
                      yaxis = dict(title = 'population growth'),
                     )
    
    
    # fourth chart plot
    # as a line chart
    
    graph_four = []
    df = get_development_data(measures=['Fertility rate, total (births per woman)'])
    df.drop(['measure'], axis=1, inplace=True)
    df.columns = ['country','year','fertility_rate']
    df['fertility_rate'] = pd.to_numeric(df['fertility_rate'])
    df.sort_values('year', ascending=False, inplace=True)
    
    for country in countrylist:
        x_val = df[df['country'] == country]['year'].tolist()
        y_val = df[df['country'] == country]['fertility_rate'].tolist()
        graph_four.append(
            go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines',
                name = country,
                line = dict(
                    color = get_color(country),
                    width = get_linewidth(country)
                )
            )
        )

    layout_four = dict(title = 'Fertility rate in Romania (births per woman)',
                      xaxis = dict(title = 'year'),
                      yaxis = dict(title = 'births per woman')
                     )
    
    
    # fifth chart plot
    # as a line chart
    
    graph_five = []
    df = get_sustainability_data(measures=['CO2 emissions (metric tons per capita)'])
    df.drop(['measure'], axis=1, inplace=True)
    df.columns = ['country','year','co2_emissions']
    df['co2_emissions'] = pd.to_numeric(df['co2_emissions'])
    df.sort_values('year', ascending=False, inplace=True)

    for country in countrylist:
        x_val = df[df['country'] == country]['year'].tolist()
        y_val = df[df['country'] == country]['co2_emissions'].tolist()
        graph_five.append(
            go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines',
                name = country,
                line = dict(
                    color = get_color(country),
                    width = get_linewidth(country)
                )
            )
        )

    layout_five = dict(title = 'CO2 emissions (metric tons per capita)',
                      xaxis = dict(title = 'year'),
                      yaxis = dict(title = 'metric tons per capita')
                     )
    
    
    # sixth chart plot
    # as a scatter plot
    
    graph_six = []
    df = get_sustainability_data(measures=['Renewable electricity output (GWh)',\
                                           'Renewable electricity share of total electricity output (%)'])
    measures_list = df['measure'].unique().tolist()
    df['value'] = pd.to_numeric(df['value'])
    df = df[df['year'] == 2015]

    for country in countrylist:
        country_df = df[df['country'] == country]
        x_val = country_df[country_df['measure'] == measures_list[0]]['value'].tolist()
        y_val = country_df[country_df['measure'] == measures_list[1]]['value'].tolist()
        
        graph_six.append(
            go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'markers',
                text = [country],
                name = country,
                textposition = 'top left',
                marker = dict(
                    color = get_color(country),
                    size = get_size(country)
                )
            )
        )

    layout_six = dict(title = 'Renewable Electricity Output vs Share of Total Output',
                      xaxis = dict(title = 'renewable electricity output (Gwh)'),
                      yaxis = dict(title = 'renewable share of total output (%)')
                     )
    
    
    # seventh chart plot
    # as a bar chart
    
    graph_seven = []
    df = get_development_data(measures=['Urban population (% of total population)'])
    df.drop(['measure'], axis=1, inplace=True)
    df = df[df['year'] == 2018]
    df = df[df['country'] == 'Romania']
    df.columns = ['country','year','urban_population_prc']
    
    graph_seven.append(
        go.Bar(
            x = df['country'].tolist(),
            y = df['urban_population_prc'].tolist()
        )
    )

    layout_seven = dict(title = 'Urban Population (%) in 2018',
                        xaxis = dict(title = 'year',),
                        yaxis = dict(title = 'urban population percentage')
                       )
    
    
    # eight chart plot
    # as a line chart
    
    graph_eight = []
    df = get_development_data(measures=['Individuals using the Internet (% of population)'])
    df.drop(['measure'], axis=1, inplace=True)
    df.columns = ['country','year','internet_usage']
    df['internet_usage'] = pd.to_numeric(df['internet_usage'])
    df.sort_values('year', ascending=False, inplace=True)

    for country in countrylist:
        x_val = df[df['country'] == country]['year'].tolist()
        y_val = df[df['country'] == country]['internet_usage'].tolist()
        graph_eight.append(
            go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines',
                name = country,
                line = dict(
                    color = get_color(country),
                    width = get_linewidth(country)
                )
            )
        )

    layout_eight = dict(title = 'Population using the internet (%)',
                      xaxis = dict(title = 'year'),
                      yaxis = dict(title = '% of population using the internet')
                     )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))
    figures.append(dict(data=graph_six, layout=layout_six))
    figures.append(dict(data=graph_seven, layout=layout_seven))
    figures.append(dict(data=graph_eight, layout=layout_eight))
    
    return figures