#################################################################################################
###                         Merge  Covid19, Age, SES, T2DM, and AP data                       ###
#############            for dates January 22, 2020   to   July 8, 2020            ##############
#################################################################################################


####    Download Raw Covid19 cases and deaths data from Github repository    ####

import pandas as pd
import io
import requests

# combined cases and deaths, long-format, not used
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
string_url_content = requests.get(url).content
my_dataframe = pd.read_csv(io.StringIO(string_url_content.decode('utf-8')))
print(my_dataframe.describe())

# deaths, wide-format 
covid_deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
covid_deaths_string_url_content = requests.get(covid_deaths_url).content
covid_deaths_df = pd.read_csv(io.StringIO(covid_deaths_string_url_content.decode('utf-8')))
print(covid_deaths_df.describe())

# cases, wide-format
covid_cases_urlfile = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
covid_cases_string_url_content = requests.get(covid_cases_urlfile).content
covid_cases_df = pd.read_csv(io.StringIO(covid_cases_string_url_content.decode('utf-8')))
print(covid_cases_df.describe())


#################################################################################################
###                         Change cumulative Covid19 to daily counts                        ###
#################################################################################################

covid_cases_df["7/24/20"] = covid_cases_df["7/24/20"] - covid_cases_df["7/23/20"]
covid_cases_df["7/23/20"] = covid_cases_df["7/23/20"] - covid_cases_df["7/22/20"]
covid_cases_df["7/22/20"] = covid_cases_df["7/22/20"] - covid_cases_df["7/21/20"]
covid_cases_df["7/21/20"] = covid_cases_df["7/21/20"] - covid_cases_df["7/20/20"]
covid_cases_df["7/20/20"] = covid_cases_df["7/20/20"] - covid_cases_df["7/19/20"]
covid_cases_df["7/19/20"] = covid_cases_df["7/19/20"] - covid_cases_df["7/18/20"]
covid_cases_df["7/18/20"] = covid_cases_df["7/18/20"] - covid_cases_df["7/17/20"]
covid_cases_df["7/17/20"] = covid_cases_df["7/17/20"] - covid_cases_df["7/16/20"]
covid_cases_df["7/16/20"] = covid_cases_df["7/16/20"] - covid_cases_df["7/15/20"]
covid_cases_df["7/15/20"] = covid_cases_df["7/15/20"] - covid_cases_df["7/14/20"]
covid_cases_df["7/14/20"] = covid_cases_df["7/14/20"] - covid_cases_df["7/13/20"]
covid_cases_df["7/13/20"] = covid_cases_df["7/13/20"] - covid_cases_df["7/12/20"]
covid_cases_df["7/12/20"] = covid_cases_df["7/12/20"] - covid_cases_df["7/11/20"]
covid_cases_df["7/11/20"] = covid_cases_df["7/11/20"] - covid_cases_df["7/10/20"]
covid_cases_df["7/10/20"] = covid_cases_df["7/10/20"] - covid_cases_df["7/9/20"]
covid_cases_df["7/9/20"] = covid_cases_df["7/9/20"] - covid_cases_df["7/9/20"]
covid_cases_df["7/8/20"] = covid_cases_df["7/8/20"] - covid_cases_df["7/7/20"]
covid_cases_df["7/7/20"] = covid_cases_df["7/7/20"] - covid_cases_df["7/6/20"]
covid_cases_df["7/6/20"] = covid_cases_df["7/6/20"] - covid_cases_df["7/5/20"]
covid_cases_df["7/5/20"] = covid_cases_df["7/5/20"] - covid_cases_df["7/4/20"]
covid_cases_df["7/4/20"] = covid_cases_df["7/4/20"] - covid_cases_df["7/3/20"]
covid_cases_df["7/3/20"] = covid_cases_df["7/3/20"] - covid_cases_df["7/2/20"]
covid_cases_df["7/2/20"] = covid_cases_df["7/2/20"] - covid_cases_df["7/1/20"]
covid_cases_df["7/1/20"] = covid_cases_df["7/1/20"] - covid_cases_df["6/30/20"]
covid_cases_df["6/30/20"] = covid_cases_df["6/30/20"] - covid_cases_df["6/29/20"]
covid_cases_df["6/29/20"] = covid_cases_df["6/29/20"] - covid_cases_df["6/28/20"]
covid_cases_df["6/28/20"] = covid_cases_df["6/28/20"] - covid_cases_df["6/27/20"]
covid_cases_df["6/27/20"] = covid_cases_df["6/27/20"] - covid_cases_df["6/26/20"]
covid_cases_df["6/26/20"] = covid_cases_df["6/26/20"] - covid_cases_df["6/25/20"]
covid_cases_df["6/25/20"] = covid_cases_df["6/25/20"] - covid_cases_df["6/24/20"]
covid_cases_df["6/24/20"] = covid_cases_df["6/24/20"] - covid_cases_df["6/23/20"]
covid_cases_df["6/23/20"] = covid_cases_df["6/23/20"] - covid_cases_df["6/22/20"]
covid_cases_df["6/22/20"] = covid_cases_df["6/22/20"] - covid_cases_df["6/21/20"]
covid_cases_df["6/21/20"] = covid_cases_df["6/21/20"] - covid_cases_df["6/20/20"]
covid_cases_df["6/20/20"] = covid_cases_df["6/20/20"] - covid_cases_df["6/19/20"]
covid_cases_df["6/19/20"] = covid_cases_df["6/19/20"] - covid_cases_df["6/18/20"]
covid_cases_df["6/18/20"] = covid_cases_df["6/18/20"] - covid_cases_df["6/17/20"]
covid_cases_df["6/17/20"] = covid_cases_df["6/17/20"] - covid_cases_df["6/16/20"]
covid_cases_df["6/16/20"] = covid_cases_df["6/16/20"] - covid_cases_df["6/15/20"]
covid_cases_df["6/15/20"] = covid_cases_df["6/15/20"] - covid_cases_df["6/14/20"]
covid_cases_df["6/14/20"] = covid_cases_df["6/14/20"] - covid_cases_df["6/13/20"]
covid_cases_df["6/13/20"] = covid_cases_df["6/13/20"] - covid_cases_df["6/12/20"]
covid_cases_df["6/12/20"] = covid_cases_df["6/12/20"] - covid_cases_df["6/11/20"]
covid_cases_df["6/11/20"] = covid_cases_df["6/11/20"] - covid_cases_df["6/10/20"]
covid_cases_df["6/10/20"] = covid_cases_df["6/10/20"] - covid_cases_df["6/9/20"]
covid_cases_df["6/9/20"] = covid_cases_df["6/9/20"] - covid_cases_df["6/8/20"]
covid_cases_df["6/8/20"] = covid_cases_df["6/8/20"] - covid_cases_df["6/7/20"]
covid_cases_df["6/7/20"] = covid_cases_df["6/7/20"] - covid_cases_df["6/6/20"]
covid_cases_df["6/6/20"] = covid_cases_df["6/6/20"] - covid_cases_df["6/5/20"]
covid_cases_df["6/5/20"] = covid_cases_df["6/5/20"] - covid_cases_df["6/4/20"]
covid_cases_df["6/4/20"] = covid_cases_df["6/4/20"] - covid_cases_df["6/3/20"]
covid_cases_df["6/3/20"] = covid_cases_df["6/3/20"] - covid_cases_df["6/2/20"]
covid_cases_df["6/2/20"] = covid_cases_df["6/2/20"] - covid_cases_df["6/1/20"]
covid_cases_df["6/1/20"] = covid_cases_df["6/1/20"] - covid_cases_df["5/31/20"]
covid_cases_df["5/31/20"] = covid_cases_df["5/31/20"] - covid_cases_df["5/30/20"]
covid_cases_df["5/30/20"] = covid_cases_df["5/30/20"] - covid_cases_df["5/29/20"]
covid_cases_df["5/29/20"] = covid_cases_df["5/29/20"] - covid_cases_df["5/28/20"]
covid_cases_df["5/28/20"] = covid_cases_df["5/28/20"] - covid_cases_df["5/27/20"]
covid_cases_df["5/27/20"] = covid_cases_df["5/27/20"] - covid_cases_df["5/26/20"]
covid_cases_df["5/26/20"] = covid_cases_df["5/26/20"] - covid_cases_df["5/25/20"]
covid_cases_df["5/25/20"] = covid_cases_df["5/25/20"] - covid_cases_df["5/24/20"]
covid_cases_df["5/24/20"] = covid_cases_df["5/24/20"] - covid_cases_df["5/23/20"]
covid_cases_df["5/23/20"] = covid_cases_df["5/23/20"] - covid_cases_df["5/22/20"]
covid_cases_df["5/22/20"] = covid_cases_df["5/22/20"] - covid_cases_df["5/21/20"]
covid_cases_df["5/21/20"] = covid_cases_df["5/21/20"] - covid_cases_df["5/20/20"]
covid_cases_df["5/20/20"] = covid_cases_df["5/20/20"] - covid_cases_df["5/19/20"]
covid_cases_df["5/19/20"] = covid_cases_df["5/19/20"] - covid_cases_df["5/18/20"]
covid_cases_df["5/18/20"] = covid_cases_df["5/18/20"] - covid_cases_df["5/17/20"]
covid_cases_df["5/17/20"] = covid_cases_df["5/17/20"] - covid_cases_df["5/16/20"]
covid_cases_df["5/16/20"] = covid_cases_df["5/16/20"] - covid_cases_df["5/15/20"]
covid_cases_df["5/15/20"] = covid_cases_df["5/15/20"] - covid_cases_df["5/14/20"]
covid_cases_df["5/14/20"] = covid_cases_df["5/14/20"] - covid_cases_df["5/13/20"]
covid_cases_df["5/13/20"] = covid_cases_df["5/13/20"] - covid_cases_df["5/12/20"]
covid_cases_df["5/12/20"] = covid_cases_df["5/12/20"] - covid_cases_df["5/11/20"]
covid_cases_df["5/11/20"] = covid_cases_df["5/11/20"] - covid_cases_df["5/10/20"]
covid_cases_df["5/10/20"] = covid_cases_df["5/10/20"] - covid_cases_df["5/9/20"]
covid_cases_df["5/9/20"] = covid_cases_df["5/9/20"] - covid_cases_df["5/8/20"]
covid_cases_df["5/8/20"] = covid_cases_df["5/8/20"] - covid_cases_df["5/7/20"]
covid_cases_df["5/7/20"] = covid_cases_df["5/7/20"] - covid_cases_df["5/6/20"]
covid_cases_df["5/6/20"] = covid_cases_df["5/6/20"] - covid_cases_df["5/5/20"]
covid_cases_df["5/5/20"] = covid_cases_df["5/5/20"] - covid_cases_df["5/4/20"]
covid_cases_df["5/4/20"] = covid_cases_df["5/4/20"] - covid_cases_df["5/3/20"]
covid_cases_df["5/3/20"] = covid_cases_df["5/3/20"] - covid_cases_df["5/2/20"]
covid_cases_df["5/2/20"] = covid_cases_df["5/2/20"] - covid_cases_df["5/1/20"]
covid_cases_df["5/1/20"] = covid_cases_df["5/1/20"] - covid_cases_df["4/30/20"]
covid_cases_df["4/30/20"] = covid_cases_df["4/30/20"] - covid_cases_df["4/29/20"]
covid_cases_df["4/29/20"] = covid_cases_df["4/29/20"] - covid_cases_df["4/28/20"]
covid_cases_df["4/28/20"] = covid_cases_df["4/28/20"] - covid_cases_df["4/27/20"]
covid_cases_df["4/27/20"] = covid_cases_df["4/27/20"] - covid_cases_df["4/26/20"]
covid_cases_df["4/26/20"] = covid_cases_df["4/26/20"] - covid_cases_df["4/25/20"]
covid_cases_df["4/25/20"] = covid_cases_df["4/25/20"] - covid_cases_df["4/24/20"]
covid_cases_df["4/24/20"] = covid_cases_df["4/24/20"] - covid_cases_df["4/23/20"]
covid_cases_df["4/23/20"] = covid_cases_df["4/23/20"] - covid_cases_df["4/22/20"]
covid_cases_df["4/22/20"] = covid_cases_df["4/22/20"] - covid_cases_df["4/21/20"]
covid_cases_df["4/21/20"] = covid_cases_df["4/21/20"] - covid_cases_df["4/20/20"]
covid_cases_df["4/20/20"] = covid_cases_df["4/20/20"] - covid_cases_df["4/19/20"]
covid_cases_df["4/19/20"] = covid_cases_df["4/19/20"] - covid_cases_df["4/18/20"]
covid_cases_df["4/18/20"] = covid_cases_df["4/18/20"] - covid_cases_df["4/17/20"]
covid_cases_df["4/17/20"] = covid_cases_df["4/17/20"] - covid_cases_df["4/16/20"]
covid_cases_df["4/16/20"] = covid_cases_df["4/16/20"] - covid_cases_df["4/15/20"]
covid_cases_df["4/15/20"] = covid_cases_df["4/15/20"] - covid_cases_df["4/15/20"]
covid_cases_df["4/14/20"] = covid_cases_df["4/14/20"] - covid_cases_df["4/13/20"]
covid_cases_df["4/13/20"] = covid_cases_df["4/13/20"] - covid_cases_df["4/12/20"]
covid_cases_df["4/12/20"] = covid_cases_df["4/12/20"] - covid_cases_df["4/11/20"]
covid_cases_df["4/11/20"] = covid_cases_df["4/11/20"] - covid_cases_df["4/10/20"]
covid_cases_df["4/10/20"] = covid_cases_df["4/10/20"] - covid_cases_df["4/9/20"]
covid_cases_df["4/9/20"] = covid_cases_df["4/9/20"] - covid_cases_df["4/8/20"]
covid_cases_df["4/8/20"] = covid_cases_df["4/8/20"] - covid_cases_df["4/7/20"]
covid_cases_df["4/7/20"] = covid_cases_df["4/7/20"] - covid_cases_df["4/6/20"]
covid_cases_df["4/6/20"] = covid_cases_df["4/6/20"] - covid_cases_df["4/5/20"]
covid_cases_df["4/5/20"] = covid_cases_df["4/5/20"] - covid_cases_df["4/4/20"]
covid_cases_df["4/4/20"] = covid_cases_df["4/4/20"] - covid_cases_df["4/3/20"]
covid_cases_df["4/3/20"] = covid_cases_df["4/3/20"] - covid_cases_df["4/2/20"]
covid_cases_df["4/2/20"] = covid_cases_df["4/2/20"] - covid_cases_df["4/1/20"]
covid_cases_df["4/1/20"] = covid_cases_df["4/1/20"] - covid_cases_df["3/31/20"]
covid_cases_df["3/31/20"] = covid_cases_df["3/31/20"] - covid_cases_df["3/30/20"]
covid_cases_df["3/30/20"] = covid_cases_df["3/30/20"] - covid_cases_df["3/29/20"]
covid_cases_df["3/29/20"] = covid_cases_df["3/29/20"] - covid_cases_df["3/28/20"]
covid_cases_df["3/28/20"] = covid_cases_df["3/28/20"] - covid_cases_df["3/27/20"]
covid_cases_df["3/27/20"] = covid_cases_df["3/27/20"] - covid_cases_df["3/26/20"]
covid_cases_df["3/26/20"] = covid_cases_df["3/26/20"] - covid_cases_df["3/25/20"]
covid_cases_df["3/25/20"] = covid_cases_df["3/25/20"] - covid_cases_df["3/24/20"]
covid_cases_df["3/24/20"] = covid_cases_df["3/24/20"] - covid_cases_df["3/23/20"]
covid_cases_df["3/23/20"] = covid_cases_df["3/23/20"] - covid_cases_df["3/22/20"]
covid_cases_df["3/22/20"] = covid_cases_df["3/22/20"] - covid_cases_df["3/21/20"]
covid_cases_df["3/21/20"] = covid_cases_df["3/21/20"] - covid_cases_df["3/20/20"]
covid_cases_df["3/20/20"] = covid_cases_df["3/20/20"] - covid_cases_df["3/19/20"]
covid_cases_df["3/19/20"] = covid_cases_df["3/19/20"] - covid_cases_df["3/18/20"]
covid_cases_df["3/18/20"] = covid_cases_df["3/18/20"] - covid_cases_df["3/17/20"]
covid_cases_df["3/17/20"] = covid_cases_df["3/17/20"] - covid_cases_df["3/16/20"]
covid_cases_df["3/16/20"] = covid_cases_df["3/16/20"] - covid_cases_df["3/15/20"]
covid_cases_df["3/15/20"] = covid_cases_df["3/15/20"] - covid_cases_df["3/14/20"]
covid_cases_df["3/14/20"] = covid_cases_df["3/14/20"] - covid_cases_df["3/13/20"]
covid_cases_df["3/13/20"] = covid_cases_df["3/13/20"] - covid_cases_df["3/12/20"]
covid_cases_df["3/12/20"] = covid_cases_df["3/12/20"] - covid_cases_df["3/11/20"]
covid_cases_df["3/11/20"] = covid_cases_df["3/11/20"] - covid_cases_df["3/10/20"]
covid_cases_df["3/10/20"] = covid_cases_df["3/10/20"] - covid_cases_df["3/9/20"]
covid_cases_df["3/9/20"] = covid_cases_df["3/9/20"] - covid_cases_df["3/8/20"]
covid_cases_df["3/8/20"] = covid_cases_df["3/8/20"] - covid_cases_df["3/7/20"]
covid_cases_df["3/7/20"] = covid_cases_df["3/7/20"] - covid_cases_df["3/6/20"]
covid_cases_df["3/6/20"] = covid_cases_df["3/6/20"] - covid_cases_df["3/5/20"]
covid_cases_df["3/5/20"] = covid_cases_df["3/5/20"] - covid_cases_df["3/4/20"]
covid_cases_df["3/4/20"] = covid_cases_df["3/4/20"] - covid_cases_df["3/3/20"]
covid_cases_df["3/3/20"] = covid_cases_df["3/3/20"] - covid_cases_df["3/2/20"]
covid_cases_df["3/2/20"] = covid_cases_df["3/2/20"] - covid_cases_df["3/1/20"]
covid_cases_df["3/1/20"] = covid_cases_df["3/1/20"] - covid_cases_df["2/29/20"]  


covid_deaths["7/24/20"] = covid_deaths["7/24/20"] - covid_deaths["7/23/20"]
covid_deaths["7/23/20"] = covid_deaths["7/23/20"] - covid_deaths["7/22/20"]
covid_deaths["7/22/20"] = covid_deaths["7/22/20"] - covid_deaths["7/21/20"]
covid_deaths["7/21/20"] = covid_deaths["7/21/20"] - covid_deaths["7/20/20"]
covid_deaths["7/20/20"] = covid_deaths["7/20/20"] - covid_deaths["7/19/20"]
covid_deaths["7/19/20"] = covid_deaths["7/19/20"] - covid_deaths["7/18/20"]
covid_deaths["7/18/20"] = covid_deaths["7/18/20"] - covid_deaths["7/17/20"]
covid_deaths["7/17/20"] = covid_deaths["7/17/20"] - covid_deaths["7/16/20"]
covid_deaths["7/16/20"] = covid_deaths["7/16/20"] - covid_deaths["7/15/20"]
covid_deaths["7/15/20"] = covid_deaths["7/15/20"] - covid_deaths["7/14/20"]
covid_deaths["7/14/20"] = covid_deaths["7/14/20"] - covid_deaths["7/13/20"]
covid_deaths["7/13/20"] = covid_deaths["7/13/20"] - covid_deaths["7/12/20"]
covid_deaths["7/12/20"] = covid_deaths["7/12/20"] - covid_deaths["7/11/20"]
covid_deaths["7/11/20"] = covid_deaths["7/11/20"] - covid_deaths["7/10/20"]
covid_deaths["7/10/20"] = covid_deaths["7/10/20"] - covid_deaths["7/9/20"]
covid_deaths["7/9/20"] = covid_deaths["7/9/20"] - covid_deaths["7/9/20"]
covid_deaths["7/8/20"] = covid_deaths["7/8/20"] - covid_deaths["7/7/20"]
covid_deaths["7/7/20"] = covid_deaths["7/7/20"] - covid_deaths["7/6/20"]
covid_deaths["7/6/20"] = covid_deaths["7/6/20"] - covid_deaths["7/5/20"]
covid_deaths["7/5/20"] = covid_deaths["7/5/20"] - covid_deaths["7/4/20"]
covid_deaths["7/4/20"] = covid_deaths["7/4/20"] - covid_deaths["7/3/20"]
covid_deaths["7/3/20"] = covid_deaths["7/3/20"] - covid_deaths["7/2/20"]
covid_deaths["7/2/20"] = covid_deaths["7/2/20"] - covid_deaths["7/1/20"]
covid_deaths["7/1/20"] = covid_deaths["7/1/20"] - covid_deaths["6/30/20"]
covid_deaths["6/30/20"] = covid_deaths["6/30/20"] - covid_deaths["6/29/20"]
covid_deaths["6/29/20"] = covid_deaths["6/29/20"] - covid_deaths["6/28/20"]
covid_deaths["6/28/20"] = covid_deaths["6/28/20"] - covid_deaths["6/27/20"]
covid_deaths["6/27/20"] = covid_deaths["6/27/20"] - covid_deaths["6/26/20"]
covid_deaths["6/26/20"] = covid_deaths["6/26/20"] - covid_deaths["6/25/20"]
covid_deaths["6/25/20"] = covid_deaths["6/25/20"] - covid_deaths["6/24/20"]
covid_deaths["6/24/20"] = covid_deaths["6/24/20"] - covid_deaths["6/23/20"]
covid_deaths["6/23/20"] = covid_deaths["6/23/20"] - covid_deaths["6/22/20"]
covid_deaths["6/22/20"] = covid_deaths["6/22/20"] - covid_deaths["6/21/20"]
covid_deaths["6/21/20"] = covid_deaths["6/21/20"] - covid_deaths["6/20/20"]
covid_deaths["6/20/20"] = covid_deaths["6/20/20"] - covid_deaths["6/19/20"]
covid_deaths["6/19/20"] = covid_deaths["6/19/20"] - covid_deaths["6/18/20"]
covid_deaths["6/18/20"] = covid_deaths["6/18/20"] - covid_deaths["6/17/20"]
covid_deaths["6/17/20"] = covid_deaths["6/17/20"] - covid_deaths["6/16/20"]
covid_deaths["6/16/20"] = covid_deaths["6/16/20"] - covid_deaths["6/15/20"]
covid_deaths["6/15/20"] = covid_deaths["6/15/20"] - covid_deaths["6/14/20"]
covid_deaths["6/14/20"] = covid_deaths["6/14/20"] - covid_deaths["6/13/20"]
covid_deaths["6/13/20"] = covid_deaths["6/13/20"] - covid_deaths["6/12/20"]
covid_deaths["6/12/20"] = covid_deaths["6/12/20"] - covid_deaths["6/11/20"]
covid_deaths["6/11/20"] = covid_deaths["6/11/20"] - covid_deaths["6/10/20"]
covid_deaths["6/10/20"] = covid_deaths["6/10/20"] - covid_deaths["6/9/20"]
covid_deaths["6/9/20"] = covid_deaths["6/9/20"] - covid_deaths["6/8/20"]
covid_deaths["6/8/20"] = covid_deaths["6/8/20"] - covid_deaths["6/7/20"]
covid_deaths["6/7/20"] = covid_deaths["6/7/20"] - covid_deaths["6/6/20"]
covid_deaths["6/6/20"] = covid_deaths["6/6/20"] - covid_deaths["6/5/20"]
covid_deaths["6/5/20"] = covid_deaths["6/5/20"] - covid_deaths["6/4/20"]
covid_deaths["6/4/20"] = covid_deaths["6/4/20"] - covid_deaths["6/3/20"]
covid_deaths["6/3/20"] = covid_deaths["6/3/20"] - covid_deaths["6/2/20"]
covid_deaths["6/2/20"] = covid_deaths["6/2/20"] - covid_deaths["6/1/20"]
covid_deaths["6/1/20"] = covid_deaths["6/1/20"] - covid_deaths["5/31/20"]
covid_deaths["5/31/20"] = covid_deaths["5/31/20"] - covid_deaths["5/30/20"]
covid_deaths["5/30/20"] = covid_deaths["5/30/20"] - covid_deaths["5/29/20"]
covid_deaths["5/29/20"] = covid_deaths["5/29/20"] - covid_deaths["5/28/20"]
covid_deaths["5/28/20"] = covid_deaths["5/28/20"] - covid_deaths["5/27/20"]
covid_deaths["5/27/20"] = covid_deaths["5/27/20"] - covid_deaths["5/26/20"]
covid_deaths["5/26/20"] = covid_deaths["5/26/20"] - covid_deaths["5/25/20"]
covid_deaths["5/25/20"] = covid_deaths["5/25/20"] - covid_deaths["5/24/20"]
covid_deaths["5/24/20"] = covid_deaths["5/24/20"] - covid_deaths["5/23/20"]
covid_deaths["5/23/20"] = covid_deaths["5/23/20"] - covid_deaths["5/22/20"]
covid_deaths["5/22/20"] = covid_deaths["5/22/20"] - covid_deaths["5/21/20"]
covid_deaths["5/21/20"] = covid_deaths["5/21/20"] - covid_deaths["5/20/20"]
covid_deaths["5/20/20"] = covid_deaths["5/20/20"] - covid_deaths["5/19/20"]
covid_deaths["5/19/20"] = covid_deaths["5/19/20"] - covid_deaths["5/18/20"]
covid_deaths["5/18/20"] = covid_deaths["5/18/20"] - covid_deaths["5/17/20"]
covid_deaths["5/17/20"] = covid_deaths["5/17/20"] - covid_deaths["5/16/20"]
covid_deaths["5/16/20"] = covid_deaths["5/16/20"] - covid_deaths["5/15/20"]
covid_deaths["5/15/20"] = covid_deaths["5/15/20"] - covid_deaths["5/14/20"]
covid_deaths["5/14/20"] = covid_deaths["5/14/20"] - covid_deaths["5/13/20"]
covid_deaths["5/13/20"] = covid_deaths["5/13/20"] - covid_deaths["5/12/20"]
covid_deaths["5/12/20"] = covid_deaths["5/12/20"] - covid_deaths["5/11/20"]
covid_deaths["5/11/20"] = covid_deaths["5/11/20"] - covid_deaths["5/10/20"]
covid_deaths["5/10/20"] = covid_deaths["5/10/20"] - covid_deaths["5/9/20"]
covid_deaths["5/9/20"] = covid_deaths["5/9/20"] - covid_deaths["5/8/20"]
covid_deaths["5/8/20"] = covid_deaths["5/8/20"] - covid_deaths["5/7/20"]
covid_deaths["5/7/20"] = covid_deaths["5/7/20"] - covid_deaths["5/6/20"]
covid_deaths["5/6/20"] = covid_deaths["5/6/20"] - covid_deaths["5/5/20"]
covid_deaths["5/5/20"] = covid_deaths["5/5/20"] - covid_deaths["5/4/20"]
covid_deaths["5/4/20"] = covid_deaths["5/4/20"] - covid_deaths["5/3/20"]
covid_deaths["5/3/20"] = covid_deaths["5/3/20"] - covid_deaths["5/2/20"]
covid_deaths["5/2/20"] = covid_deaths["5/2/20"] - covid_deaths["5/1/20"]
covid_deaths["5/1/20"] = covid_deaths["5/1/20"] - covid_deaths["4/30/20"]
covid_deaths["4/30/20"] = covid_deaths["4/30/20"] - covid_deaths["4/29/20"]
covid_deaths["4/29/20"] = covid_deaths["4/29/20"] - covid_deaths["4/28/20"]
covid_deaths["4/28/20"] = covid_deaths["4/28/20"] - covid_deaths["4/27/20"]
covid_deaths["4/27/20"] = covid_deaths["4/27/20"] - covid_deaths["4/26/20"]
covid_deaths["4/26/20"] = covid_deaths["4/26/20"] - covid_deaths["4/25/20"]
covid_deaths["4/25/20"] = covid_deaths["4/25/20"] - covid_deaths["4/24/20"]
covid_deaths["4/24/20"] = covid_deaths["4/24/20"] - covid_deaths["4/23/20"]
covid_deaths["4/23/20"] = covid_deaths["4/23/20"] - covid_deaths["4/22/20"]
covid_deaths["4/22/20"] = covid_deaths["4/22/20"] - covid_deaths["4/21/20"]
covid_deaths["4/21/20"] = covid_deaths["4/21/20"] - covid_deaths["4/20/20"]
covid_deaths["4/20/20"] = covid_deaths["4/20/20"] - covid_deaths["4/19/20"]
covid_deaths["4/19/20"] = covid_deaths["4/19/20"] - covid_deaths["4/18/20"]
covid_deaths["4/18/20"] = covid_deaths["4/18/20"] - covid_deaths["4/17/20"]
covid_deaths["4/17/20"] = covid_deaths["4/17/20"] - covid_deaths["4/16/20"]
covid_deaths["4/16/20"] = covid_deaths["4/16/20"] - covid_deaths["4/15/20"]
covid_deaths["4/15/20"] = covid_deaths["4/15/20"] - covid_deaths["4/15/20"]
covid_deaths["4/14/20"] = covid_deaths["4/14/20"] - covid_deaths["4/13/20"]
covid_deaths["4/13/20"] = covid_deaths["4/13/20"] - covid_deaths["4/12/20"]
covid_deaths["4/12/20"] = covid_deaths["4/12/20"] - covid_deaths["4/11/20"]
covid_deaths["4/11/20"] = covid_deaths["4/11/20"] - covid_deaths["4/10/20"]
covid_deaths["4/10/20"] = covid_deaths["4/10/20"] - covid_deaths["4/9/20"]
covid_deaths["4/9/20"] = covid_deaths["4/9/20"] - covid_deaths["4/8/20"]
covid_deaths["4/8/20"] = covid_deaths["4/8/20"] - covid_deaths["4/7/20"]
covid_deaths["4/7/20"] = covid_deaths["4/7/20"] - covid_deaths["4/6/20"]
covid_deaths["4/6/20"] = covid_deaths["4/6/20"] - covid_deaths["4/5/20"]
covid_deaths["4/5/20"] = covid_deaths["4/5/20"] - covid_deaths["4/4/20"]
covid_deaths["4/4/20"] = covid_deaths["4/4/20"] - covid_deaths["4/3/20"]
covid_deaths["4/3/20"] = covid_deaths["4/3/20"] - covid_deaths["4/2/20"]
covid_deaths["4/2/20"] = covid_deaths["4/2/20"] - covid_deaths["4/1/20"]
covid_deaths["4/1/20"] = covid_deaths["4/1/20"] - covid_deaths["3/31/20"]
covid_deaths["3/31/20"] = covid_deaths["3/31/20"] - covid_deaths["3/30/20"]
covid_deaths["3/30/20"] = covid_deaths["3/30/20"] - covid_deaths["3/29/20"]
covid_deaths["3/29/20"] = covid_deaths["3/29/20"] - covid_deaths["3/28/20"]
covid_deaths["3/28/20"] = covid_deaths["3/28/20"] - covid_deaths["3/27/20"]
covid_deaths["3/27/20"] = covid_deaths["3/27/20"] - covid_deaths["3/26/20"]
covid_deaths["3/26/20"] = covid_deaths["3/26/20"] - covid_deaths["3/25/20"]
covid_deaths["3/25/20"] = covid_deaths["3/25/20"] - covid_deaths["3/24/20"]
covid_deaths["3/24/20"] = covid_deaths["3/24/20"] - covid_deaths["3/23/20"]
covid_deaths["3/23/20"] = covid_deaths["3/23/20"] - covid_deaths["3/22/20"]
covid_deaths["3/22/20"] = covid_deaths["3/22/20"] - covid_deaths["3/21/20"]
covid_deaths["3/21/20"] = covid_deaths["3/21/20"] - covid_deaths["3/20/20"]
covid_deaths["3/20/20"] = covid_deaths["3/20/20"] - covid_deaths["3/19/20"]
covid_deaths["3/19/20"] = covid_deaths["3/19/20"] - covid_deaths["3/18/20"]
covid_deaths["3/18/20"] = covid_deaths["3/18/20"] - covid_deaths["3/17/20"]
covid_deaths["3/17/20"] = covid_deaths["3/17/20"] - covid_deaths["3/16/20"]
covid_deaths["3/16/20"] = covid_deaths["3/16/20"] - covid_deaths["3/15/20"]
covid_deaths["3/15/20"] = covid_deaths["3/15/20"] - covid_deaths["3/14/20"]
covid_deaths["3/14/20"] = covid_deaths["3/14/20"] - covid_deaths["3/13/20"]
covid_deaths["3/13/20"] = covid_deaths["3/13/20"] - covid_deaths["3/12/20"]
covid_deaths["3/12/20"] = covid_deaths["3/12/20"] - covid_deaths["3/11/20"]
covid_deaths["3/11/20"] = covid_deaths["3/11/20"] - covid_deaths["3/10/20"]
covid_deaths["3/10/20"] = covid_deaths["3/10/20"] - covid_deaths["3/9/20"]
covid_deaths["3/9/20"] = covid_deaths["3/9/20"] - covid_deaths["3/8/20"]
covid_deaths["3/8/20"] = covid_deaths["3/8/20"] - covid_deaths["3/7/20"]
covid_deaths["3/7/20"] = covid_deaths["3/7/20"] - covid_deaths["3/6/20"]
covid_deaths["3/6/20"] = covid_deaths["3/6/20"] - covid_deaths["3/5/20"]
covid_deaths["3/5/20"] = covid_deaths["3/5/20"] - covid_deaths["3/4/20"]
covid_deaths["3/4/20"] = covid_deaths["3/4/20"] - covid_deaths["3/3/20"]
covid_deaths["3/3/20"] = covid_deaths["3/3/20"] - covid_deaths["3/2/20"]
covid_deaths["3/2/20"] = covid_deaths["3/2/20"] - covid_deaths["3/1/20"]
covid_deaths["3/1/20"] = covid_deaths["3/1/20"] - covid_deaths["2/29/20"] 
 

#################################################################################################
# Covid dataframe renaming and subsetting, 
#################################################################################################
## Rename variables
colnames(covid_cases_df)
summary(covid_cases_df)
names(covid_cases_df)[names(covid_cases_df) == "Admin2"] = "County.Name"
names(covid_cases_df)[names(covid_cases_df) == "Province_State"] = "State.Name"
names(covid_deaths)[names(covid_deaths) == "Admin2"] = "County.Name"
names(covid_deaths)[names(covid_deaths) == "Province_State"] = "State.Name"

covid_cases_df = covid_cases_df[!(covid_cases_df$State.Name == "Puerto Rico" | 
                               covid_cases_df$State.Name == "American Samoa" | covid_cases_df$State.Name == 
                               "Guam" | covid_cases_df$State.Name == "Virgin Islands" | 
                               covid_cases_df$State.Name == "Northern Mariana Islands"), ] 
# to delete obs if State = Puerto Rico, Guam, American Samoa, 
# Northern Mariana island, or Virgin islands            

covid_deaths = covid_deaths[!(covid_deaths$State.Name == "Puerto Rico" | 
                                 covid_deaths$State.Name == "American Samoa" | covid_deaths$State.Name == 
                                 "Guam" | covid_deaths$State.Name == "Virgin Islands" | 
                                 covid_deaths$State.Name == "Northern Mariana Islands"), ] 
# to delete obs if State = Puerto Rico, Guam, American Samoa, 
# Northern Mariana island, or Virgin islands            


## subset only needed variables
colnames(covid_deaths) 
vars = c("State.Name",  "County.Name", "Population", "FIPS",  "3/11/20","3/12/20",
          "3/13/20", "3/14/20", "3/15/20", "3/16/20", "3/17/20",  "3/18/20",  "3/19/20",
          "3/20/20", "3/21/20", "3/22/20", "3/23/20", "3/24/20", "3/25/20", "3/26/20", "3/27/20",
          "3/28/20", "3/29/20", "3/30/20", "3/31/20", "4/1/20", "4/2/20", "4/3/20",  
          "4/4/20", "4/5/20", "4/6/20", "4/7/20", "4/8/20", "4/9/20","4/10/20", "4/11/20", 
          "4/12/20","4/13/20",  "4/14/20", "4/15/20", "4/16/20", "4/17/20", "4/18/20", "4/19/20", 
          "4/20/20", "4/21/20", "4/22/20", "4/23/20", "4/24/20", "4/25/20", "4/26/20",
          "4/27/20",  "4/28/20", "4/29/20", "4/30/20","5/1/20", "5/2/20", "5/3/20", "5/4/20",        
          "5/5/20", "5/6/20", "5/7/20", "5/8/20", "5/9/20", "5/10/20", "5/11/20", "5/12/20", 
          "5/13/20", "5/14/20", "5/15/20", "5/16/20", "5/17/20", "5/18/20", "5/19/20", "5/20/20",
          "5/21/20", "5/22/20", "5/23/20", "5/24/20", "5/25/20",  "5/26/20", "5/27/20", "5/28/20",
          "5/29/20",  "5/30/20",  "5/31/20",  "6/1/20", "6/2/20", "6/3/20",  "6/4/20", "6/5/20",
          "6/6/20", "6/7/20", "6/8/20", "6/9/20", "6/10/20", "6/11/20", "6/12/20", "6/13/20", 
          "6/14/20", "6/15/20", "6/16/20", "6/17/20", "6/18/20",  "6/19/20", "6/20/20", "6/21/20",
          "6/22/20", "6/23/20", "6/24/20", "6/25/20", "6/26/20", "6/27/20", "6/28/20", "6/29/20",              
          "6/30/20", "7/1/20", "7/2/20", "7/3/20", "7/4/20","7/5/20", "7/6/20","7/7/20", "7/8/20",
          "7/9/20" , "7/10/20", "7/11/20" , "7/12/20", "7/13/20" ,"7/14/20" , "7/15/20", "7/16/20",
          "7/17/20","7/18/20", "7/19/20", "7/20/20" , "7/21/20" ,"7/22/20" ,"7/23/20" ,"7/24/20" )

covid_cases_df = covid_cases_df[vars]
covid_deaths = covid_deaths[vars]

## reshape covid dataframes from wide to long
covid_cases_long = melt(setDT(covid_cases_df), id.vars = c("State.Name", "County.Name", "FIPS"), 
                         variable.name = "Date.Local")
names(covid_cases_long)[names(covid_cases_long) == "value"] = "cases"

covid_deaths_long = melt(setDT(covid_deaths), id.vars = c("State.Name", "County.Name", "FIPS", 
                                                           "Population"), 
                          variable.name = "Date.Local")
names(covid_deaths_long)[names(covid_deaths_long) == "value"] = "deaths"


# exclude County.Name equal to "Unassigned"
covid_cases_long = subset(covid_cases_long, County.Name != "Unassigned")
covid_deaths_long = subset(covid_deaths_long, County.Name != "Unassigned")

# merge population with covid_cases_long
vars = c("Population")
covid_deaths_long = as.data.frame(covid_deaths_long)
covid_cases_long = as.data.frame(covid_cases_long)
popest = covid_deaths_long[vars]
covid_cases_long = cbind(covid_cases_long, popest)
rm(popest)

# exclude Population equal to "0"
covid_cases_long = subset(covid_cases_long, Population != 0)
covid_deaths_long = subset(covid_deaths_long, Population != 0)

# exclude deaths less than 0
covid_deaths_long = subset(covid_deaths_long, deaths >= 0)
covid_cases_long = subset(covid_cases_long, cases >= 0)




#################################################################################################
# Covid dataframe renaming and subsetting, for case-fatality data
#################################################################################################
## Rename variables
colnames(covid_cases2)
summary(covid_cases2)
names(covid_cases2)[names(covid_cases2) == "Admin2"] = "County.Name"
names(covid_cases2)[names(covid_cases2) == "Province_State"] = "State.Name"
names(covid_deaths2)[names(covid_deaths2) == "Admin2"] = "County.Name"
names(covid_deaths2)[names(covid_deaths2) == "Province_State"] = "State.Name"

covid_cases2 = covid_cases2[!(covid_cases2$State.Name == "Puerto Rico" | 
                               covid_cases2$State.Name == "American Samoa" | covid_cases2$State.Name == 
                               "Guam" | covid_cases2$State.Name == "Virgin Islands" | 
                               covid_cases2$State.Name == "Northern Mariana Islands"), ] 
# to delete obs if State = Puerto Rico, Guam, American Samoa, 
# Northern Mariana island, or Virgin islands            

covid_deaths2 = covid_deaths2[!(covid_deaths2$State.Name == "Puerto Rico" | 
                                 covid_deaths2$State.Name == "American Samoa" | covid_deaths2$State.Name == 
                                 "Guam" | covid_deaths2$State.Name == "Virgin Islands" | 
                                 covid_deaths2$State.Name == "Northern Mariana Islands"), ] 
# to delete obs if State = Puerto Rico, Guam, American Samoa, 
# Northern Mariana island, or Virgin islands            


## subset only needed variables
colnames(covid_deaths2) 
vars = c("State.Name",  "County.Name",  "Population", "FIPS",  "3/11/20","3/12/20",
          "3/13/20", "3/14/20", "3/15/20", "3/16/20", "3/17/20",  "3/18/20",  "3/19/20",
          "3/20/20", "3/21/20", "3/22/20", "3/23/20", "3/24/20", "3/25/20", "3/26/20", "3/27/20",
          "3/28/20", "3/29/20", "3/30/20", "3/31/20", "4/1/20", "4/2/20", "4/3/20",  
          "4/4/20", "4/5/20", "4/6/20", "4/7/20", "4/8/20", "4/9/20","4/10/20", "4/11/20", 
          "4/12/20","4/13/20",  "4/14/20", "4/15/20", "4/16/20", "4/17/20", "4/18/20", "4/19/20", 
          "4/20/20", "4/21/20", "4/22/20", "4/23/20", "4/24/20", "4/25/20", "4/26/20",
          "4/27/20",  "4/28/20", "4/29/20", "4/30/20","5/1/20", "5/2/20", "5/3/20", "5/4/20",        
          "5/5/20", "5/6/20", "5/7/20", "5/8/20", "5/9/20", "5/10/20", "5/11/20", "5/12/20", 
          "5/13/20", "5/14/20", "5/15/20", "5/16/20", "5/17/20", "5/18/20", "5/19/20", "5/20/20",
          "5/21/20", "5/22/20", "5/23/20", "5/24/20", "5/25/20",  "5/26/20", "5/27/20", "5/28/20",
          "5/29/20",  "5/30/20",  "5/31/20",  "6/1/20", "6/2/20", "6/3/20",  "6/4/20", "6/5/20",
          "6/6/20", "6/7/20", "6/8/20", "6/9/20", "6/10/20", "6/11/20", "6/12/20", "6/13/20", 
          "6/14/20", "6/15/20", "6/16/20", "6/17/20", "6/18/20",  "6/19/20", "6/20/20", "6/21/20",
          "6/22/20", "6/23/20", "6/24/20", "6/25/20", "6/26/20", "6/27/20", "6/28/20", "6/29/20",              
          "6/30/20", "7/1/20", "7/2/20", "7/3/20", "7/4/20","7/5/20", "7/6/20","7/7/20", "7/8/20",
          "7/9/20" , "7/10/20", "7/11/20" , "7/12/20", "7/13/20" ,"7/14/20" , "7/15/20", "7/16/20",
          "7/17/20","7/18/20", "7/19/20", "7/20/20" , "7/21/20" ,"7/22/20" ,"7/23/20" ,"7/24/20" )

covid_cases2 = covid_cases2[vars]
covid_deaths2 = covid_deaths2[vars]

## reshape covid dataframes from wide to long
library(data.table)
library(reshape2)
covid_cases2_long = melt(setDT(covid_cases2), id.vars = c("State.Name", "County.Name", "FIPS"), 
                         variable.name = "Date.Local")
names(covid_cases2_long)[names(covid_cases2_long) == "value"] = "cases"

covid_deaths2_long = melt(setDT(covid_deaths2), id.vars = c("State.Name", "County.Name", "FIPS", 
                                                           "Population"), 
                          variable.name = "Date.Local")
names(covid_deaths2_long)[names(covid_deaths2_long) == "value"] = "deaths"


# exclude County.Name equal to "Unassigned"
covid_cases2_long = subset(covid_cases2_long, County.Name != "Unassigned")
covid_deaths2_long = subset(covid_deaths2_long, County.Name != "Unassigned")

# merge population with covid_cases2_long
covid_deaths2_long = as.data.frame(covid_deaths2_long)
covid_cases2_long = as.data.frame(covid_cases2_long)


# exclude Population equal to "0"
covid_deaths2_long = subset(covid_deaths2_long, Population != 0)




#################################################################################################
###                     Download and merge Air Pollution Data from EPA                        ###
#############                         for 2015 - 2020                              ##############
#################################################################################################

ap_vars = c("State.Name", "County.Name", "City.Name", "Date.Local", "Arithmetic.Mean",
             "AQI", "X1st.Max.Value")

## Ozone
download.file("https://aqs.epa.gov/aqsweb/airdata/daily_44201_2020.zip", "temp.zip")
con = unzip("temp.zip")
ozone_2020 = read.table("daily_44201_2020.csv", sep = ",", header = TRUE)
unlink("daily_44201_2020.csv")
ozone_2020 = ozone_2020[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_44201_2019.zip", "temp.zip")
con = unzip("temp.zip")
ozone_2019 = read.table("daily_44201_2019.csv", sep = ",", header = TRUE)
unlink("daily_44201_2019.csv")
ozone_2019 = ozone_2019[ap_vars]

ozone_19_20 = rbind(ozone_2019, ozone_2020)
summary(ozone_19_20)
rm(ozone_2019, ozone_2020)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_44201_2015.zip", "temp.zip")
con = unzip("temp.zip")
ozone_2015 = read.table("daily_44201_2015.csv", sep = ",", header = TRUE)
unlink("daily_44201_2015.csv")
ozone_2015 = ozone_2015[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_44201_2016.zip", "temp.zip")
con = unzip("temp.zip")
ozone_2016 = read.table("daily_44201_2016.csv", sep = ",", header = TRUE)
unlink("daily_44201_2016.csv")
ozone_2016 = ozone_2016[ap_vars]

ozone_15_16 = rbind(ozone_2015, ozone_2016)
summary(ozone_15_16)
rm(ozone_2015, ozone_2016)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_44201_2017.zip", "temp.zip")
con = unzip("temp.zip")
ozone_2017 = read.table("daily_44201_2017.csv", sep = ",", header = TRUE)
unlink("daily_44201_2017.csv")
ozone_2017 = ozone_2017[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_44201_2018.zip", "temp.zip")
con = unzip("temp.zip")
ozone_2018 = read.table("daily_44201_2018.csv", sep = ",", header = TRUE)
unlink("daily_44201_2018.csv")
ozone_2018 = ozone_2018[ap_vars]

ozone_17_18 = rbind(ozone_2017, ozone_2018)
summary(ozone_17_18)
rm(ozone_2017, ozone_2018)

ozone_15_18 = rbind(ozone_15_16, ozone_17_18)
rm(ozone_15_16, ozone_17_18)

names(ozone_15_18)[names(ozone_15_18) == "Arithmetic.Mean"] = "ozone"
names(ozone_15_18)[names(ozone_15_18) == "X1st.Max.Value"] = "ozone_max_value"

ap_vars2 = c("State.Name", "County.Name", "City.Name", "Date.Local", "ozone",
             "AQI", "ozone_max_value")
ozone_19_20 = ozone_19_20[ap_vars2]

ozone_15_20 = rbind(ozone_15_18, ozone_19_20)
rm(ozone_15_18, ozone_19_20)


## SO2 
download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42401_2020.zip", "temp.zip")
con = unzip("temp.zip")
so2_2020 = read.table("daily_42401_2020.csv", sep = ",", header = TRUE)
unlink("daily_42401_2020.csv")
so2_2020 = so2_2020[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42401_2019.zip", "temp.zip")
con = unzip("temp.zip")
so2_2019 = read.table("daily_42401_2019.csv", sep = ",", header = TRUE)
unlink("daily_42401_2019.csv")
so2_2019 = so2_2019[ap_vars]

so2_19_20 = rbind(so2_2019, so2_2020)
summary(so2_19_20)
rm(so2_2019, so2_2020)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42401_2015.zip", "temp.zip")
con = unzip("temp.zip")
so2_2015 = read.table("daily_42401_2015.csv", sep = ",", header = TRUE)
unlink("daily_42401_2015.csv")
so2_2015 = so2_2015[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42401_2016.zip", "temp.zip")
con = unzip("temp.zip")
so2_2016 = read.table("daily_42401_2016.csv", sep = ",", header = TRUE)
unlink("daily_42401_2016.csv")
so2_2016 = so2_2016[ap_vars]

so2_15_16 = rbind(so2_2015, so2_2016)
rm(so2_2015, so2_2016)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42401_2017.zip", "temp.zip")
con = unzip("temp.zip")
so2_2017 = read.table("daily_42401_2017.csv", sep = ",", header = TRUE)
unlink("daily_42401_2017.csv")
so2_2017 = so2_2017[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42401_2018.zip", "temp.zip")
con = unzip("temp.zip")
so2_2018 = read.table("daily_42401_2018.csv", sep = ",", header = TRUE)
unlink("daily_42401_2018.csv")
so2_2018 = so2_2018[ap_vars]

so2_17_18 = rbind(so2_2017, so2_2018)
rm(so2_2017, so2_2018)

so2_15_18 = rbind(so2_15_16, so2_17_18)
rm(so2_15_16, so2_17_18)

names(so2_15_18)[names(so2_15_18) == "Arithmetic.Mean"] = "so2"
names(so2_15_18)[names(so2_15_18) == "X1st.Max.Value"] = "so2_max_value"

ap_vars2 = c("State.Name", "County.Name", "City.Name", "Date.Local", "so2",
              "AQI", "so2_max_value")
so2_19_20 = so2_19_20[ap_vars2]

so2_15_20 = rbind(so2_15_18, so2_19_20)
rm(so2_15_18, so2_19_20)


## CO 
download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42101_2020.zip", "temp.zip")
con = unzip("temp.zip")
co_2020 = read.table("daily_42101_2020.csv", sep = ",", header = TRUE)
unlink("daily_42101_2020.csv")
co_2020 = co_2020[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42101_2019.zip", "temp.zip")
con = unzip("temp.zip")
co_2019 = read.table("daily_42101_2019.csv", sep = ",", header = TRUE)
unlink("daily_42101_2019.csv")
co_2019 = co_2019[ap_vars]

co_19_20 = rbind(co_2019, co_2020)
summary(co_19_20)
rm(co_2019, co_2020)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42101_2015.zip", "temp.zip")
con = unzip("temp.zip")
co_2015 = read.table("daily_42101_2015.csv", sep = ",", header = TRUE)
unlink("daily_42101_2015.csv")
co_2015 = co_2015[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42101_2016.zip", "temp.zip")
con = unzip("temp.zip")
co_2016 = read.table("daily_42101_2016.csv", sep = ",", header = TRUE)
unlink("daily_42101_2016.csv")
co_2016 = co_2016[ap_vars]

co_15_16 = rbind(co_2015, co_2016)
rm(co_2015, co_2016)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42101_2017.zip", "temp.zip")
con = unzip("temp.zip")
co_2017 = read.table("daily_42101_2017.csv", sep = ",", header = TRUE)
unlink("daily_42101_2017.csv")
co_2017 = co_2017[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42101_2018.zip", "temp.zip")
con = unzip("temp.zip")
co_2018 = read.table("daily_42101_2018.csv", sep = ",", header = TRUE)
unlink("daily_42101_2018.csv")
co_2018 = co_2018[ap_vars]

co_17_18 = rbind(co_2017, co_2018)
rm(co_2017, co_2018)

co_15_18 = rbind(co_15_16, co_17_18)
rm(co_15_16, co_17_18)

names(co_15_18)[names(co_15_18) == "Arithmetic.Mean"] = "co"
names(co_15_18)[names(co_15_18) == "X1st.Max.Value"] = "co_max_value"

ap_vars2 = c("State.Name", "County.Name", "City.Name", "Date.Local", "co",
              "AQI", "co_max_value")
co_19_20 = co_19_20[ap_vars2]

co_15_20 = rbind(co_15_18, co_19_20)
rm(co_15_18, co_19_20)



## NO2 
download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42602_2020.zip", "temp.zip")
con = unzip("temp.zip")
no2_2020 = read.table("daily_42602_2020.csv", sep = ",", header = TRUE)
unlink("daily_42602_2020.csv")
no2_2020 = no2_2020[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42602_2019.zip", "temp.zip")
con = unzip("temp.zip")
no2_2019 = read.table("daily_42602_2019.csv", sep = ",", header = TRUE)
unlink("daily_42602_2019.csv")
no2_2019 = no2_2019[ap_vars]

no2_19_20 = rbind(no2_2019, no2_2020)
rm(no2_2019, no2_2020)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42602_2015.zip", "temp.zip")
con = unzip("temp.zip")
no2_2015 = read.table("daily_42602_2015.csv", sep = ",", header = TRUE)
unlink("daily_42602_2015.csv")
no2_2015 = no2_2015[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42602_2016.zip", "temp.zip")
con = unzip("temp.zip")
no2_2016 = read.table("daily_42602_2016.csv", sep = ",", header = TRUE)
unlink("daily_42602_2016.csv")
no2_2016 = no2_2016[ap_vars]

no2_15_16 = rbind(no2_2015, no2_2016)
rm(no2_2015, no2_2016)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42602_2017.zip", "temp.zip")
con = unzip("temp.zip")
no2_2017 = read.table("daily_42602_2017.csv", sep = ",", header = TRUE)
unlink("daily_42602_2017.csv")
no2_2017 = no2_2017[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_42602_2018.zip", "temp.zip")
con = unzip("temp.zip")
no2_2018 = read.table("daily_42602_2018.csv", sep = ",", header = TRUE)
unlink("daily_42602_2018.csv")
no2_2018 = no2_2018[ap_vars]

no2_17_18 = rbind(no2_2017, no2_2018)
rm(no2_2017, no2_2018)

no2_15_18 = rbind(no2_15_16, no2_17_18)
rm(no2_15_16, no2_17_18)

names(no2_15_18)[names(no2_15_18) == "Arithmetic.Mean"] = "no2"
names(no2_15_18)[names(no2_15_18) == "X1st.Max.Value"] = "no2_max_value"

ap_vars2 = c("State.Name", "County.Name", "City.Name", "Date.Local", "no2",
              "AQI", "no2_max_value")
no2_19_20 = no2_19_20[ap_vars2]

no2_15_20 = rbind(no2_15_18, no2_19_20)
rm(no2_15_18, no2_19_20)


## PM2.5 
download.file("https://aqs.epa.gov/aqsweb/airdata/daily_88101_2020.zip", "temp.zip")
con = unzip("temp.zip")
pm25_2020 = read.table("daily_88101_2020.csv", sep = ",", header = TRUE)
unlink("daily_88101_2020.csv")
pm25_2020 = pm25_2020[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_88101_2019.zip", "temp.zip")
con = unzip("temp.zip")
pm25_2019 = read.table("daily_88101_2019.csv", sep = ",", header = TRUE)
unlink("daily_88101_2019.csv")
pm25_2019 = pm25_2019[ap_vars]

pm25_19_20 = rbind(pm25_2019, pm25_2020)
rm(pm25_2019, pm25_2020)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_88101_2015.zip", "temp.zip")
con = unzip("temp.zip")
pm25_2015 = read.table("daily_88101_2015.csv", sep = ",", header = TRUE)
unlink("daily_88101_2015.csv")
pm25_2015 = pm25_2015[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_88101_2016.zip", "temp.zip")
con = unzip("temp.zip")
pm25_2016 = read.table("daily_88101_2016.csv", sep = ",", header = TRUE)
unlink("daily_88101_2016.csv")
pm25_2016 = pm25_2016[ap_vars]

pm25_15_16 = rbind(pm25_2015, pm25_2016)
rm(pm25_2015, pm25_2016)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_88101_2017.zip", "temp.zip")
con = unzip("temp.zip")
pm25_2017 = read.table("daily_88101_2017.csv", sep = ",", header = TRUE)
unlink("daily_88101_2017.csv")
pm25_2017 = pm25_2017[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_88101_2018.zip", "temp.zip")
con = unzip("temp.zip")
pm25_2018 = read.table("daily_88101_2018.csv", sep = ",", header = TRUE)
unlink("daily_88101_2018.csv")
pm25_2018 = pm25_2018[ap_vars]

pm25_17_18 = rbind(pm25_2017, pm25_2018)
rm(pm25_2017, pm25_2018)

pm25_15_18 = rbind(pm25_15_16, pm25_17_18)
rm(pm25_15_16, pm25_17_18)

pm25_15_20 = rbind(pm25_15_18, pm25_19_20)
rm(pm25_15_18, pm25_19_20)

names(pm25_15_20)[names(pm25_15_20) == "Arithmetic.Mean"] = "pm25"
names(pm25_15_20)[names(pm25_15_20) == "X1st.Max.Value"] = "pm25_max_value"

ap_vars2 = c("State.Name", "County.Name", "City.Name", "Date.Local", "pm25",
              "AQI", "pm25_max_value")
pm25_15_20 = pm25_15_20[ap_vars2]


## PM10
download.file("https://aqs.epa.gov/aqsweb/airdata/daily_81102_2020.zip", "temp.zip")
con = unzip("temp.zip")
pm10_2020 = read.table("daily_81102_2020.csv", sep = ",", header = TRUE)
unlink("daily_81102_2020.csv")
pm10_2020 = pm10_2020[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_81102_2019.zip", "temp.zip")
con = unzip("temp.zip")
pm10_2019 = read.table("daily_81102_2019.csv", sep = ",", header = TRUE)
unlink("daily_81102_2019.csv")
pm10_2019 = pm10_2019[ap_vars]

pm10_19_20 = rbind(pm10_2019, pm10_2020)
rm(pm10_2019, pm10_2020)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_81102_2015.zip", "temp.zip")
con = unzip("temp.zip")
pm10_2015 = read.table("daily_81102_2015.csv", sep = ",", header = TRUE)
unlink("daily_81102_2015.csv")
pm10_2015 = pm10_2015[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_81102_2016.zip", "temp.zip")
con = unzip("temp.zip")
pm10_2016 = read.table("daily_81102_2016.csv", sep = ",", header = TRUE)
unlink("daily_81102_2016.csv")
pm10_2016 = pm10_2016[ap_vars]

pm10_15_16 = rbind(pm10_2015, pm10_2016)
rm(pm10_2015, pm10_2016)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_81102_2017.zip", "temp.zip")
con = unzip("temp.zip")
pm10_2017 = read.table("daily_81102_2017.csv", sep = ",", header = TRUE)
unlink("daily_81102_2017.csv")
pm10_2017 = pm10_2017[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_81102_2018.zip", "temp.zip")
con = unzip("temp.zip")
pm10_2018 = read.table("daily_81102_2018.csv", sep = ",", header = TRUE)
unlink("daily_81102_2018.csv")
pm10_2018 = pm10_2018[ap_vars]

pm10_17_18 = rbind(pm10_2017, pm10_2018)
rm(pm10_2017, pm10_2018)

pm10_15_18 = rbind(pm10_15_16, pm10_17_18)
rm(pm10_15_16, pm10_17_18)

pm10_15_20 = rbind(pm10_15_18, pm10_19_20)
rm(pm10_15_18, pm10_19_20)

names(pm10_15_20)[names(pm10_15_20) == "Arithmetic.Mean"] = "pm10"
names(pm10_15_20)[names(pm10_15_20) == "X1st.Max.Value"] = "pm10_max_value"

ap_vars2 = c("State.Name", "County.Name", "City.Name", "Date.Local", "pm10",
              "AQI", "pm10_max_value")
pm10_15_20 = pm10_15_20[ap_vars2]


## Speciated PM2.5
ap_vars2 = c("State.Name", "County.Name", "City.Name", "Date.Local", "Parameter.Name", 
              "Arithmetic.Mean", "AQI", "X1st.Max.Value")

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_SPEC_2020.zip", "temp.zip")
con = unzip("temp.zip")
spec_pm25_2020 = read.table("daily_SPEC_2020.csv", sep = ",", header = TRUE)
unlink("daily_SPEC_2020.csv")
spec_pm25_2020 = spec_pm25_2020[ap_vars2]

ls(spec_pm25_2020)
download.file("https://aqs.epa.gov/aqsweb/airdata/daily_SPEC_2019.zip", "temp.zip")
con = unzip("temp.zip")
spec_pm25_2019 = read.table("daily_SPEC_2019.csv", sep = ",", header = TRUE)
unlink("daily_SPEC_2019.csv")
spec_pm25_2019 = spec_pm25_2019[ap_vars2]


## Temperature
download.file("https://aqs.epa.gov/aqsweb/airdata/daily_TEMP_2020.zip", "temp.zip")
con = unzip("temp.zip")
TEMP_2020 = read.table("daily_TEMP_2020.csv", sep = ",", header = TRUE)
unlink("daily_TEMP_2020.csv")
TEMP_2020 = TEMP_2020[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_TEMP_2019.zip", "temp.zip")
con = unzip("temp.zip")
TEMP_2019 = read.table("daily_TEMP_2019.csv", sep = ",", header = TRUE)
unlink("daily_TEMP_2019.csv")
TEMP_2019 = TEMP_2019[ap_vars]

temp_19_20 = rbind(TEMP_2019, TEMP_2020)
rm(TEMP_2019, TEMP_2020)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_TEMP_2015.zip", "temp.zip")
con = unzip("temp.zip")
TEMP_2015 = read.table("daily_TEMP_2015.csv", sep = ",", header = TRUE)
unlink("daily_TEMP_2015.csv")
TEMP_2015 = TEMP_2015[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_TEMP_2016.zip", "temp.zip")
con = unzip("temp.zip")
TEMP_2016 = read.table("daily_TEMP_2016.csv", sep = ",", header = TRUE)
unlink("daily_TEMP_2016.csv")
TEMP_2016 = TEMP_2016[ap_vars]

TEMP_15_16 = rbind(TEMP_2015, TEMP_2016)
rm(TEMP_2015, TEMP_2016)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_TEMP_2017.zip", "temp.zip")
con = unzip("temp.zip")
TEMP_2017 = read.table("daily_TEMP_2017.csv", sep = ",", header = TRUE)
unlink("daily_TEMP_2017.csv")
TEMP_2017 = TEMP_2017[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_TEMP_2018.zip", "temp.zip")
con = unzip("temp.zip")
TEMP_2018 = read.table("daily_TEMP_2018.csv", sep = ",", header = TRUE)
unlink("daily_TEMP_2018.csv")
TEMP_2018 = TEMP_2018[ap_vars]

TEMP_17_18 = rbind(TEMP_2017, TEMP_2018)
rm(TEMP_2017, TEMP_2018)

TEMP_15_18 = rbind(TEMP_15_16, TEMP_17_18)
rm(TEMP_15_16, TEMP_17_18)

names(TEMP_15_18)[names(TEMP_15_18) == "TEMP"] = "tempurature"
names(TEMP_15_18)[names(TEMP_15_18) == "TEMP_max_value"] = "tempurature_max_value"

ap_vars2 = c("State.Name", "County.Name", "City.Name", "Date.Local", "tempurature",
              "AQI", "tempurature_max_value")
temp_19_20 = temp_19_20[ap_vars2]

temp_15_20 = rbind(TEMP_15_18, temp_19_20)
rm(TEMP_15_18, temp_19_20)

## Relative Humidity 
download.file("https://aqs.epa.gov/aqsweb/airdata/daily_RH_DP_2020.zip", "RH_DP.zip")
con = unzip("RH_DP.zip")
RH_DP_2020 = read.table("daily_RH_DP_2020.csv", sep = ",", header = TRUE)
unlink("daily_RH_DP_2020.csv")
RH_DP_2020 = RH_DP_2020[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_RH_DP_2019.zip", "RH_DP.zip")
con = unzip("RH_DP.zip")
RH_DP_2019 = read.table("daily_RH_DP_2019.csv", sep = ",", header = TRUE)
unlink("daily_RH_DP_2019.csv")
RH_DP_2019 = RH_DP_2019[ap_vars]

rh_19_20 = rbind(RH_DP_2019, RH_DP_2020)
summary(rh_19_20)
rm(RH_DP_2019, RH_DP_2020)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_RH_DP_2015.zip", "temp.zip")
con = unzip("temp.zip")
rh_dp_2015 = read.table("daily_RH_DP_2015.csv", sep = ",", header = TRUE)
unlink("daily_RH_DP_2015.csv")
rh_dp_2015 = rh_dp_2015[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_RH_DP_2016.zip", "temp.zip")
con = unzip("temp.zip")
rh_dp_2016 = read.table("daily_RH_DP_2016.csv", sep = ",", header = TRUE)
unlink("daily_RH_DP_2016.csv")
rh_dp_2016 = rh_dp_2016[ap_vars]

rh_dp_15_16 = rbind(rh_dp_2015, rh_dp_2016)
rm(rh_dp_2015, rh_dp_2016)

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_RH_DP_2017.zip", "temp.zip")
con = unzip("temp.zip")
rh_dp_2017 = read.table("daily_RH_DP_2017.csv", sep = ",", header = TRUE)
unlink("daily_RH_DP_2017.csv")
rh_dp_2017 = rh_dp_2017[ap_vars]

download.file("https://aqs.epa.gov/aqsweb/airdata/daily_RH_DP_2018.zip", "temp.zip")
con = unzip("temp.zip")
rh_dp_2018 = read.table("daily_RH_DP_2018.csv", sep = ",", header = TRUE)
unlink("daily_RH_DP_2018.csv")
rh_dp_2018 = rh_dp_2018[ap_vars]

rh_dp_17_18 = rbind(rh_dp_2017, rh_dp_2018)
rm(rh_dp_2017, rh_dp_2018)

rh_dp_15_18 = rbind(rh_dp_15_16, rh_dp_17_18)
rm(rh_dp_15_16, rh_dp_17_18)

names(rh_dp_15_18)[names(rh_dp_15_18) == "Arithmetic.Mean"] = "rel_humid"
names(rh_dp_15_18)[names(rh_dp_15_18) == "X1st.Max.Value"] = "rel_humid_max_value"

ap_vars2 = c("State.Name", "County.Name", "City.Name", "Date.Local", "rel_humid",
              "AQI", "rel_humid_max_value")
rh_19_20 = rh_19_20[ap_vars2]

rh_15_20 = rbind(rh_dp_15_18, rh_19_20)
rm(rh_dp_15_18, rh_dp_19_20)


## Rename variable "Arithmetic.Mean" to AP constituent within each DF
names(no2_19_20)[names(no2_19_20) == "Arithmetic.Mean"] = "no2"
names(so2_19_20)[names(so2_19_20) == "Arithmetic.Mean"] = "so2"
names(co_19_20)[names(co_19_20) == "Arithmetic.Mean"] = "co2"
names(ozone_19_20)[names(ozone_19_20) == "Arithmetic.Mean"] = "ozone"
names(pm10_19_20)[names(pm10_19_20) == "Arithmetic.Mean"] = "pm10"
names(pm25_19_20)[names(pm25_19_20) == "Arithmetic.Mean"] = "pm25"
names(temp_19_20)[names(temp_19_20) == "Arithmetic.Mean"] = "tempurature"
names(rh_19_20)[names(rh_19_20) == "Arithmetic.Mean"] = "rel_humid"

## Rename variable "X1st.Max.Value" to AP constituent within each DF
names(no2_19_20)[names(no2_19_20) == "X1st.Max.Value"] = "no2_max_value"
names(so2_19_20)[names(so2_19_20) == "X1st.Max.Value"] = "so2_max_value"
names(co_19_20)[names(co_19_20) == "X1st.Max.Value"] = "co2_max_value"
names(ozone_19_20)[names(ozone_19_20) == "X1st.Max.Value"] = "ozone_max_value"
names(pm10_19_20)[names(pm10_19_20) == "X1st.Max.Value"] = "pm10_max_value"
names(pm25_19_20)[names(pm25_19_20) == "X1st.Max.Value"] = "pm25_max_value"
names(temp_19_20)[names(temp_19_20) == "X1st.Max.Value"] = "tempurature_max_value"
names(rh_19_20)[names(rh_19_20) == "X1st.Max.Value"] = "rel_humid_max_value"



## deduplicate and exlcude any non-US states
library(tidyverse)
library(zoo)
ozone_15_20 = ozone_15_20 %>% distinct()   #  (de-duplicated)
ozone_15_20 = ozone_15_20[!(ozone_15_20$State.Name == "Puerto Rico" | 
                         ozone_15_20$State.Name == "Canada" | ozone_15_20$State.Name == 
                         "Country Of Mexico" | ozone_15_20$State.Name == "Virgin Islands"),
                     ] # to delete obs if State = Puerto Rico, Canada, Mexico, Virgin islands            
ozone_15_20 = ozone_15_20 %>% # arrange by State, County, City, then date
  arrange(State.Name, County.Name, City.Name, Date.Local)

pm25_15_20 = pm25_15_20 %>% distinct() 
pm25_15_20 = pm25_15_20[!(pm25_15_20$State.Name == "Puerto Rico" | 
                             pm25_15_20$State.Name == "Canada" | pm25_15_20$State.Name == 
                             "Country Of Mexico" | pm25_15_20$State.Name == "Virgin Islands"),
                         ] # to delete obs if State = Puerto Rico, Canada, Mexico, Virgin islands            
pm25_15_20 = pm25_15_20 %>% # arrange by State, County, City, then date
  arrange(State.Name, County.Name, City.Name, Date.Local)

so2_15_20 = so2_15_20 %>% distinct() 
so2_15_20 = so2_15_20[!(so2_15_20$State.Name == "Puerto Rico" | 
                           so2_15_20$State.Name == "Canada" | so2_15_20$State.Name == 
                           "Country Of Mexico" | so2_15_20$State.Name == "Virgin Islands"),
                       ] # to delete obs if State = Puerto Rico, Canada, Mexico, Virgin islands            
so2_15_20 = so2_15_20 %>% # arrange by State, County, City, then date
  arrange(State.Name, County.Name, City.Name, Date.Local)

no2_15_20 = no2_15_20 %>% distinct() 
no2_15_20 = no2_15_20[!(no2_15_20$State.Name == "Puerto Rico" | 
                           no2_15_20$State.Name == "Canada" | no2_15_20$State.Name == 
                           "Country Of Mexico" | no2_15_20$State.Name == "Virgin Islands"),
                       ] # to delete obs if State = Puerto Rico, Canada, Mexico, Virgin islands            
no2_15_20 = no2_15_20 %>% # arrange by State, County, City, then date
  arrange(State.Name, County.Name, City.Name, Date.Local)

co_15_20 = co_15_20 %>% distinct() 
co_15_20 = co_15_20[!(co_15_20$State.Name == "Puerto Rico" | 
                         co_15_20$State.Name == "Canada" | co_15_20$State.Name == 
                         "Country Of Mexico" | co_15_20$State.Name == "Virgin Islands"),
                     ] # to delete obs if State = Puerto Rico, Canada, Mexico, Virgin islands            
# 1694980 obs for 5 vars
co_15_20 = co_15_20 %>% # arrange by State, County, City, then date
  arrange(State.Name, County.Name, City.Name, Date.Local)

pm10_15_20 = pm10_15_20 %>% distinct() 
pm10_15_20 = pm10_15_20[!(pm10_15_20$State.Name == "Puerto Rico" | 
                           pm10_15_20$State.Name == "Canada" | pm10_15_20$State.Name == 
                           "Country Of Mexico" | pm10_15_20$State.Name == "Virgin Islands"),
                       ] # to delete obs if State = Puerto Rico, Canada, Mexico, Virgin islands            
pm10_15_20 = pm10_15_20 %>% # arrange by State, County, City, then date
  arrange(State.Name, County.Name, City.Name, Date.Local)

temp_15_20 = temp_15_20 %>% distinct() 
temp_15_20 = temp_15_20[!(temp_15_20$State.Name == "Puerto Rico" | 
                           temp_15_20$State.Name == "Canada" | temp_15_20$State.Name == 
                           "Country Of Mexico" | temp_15_20$State.Name == "Virgin Islands"),
                       ] # to delete obs if State = Puerto Rico, Canada, Mexico, Virgin islands            
temp_15_20 = temp_15_20 %>% # arrange by State, County, City, then date
  arrange(State.Name, County.Name, City.Name, Date.Local)

rh_15_20 = rh_15_20 %>% distinct() 
rh_15_20 = rh_15_20[!(rh_15_20$State.Name == "Puerto Rico" | 
                           rh_15_20$State.Name == "Canada" | rh_15_20$State.Name == 
                           "Country Of Mexico" | rh_15_20$State.Name == "Virgin Islands"),
                       ] # to delete obs if State = Puerto Rico, Canada, Mexico, Virgin islands            
rh_15_20 = rh_15_20 %>% # arrange by State, County, City, then date
  arrange(State.Name, County.Name, City.Name, Date.Local)




#################################################################################################
# Average days with mulitple measurements or multiple monitors per county
#################################################################################################
colnames(rh_15_20_mean)
vars = c("State.Name",  "County.Name",  "Date.Local",  "ozone" )
ozone_15_20_mean = ozone_15_20_mean[vars]
vars = c("State.Name",  "County.Name",  "Date.Local",  "pm25")
pm25_15_20_mean = pm25_15_20_mean[vars]
vars = c("State.Name",  "County.Name",  "Date.Local",  "so2"  )
so2_15_20_mean = so2_15_20_mean[vars]
vars = c("State.Name",  "County.Name",  "Date.Local",  "pm10" )
pm10_15_20_mean = pm10_15_20_mean[vars]
vars = c("State.Name",  "County.Name", "Date.Local",  "no2"  )
no2_15_20_mean = no2_15_20_mean[vars]
vars = c("State.Name",  "County.Name", "Date.Local",  "tempurature")
temp_15_20_mean = temp_15_20_mean[vars]
vars = c("State.Name" , "County.Name", "Date.Local" , "rel_humid")
rh_15_20_mean = rh_15_20_mean[vars]

# create id by combining state, coutny, city, date
ozone_15_20$ID = cumsum(!duplicated(ozone_15_20[1:4]))
pm25_15_20$ID = cumsum(!duplicated(pm25_15_20[1:4]))
so2_15_20$ID = cumsum(!duplicated(so2_15_20[1:4]))
no2_15_20$ID = cumsum(!duplicated(no2_15_20[1:4]))
pm10_15_20$ID = cumsum(!duplicated(pm10_15_20[1:4]))
temp_15_20$ID = cumsum(!duplicated(temp_15_20[1:4]))
rh_15_20$ID = cumsum(!duplicated(rh_15_20[1:4]))

# take the mean of two same IDs
no2_15_20_mean = aggregate(no2 ~ ID + State.Name + County.Name + City.Name + Date.Local,
                            FUN = mean, data=no2_15_20)
no2_15_20_mean$ID = NULL

so2_15_20_mean = aggregate(so2 ~ ID + State.Name + County.Name + City.Name + Date.Local,
                            FUN = mean, data=so2_15_20)
so2_15_20_mean$ID = NULL

pm25_15_20_mean = aggregate(pm25 ~ ID + State.Name + County.Name + City.Name + Date.Local,
                             FUN = mean, data=pm25_15_20)
pm25_15_20_mean$ID = NULL

pm10_15_20_mean = aggregate(pm10 ~ ID + State.Name + County.Name + City.Name + Date.Local,
                             FUN = mean, data=pm10_15_20)
pm10_15_20_mean$ID = NULL

ozone_15_20_mean = aggregate(ozone ~ ID + State.Name + County.Name + City.Name + Date.Local,
                              FUN = mean, data=ozone_15_20)
ozone_15_20_mean$ID = NULL

temp_15_20_mean = aggregate(tempurature ~ ID + State.Name + County.Name + City.Name + Date.Local,
                              FUN = mean, data=temp_15_20)
temp_15_20_mean$ID = NULL

rh_15_20_mean = aggregate(rel_humid ~ ID + State.Name + County.Name + City.Name + Date.Local,
                              FUN = mean, data=rh_15_20)
rh_15_20_mean$ID = NULL


#################################################################################################
###    Merge Air pollution dataframes:  NO2, CO, SO2, PM2.5, PM10, O3, temp and rel humid
#################################################################################################
temp_pm25 = merge(temp_15_20_mean, pm25_15_20_mean)
rm(temp_15_20, pm25_15_20)
temp_ozone = merge(temp_pm25, ozone_15_20_mean)
rm(temp_pm25, ozone_15_20)
temp_so2 = merge(temp_ozone, so2_15_20_mean)
rm(temp_ozone, so2_15_20)
temp_rel = merge(temp_so2, rh_15_20_mean)
rm(temp_so2, rh_15_20)
temp_no2 = merge(temp_rel, no2_15_20_mean)
rm(temp_rel, no2_15_20)
ap_temp_rh = merge(temp_no2, pm10_15_20_mean)
rm(temp_no2, pm10_15_20)

## second AP data frame without temp & rh (for checking data afterwards)
ozone_pm25 = merge(ozone_15_20_mean, pm25_15_20_mean)
ozone_so2 = merge(ozone_pm25, so2_15_20_mean)
rm(ozone_pm25)
ozone_no2 = merge(ozone_so2, no2_15_20_mean)
rm(ozone_so2)
ap_tot = merge(ozone_no2, pm10_15_20_mean)
rm(ozone_no2)

list(unique(ap_tot$County.Name))
#################################################################################################
###    5-year average for each ap variable 
#################################################################################################
library(dplyr)
so2_15_20_mean = so2_15_20_mean %>% 
  mutate(ID = group_indices(., State.Name, County.Name)) 
no2_15_20_mean = no2_15_20_mean %>% 
  mutate(ID = group_indices(., State.Name, County.Name)) 
ozone_15_20_mean = ozone_15_20_mean %>% 
  mutate(ID = group_indices(., State.Name, County.Name)) 
pm25_15_20_mean = pm25_15_20_mean %>% 
  mutate(ID = group_indices(., State.Name, County.Name)) 
pm10_15_20_mean = pm10_15_20_mean %>% 
  mutate(ID = group_indices(., State.Name, County.Name))  
temp_15_20_mean = temp_15_20_mean %>% 
  mutate(ID = group_indices(., State.Name, County.Name)) 
rh_15_20_mean = rh_15_20_mean %>% 
  mutate(ID = group_indices(., State.Name, County.Name)) 


no2_5yr_mean = aggregate(no2 ~ ID, FUN = mean, data=no2_15_20_mean)
so2_5yr_mean = aggregate(so2 ~ ID, FUN = mean, data=so2_15_20_mean)
pm25_5yr_mean = aggregate(pm25 ~ ID, FUN = mean, data=pm25_15_20_mean)
pm10_5yr_mean = aggregate(pm10 ~ ID, FUN = mean, data=pm10_15_20_mean)
ozone_5yr_mean = aggregate(ozone ~ ID, FUN = mean, data=ozone_15_20_mean)
temp_5yr_mean = aggregate(tempurature ~ ID, FUN = mean, data=temp_15_20_mean)
rh_5yr_mean = aggregate(rel_humid ~ ID, FUN = mean, data=rh_15_20_mean)


library(tidyverse)
vars = c("State.Name",  "County.Name", "ID")
no2_mean = no2_15_20_mean[vars]
no2_mean = unique(no2_mean)
no2_5yr_mean = merge(no2_mean, no2_5yr_mean)
rm(no2_mean)

so2_mean = so2_15_20_mean[vars]
so2_mean = unique(so2_mean)
so2_5yr_mean = merge(so2_mean, so2_5yr_mean)
rm(so2_mean)

pm25_mean = pm25_15_20_mean[vars]
pm25_mean = unique(pm25_mean)
pm25_5yr_mean = merge(pm25_mean, pm25_5yr_mean)
rm(pm25_mean)

pm10_mean = pm10_15_20_mean[vars]
pm10_mean = unique(pm10_mean)
pm10_5yr_mean = merge(pm10_mean, pm10_5yr_mean)
rm(pm10_mean)

ozone_mean = ozone_15_20_mean[vars]
ozone_mean = unique(ozone_mean)
ozone_5yr_mean = merge(ozone_mean, ozone_5yr_mean)
rm(ozone_mean)

temp_mean = temp_15_20_mean[vars]
temp_mean = unique(temp_mean)
temp_5yr_mean = merge(temp_mean, temp_5yr_mean)
rm(temp_mean)

rh_mean = rh_15_20_mean[vars]
rh_mean = unique(rh_mean)
rh_5yr_mean = merge(rh_mean, rh_5yr_mean)
rm(rh_mean)



#################################################################################################
###    Merge Air pollution dataframes:  NO2, CO, SO2, PM2.5, PM10, O3
#################################################################################################
vars = c("State.Name", "County.Name", "pm25" )
pm25_5yr_mean = pm25_5yr_mean[vars]
vars = c("State.Name", "County.Name", "pm10" )
pm10_5yr_mean = pm10_5yr_mean[vars]
vars = c("State.Name", "County.Name", "no2" )
no2_5yr_mean = no2_5yr_mean[vars]
vars = c("State.Name", "County.Name", "so2" )
so2_5yr_mean = so2_5yr_mean[vars]
vars = c("State.Name", "County.Name", "ozone" )
ozone_5yr_mean = ozone_5yr_mean[vars]
vars = c("State.Name", "County.Name", "tempurature" )
temp_5yr_mean = temp_5yr_mean[vars]
vars = c("State.Name", "County.Name", "rel_humid" )
rh_5yr_mean = rh_5yr_mean[vars]


temp_pm25 = merge(temp_5yr_mean, pm25_5yr_mean)
temp_ozone = merge(temp_pm25, ozone_5yr_mean)
rm(temp_pm25)
temp_so2 = merge(temp_ozone, so2_5yr_mean)
rm(temp_ozone)
temp_rel = merge(temp_so2, rh_5yr_mean)
rm(temp_so2)
temp_no2 = merge(temp_rel, no2_5yr_mean)
rm(temp_rel)
ap_5yr_mean = merge(temp_no2, pm10_5yr_mean)
rm(temp_no2)

## second AP data frame without temp & rh (for checking data afterwards)
ozone_pm25 = merge(ozone_5yr_mean, pm25_5yr_mean)
ozone_so2 = merge(ozone_pm25, so2_5yr_mean)
rm(ozone_pm25)
ozone_no2 = merge(ozone_so2, no2_5yr_mean)
rm(ozone_so2)
ap_5yr_tot_mean = merge(ozone_no2, pm10_5yr_mean)
rm(ozone_no2)


### aggregate all New York City boroughs into one New York County
ap_5yr_nyc = ap_5yr_tot_mean

ap_5yr_nyc$County.Name[ap_5yr_nyc$County.Name == "Bronx"] = "New York"
ap_5yr_nyc$County.Name[ap_5yr_nyc$County.Name == "Queens"] = "New York"



library(dplyr)
# take the mean of two same IDs
#aggregate(.~id1+id2, df1, mean)

ap_5yr_nyc = aggregate(.~State.Name + County.Name, FUN = mean, data=ap_5yr_nyc)





#################################################################################################
# Diabetes (CDC) dataframe  subsetting, 
#################################################################################################
## subset diabetes data to only 2016
dm_prev_2016 = read_csv('/Users/naomiriches/Desktop/Prevalence_all_states_2016.csv')
colnames(dm_prev_2016)
summary(dm_prev_2016)

names(dm_prev_2016)[names(dm_prev_2016) == "CountyFIPS"] = "FIPS"
names(dm_prev_2016)[names(dm_prev_2016) == "Percentage"] = "dm_prevalence"

vars = c("State", "County", "FIPS" , "dm_prevalence")

dm_prev_2016 = dm_prev_2016[vars]

list(unique(dm_prev_2016_2$County.Name))

##### Aggregate New York City Boroughs into a single New York County with FIPS = 36061
dm_prev_nyc = dm_prev_2016_2

dm_prev_nyc$County.Name[dm_prev_nyc$County.Name == "Bronx"] = "New York"
dm_prev_nyc$County.Name[dm_prev_nyc$County.Name == "Queens"] = "New York"
dm_prev_nyc$County.Name[dm_prev_nyc$County.Name == "Kings"] = "New York"
dm_prev_nyc$County.Name[dm_prev_nyc$County.Name == "Richmond"] = "New York"

dm_prev_nyc$FIPS[dm_prev_nyc$FIPS == 36005] = 36061
dm_prev_nyc$FIPS[dm_prev_nyc$FIPS == 36047] = 36061
dm_prev_nyc$FIPS[dm_prev_nyc$FIPS == 36081] = 36061
dm_prev_nyc$FIPS[dm_prev_nyc$FIPS == 36085] = 36061

library(dplyr)
# take the mean of two same IDs
#aggregate(.~id1+id2, df1, mean)

dm_prev_nyc = aggregate(.~State.Name + County.Name + FIPS, FUN = mean, data=dm_prev_nyc)
summary(dm_prev_nyc)




#################################################################################################
# subset age and gender dataframes
#################################################################################################
ls(merged_age_files_2019)

agevars = c("STNAME", "CTYNAME", "POPESTIMATE", "POPEST_FEM", "POPEST_MALE", "MEDIAN_AGE_TOT", 
             "MEDIAN_AGE_FEM", "MEDIAN_AGE_MALE", "UNDER5_TOT", "UNDER5_FEM", "UNDER5_MALE",  
             "AGE513_TOT",  "AGE513_FEM", "AGE513_MALE", "AGE1417_TOT", "AGE1417_FEM", "AGE1417_MALE",
             "AGE1824_TOT" , "AGE1824_FEM", "AGE1824_MALE", "AGE2544_TOT", "AGE2544_FEM", "AGE2544_MALE",     
             "AGE4564_TOT", "AGE4564_FEM", "AGE4564_MALE", 
             "AGE6569_TOT", "AGE6569_FEM", "AGE6569_MALE", "AGE7074_TOT", "AGE7074_FEM", "AGE7074_MALE", 
             "AGE7579_TOT", "AGE7579_FEM", "AGE7579_MALE", "AGE8084_TOT", "AGE8084_FEM", "AGE8084_MALE", 
             "AGE85PLUS_TOT", "AGE85PLUS_FEM", "AGE85PLUS_MALE")       
             
merged_age_files_2019 = merged_age_files_2019[agevars]             
                                              




#################################################################################################
###                    Merge diabets prevalence with covid cases & deaths
#################################################################################################
colnames(dm_prev_nyc)
colnames(covid_deaths2_long)
colnames(covid_dm_deaths)
summary(covid_cases2_long)

covid_dm_cases = merge(dm_prev_nyc, covid_cases_long, by = c("State.Name", "County.Name", "FIPS"))
covid_dm_deaths = merge(dm_prev_nyc, covid_deaths_long, by = c("State.Name", "County.Name", "FIPS"))

names(covid_deaths2_long)[names(covid_deaths2_long) == "deaths"] = "cum_deaths"
names(covid_cases2_long)[names(covid_cases2_long) == "cases"] = "cum_cases"

covid_cases_deaths = merge(covid_deaths2_long, covid_cases2_long, by = c("State.Name", "County.Name", "FIPS",
                                                                         "Date.Local"))
covid_dm_cases_deaths = merge(covid_cases_deaths, dm_prev_nyc, by = c("State.Name", "County.Name", "FIPS"))

rm(covid_cases_deaths)

vars = c("State.Name", "County.Name", "FIPS", "Date.Local", "deaths", "dm_year", "age_adj_rate_per_1000", 
          "adj_LEI", "dm_diff", "unemployment_2019", "Median Household Income (2018)", 
          "% of State Median HH Income", "POPESTIMATE", "POPEST_FEM", "POPEST_MALE", "MEDIAN_AGE_TOT", 
          "MEDIAN_AGE_FEM", "MEDIAN_AGE_MALE", "UNDER5_TOT", "UNDER5_FEM", "UNDER5_MALE", "AGE513_TOT", 
          "AGE513_FEM", "AGE513_MALE", "AGE1417_TOT", "AGE1417_FEM", "AGE1417_MALE", "AGE1824_TOT", 
          "AGE1824_FEM", "AGE1824_MALE", "AGE2544_TOT", "AGE2544_FEM", "AGE2544_MALE", "AGE4564_TOT",
          "AGE4564_FEM", "AGE4564_MALE", "AGE6569_TOT", "AGE6569_FEM", "AGE6569_MALE", "AGE7074_TOT", 
          "AGE7074_FEM", "AGE7074_MALE", "AGE7579_TOT", "AGE7579_FEM", "AGE7579_MALE", "AGE8084_TOT", 
          "AGE8084_FEM", "AGE8084_MALE", "AGE85PLUS_TOT", "AGE85PLUS_FEM", "AGE85PLUS_MALE", "UID")

covid_dm_ses_age_cases = covid_dm_ses_age_cases[vars]
covid_dm_ses_age_deaths = covid_dm_ses_age_deaths[vars]


##  create case and death rates (per 1000 population)
covid_dm_cases$daily_case_rate = (covid_dm_cases$cases/covid_dm_cases$Population)*1000
covid_dm_deaths$daily_death_rate = (covid_dm_deaths$deaths/covid_dm_deaths$Population)*1000


## create case-fatality rate
covid_dm_cases_deaths$case_fatality = ifelse(covid_dm_cases_deaths$cum_deaths == 0, 0, 
                                              covid_dm_cases_deaths$cum_deaths/covid_dm_cases_deaths$cum_cases)
covid_dm_cases_deaths = subset(covid_dm_cases_deaths, case_fatality != "Inf")
covid_dm_cases_deaths = subset(covid_dm_cases_deaths, case_fatality <= 1)

summary(covid_dm_cases_deaths)
#################################################################################################
####                   Merge covid_dm_cases/deaths/cases_deaths  + AP DF                     ####
#################################################################################################

cluster_cases = merge(covid_dm_cases, ap_5yr_nyc)
cluster_deaths = merge(covid_dm_deaths, ap_5yr_nyc)
cluster_case_fatality = merge(covid_dm_cases_deaths, ap_5yr_nyc)



#####  covid + t2dm + ap correlation matrix
colnames(cluster_cases)
colnames(cluster_deaths)
colnames(cluster_case_fatality)


vars = c("dm_prevalence", "cases", "Population", "daily_case_rate", "ozone",  
          "pm25", "so2",  "no2", "pm10")
vars2 = c("dm_prevalence", "deaths", "Population", "daily_death_rate", "ozone",  
           "pm25", "so2",  "no2", "pm10")
vars3 = c("Population", "cum_deaths", "cum_cases", "dm_prevalence", "case_fatality", 
           "ozone",  "pm25", "so2",  "no2", "pm10")

covid_corr1 = cluster_cases[vars]
covid_corr2 = cluster_deaths[vars2]
covid_corr3 = cluster_case_fatality[vars3]

res = round(cor(covid_corr1), 2)
library(reshape2)
melted_corrmat = melt(res)

library(ggplot2)
ggplot(data = melted_corrmat, aes(x=Var1, y=Var2, fill = value)) +
  geom_tile()

rm(vars, vars2, vars3, covid_corr1, covid_corr2, covid_corr3, res, melted_corrmat)



#################################################################################################
####                   Normalize covid_dm_cases/deaths/cases_deaths  + AP                    ####
#################################################################################################

######  trying Max-Min normalization bc modified z didn't work

covid_cluster_cases = cluster_cases[vars]
covid_cluster_deaths = cluster_deaths[vars2]
covid_cluster_cases_deaths = cluster_case_fatality[vars3]

install.packages("heatmaply")
library(heatmaply)
covid_cluster_cases = normalize(covid_cluster_cases)
covid_cluster_deaths = normalize(covid_cluster_deaths)
covid_cluster_cases_deaths = normalize(covid_cluster_cases_deaths)

# rename variables so I can combine them back into original data frame
names(covid_cluster_cases)[names(covid_cluster_cases) == "dm_prevalence"] = "norm_dm_prev"
names(covid_cluster_cases)[names(covid_cluster_cases) == "Population"] = "norm_pop"
names(covid_cluster_cases)[names(covid_cluster_cases) == "daily_case_rate"] = "norm_case"
names(covid_cluster_cases)[names(covid_cluster_cases) == "ozone"] = "norm_ozone"
names(covid_cluster_cases)[names(covid_cluster_cases) == "pm25"] = "norm_pm25"
names(covid_cluster_cases)[names(covid_cluster_cases) == "so2"] = "norm_so2"
names(covid_cluster_cases)[names(covid_cluster_cases) == "no2"] = "norm_no2"
names(covid_cluster_cases)[names(covid_cluster_cases) == "pm10"] = "norm_pm10"

names(covid_cluster_deaths)[names(covid_cluster_deaths) == "dm_prevalence"] = "norm_dm_prev"
names(covid_cluster_deaths)[names(covid_cluster_deaths) == "Population"] = "norm_pop"
names(covid_cluster_deaths)[names(covid_cluster_deaths) == "daily_death_rate"] = "norm_death"
names(covid_cluster_deaths)[names(covid_cluster_deaths) == "ozone"] = "norm_ozone"
names(covid_cluster_deaths)[names(covid_cluster_deaths) == "pm25"] = "norm_pm25"
names(covid_cluster_deaths)[names(covid_cluster_deaths) == "so2"] = "norm_so2"
names(covid_cluster_deaths)[names(covid_cluster_deaths) == "no2"] = "norm_no2"
names(covid_cluster_deaths)[names(covid_cluster_deaths) == "pm10"] = "norm_pm10"

names(covid_cluster_cases_deaths)[names(covid_cluster_cases_deaths) == "dm_prevalence"] = "norm_dm_prev"
names(covid_cluster_cases_deaths)[names(covid_cluster_cases_deaths) == "Population"] = "norm_pop"
names(covid_cluster_cases_deaths)[names(covid_cluster_cases_deaths) == "case_fatality"] = "norm_case_fatality"
names(covid_cluster_cases_deaths)[names(covid_cluster_cases_deaths) == "ozone"] = "norm_ozone"
names(covid_cluster_cases_deaths)[names(covid_cluster_cases_deaths) == "pm25"] = "norm_pm25"
names(covid_cluster_cases_deaths)[names(covid_cluster_cases_deaths) == "so2"] = "norm_so2"
names(covid_cluster_cases_deaths)[names(covid_cluster_cases_deaths) == "no2"] = "norm_no2"
names(covid_cluster_cases_deaths)[names(covid_cluster_cases_deaths) == "pm10"] = "norm_pm10"

covid_cluster_cases = cbind(cluster_cases, covid_cluster_cases)
covid_cluster_deaths = cbind(cluster_deaths, covid_cluster_deaths)
covid_cluster_cases_deaths = cbind(cluster_case_fatality, covid_cluster_cases_deaths)

summary(covid_cluster_cases)







#################################################################################################
#######                                
#################################################################################################