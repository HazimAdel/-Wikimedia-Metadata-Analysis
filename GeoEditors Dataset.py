import pandas as pd
import matplotlib.pyplot as plt
import pycountry_convert as pc

geoeditor = pd.read_csv('C:\\Users\\GTS\\Downloads\\geoeditors.csv')

def country_to_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    except:
        if country_name == 'unknown': return 'unknown'
        if country_name == 'Caribbean Netherlands': return "Europe"
        if country_name == 'Kosovo': return "Europe"
        if country_name == 'Vatican City': return "Europe"
        if country_name == 'Timor-Leste': return "Asia"
        print(country_name)
        return ''

plt.style.use('seaborn-darkgrid')

geoeditor['continent'] = geoeditor['country'].apply(country_to_continent)


filtered_df = geoeditor[['continent', 'number_of_edits']].copy()
pd.crosstab(filtered_df['continent'],filtered_df['number_of_edits']).plot.bar()
plt.xticks(fontsize=7,weight='bold')
plt.title('Number of edits in each continent')
plt.xlabel('continents')
plt.ylabel('number of edits')
plt.show()

asia_df=geoeditor[geoeditor['continent'] == 'Asia']
pd.crosstab(asia_df['country'],asia_df['number_of_edits']).plot.bar()
plt.xticks(fontsize=7)
plt.title('Number of edits in Asia')
plt.xlabel('countries')
plt.ylabel('number of edits')
plt.show()

europe_df=geoeditor[geoeditor['continent'] == 'Europe']
pd.crosstab(europe_df['country'],europe_df['number_of_edits']).plot.bar()
plt.xticks(fontsize=7,weight='bold')
plt.title('Number of edits in Europe')
plt.xlabel('countries')
plt.ylabel('number of edits')
plt.show()

oceania_df=geoeditor[geoeditor['continent'] == 'Oceania']
pd.crosstab(oceania_df['country'],oceania_df['number_of_edits']).plot.bar()
plt.xticks(fontsize=7,weight='bold')
plt.title('Number of edits in Oceania')
plt.xlabel('countries')
plt.ylabel('number of edits')
plt.show()

s_america_df=geoeditor[geoeditor['continent'] == 'South America']
pd.crosstab(s_america_df['country'],s_america_df['number_of_edits']).plot.bar()
plt.xticks(fontsize=7,weight='bold')
plt.title('Number of edits in South America')
plt.xlabel('countries')
plt.ylabel('number of edits')
plt.show()

n_america_df=geoeditor[geoeditor['continent'] == 'North America']
pd.crosstab(n_america_df['country'],n_america_df['number_of_edits']).plot.bar()
plt.xticks(fontsize=7,weight='bold')
plt.title('Number of edits in North America')
plt.xlabel('countries')
plt.ylabel('number of edits')
plt.show()

afrcia_df=geoeditor[geoeditor['continent'] == 'Africa']
pd.crosstab(afrcia_df['country'],afrcia_df['number_of_edits']).plot.bar()
plt.xticks(fontsize=7,weight='bold')
plt.title('Number of edits in Africa')
plt.xlabel('countries')
plt.ylabel('number of edits')
plt.show()

unknown_df=geoeditor[geoeditor['continent'] == 'unknown']
pd.crosstab(unknown_df['country'],unknown_df['number_of_edits']).plot.bar()
plt.xticks(fontsize=7,weight='bold')
plt.title('Number of edits in unknown')
plt.xlabel('unknown')
plt.ylabel('number of edits')
plt.show()

arwiki_df=geoeditor[geoeditor['wiki_db'] == 'arwiki']
pd.crosstab(arwiki_df['wiki_db'],arwiki_df['continent']).plot.bar()
plt.title('Continents using Arabic wiki')
plt.show()
pd.crosstab(arwiki_df['wiki_db'],arwiki_df['country']).plot.bar()
plt.title('Countries using Arabic wiki')
plt.show()
pd.crosstab(arwiki_df['continent'],arwiki_df['lower_bound']).plot.bar()
plt.title('lower bound of editors from continents using Arabic wiki')
plt.show()
pd.crosstab(arwiki_df['continent'],arwiki_df['upper_bound']).plot.bar()
plt.title('upper bound of editors from continents using Arabic wiki')
plt.show()



col = geoeditor.loc[: , "lower_bound":"upper_bound"]
geoeditor['bound_mean'] = col.mean(axis=1)
continent = geoeditor.groupby("continent")['bound_mean'].count()
mylabels = ["Africa","Asia", "Europe", "North America", "Oceania","South America","unknown"]
plt.pie(continent, labels = mylabels, startangle = 90,autopct='%1.1f%%')
plt.title('The average of lower and upper bound in continents')
plt.show()

asia_df=geoeditor[geoeditor['continent'] == 'Asia']
col = geoeditor.loc[: , "lower_bound":"upper_bound"]
geoeditor['bound_mean'] = col.mean(axis=1)
country= geoeditor.groupby(asia_df["country"])['bound_mean'].count()
mylabels = ["Afghanistan","Armenia","Bangladesh","Bhutan","Brunei","Cambodia","Cyprus","Georgia","Hong Kong","India",
            "Indonesia","Israel","Japan","Jordan","Kuwait","Kyrgyzstan","Lebanon","Macao","Malaysia","Maldives","Mongolia",
            "Nepal","Oman","Palestine","Philippines","Qatar","South Korea","Sri Lanka","Taiwan","Timor-Leste"]
percent = 100.*country/country.sum()
patches, texts = plt.pie(country,  startangle=90, radius=1.2)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(mylabels, percent)]
sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, country),
                                          key=lambda mylabels: mylabels[2],
                                          reverse=True))
plt.legend(patches, labels, loc='upper right', bbox_to_anchor=(-0.1, 1.),
           fontsize=9)
plt.title('The average of lower and upper bound in Asia')
plt.show()

