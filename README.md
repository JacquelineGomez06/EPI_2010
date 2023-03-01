# EPI vs Corruption 2010

***
A data exploratory project utilizing 2010 Environmental Performance Index (EPI)and Corruption datasets using SQL alchemy and Pandas to import,analyze,and plot.

Germany has the highest population followed by France,Italy,Spain and the UK. On the low end are Iceland and Luxembourg:
![Img1](https://github.com/JacquelineGomez06/EPI_2010/blob/main/images/country_pop.png "Country vs Population")

From the following bar graph we can see that Denmark,Finland and Sweden have the highest corruption scores while Italy and Greece are significantly low:
![Img2](https://github.com/JacquelineGomez06/EPI_2010/blob/main/images/country_score.png "Country vs Corruption Score")

For air, none of the countries fall below 80 with Greece habing the lowest air_h
![Img3](https://github.com/JacquelineGomez06/EPI_2010/blob/main/images/country_air.png "Country vs Air_H")

Taking a look at population vs corruption score we see that our data is positively skewed. There's a cluster of countries with low population and high corruption scores. We can also note that the low corruption score outliers are Greece and Italy. We could include more countries to see if wen can get a better picture of the relationship between corruption score and a country's population.
![Img4](https://github.com/JacquelineGomez06/EPI_2010/blob/main/images/pop_score.png "Population vs Corruption Score")

In the following scatter plot, our data is negatively skewed.Greece is yet another outlier here withe lowest corruption score and lowest air_h.
![Img5](https://github.com/JacquelineGomez06/EPI_2010/blob/main/images/air_score.png "Corruption Score vs Air_H")

***
As an extension of the analysis above, the corruption scores and air_h index have been mapped globally in the following dashboard:
Tableau Dashboard 
https://prod-useast-a.online.tableau.com/t/jacquelinegomez06/views/GlobalEPIvsCorruption2010/Dashboard1?:origin=card_share_link&:embed=n

On a global scale, the corruption scores are quite low, indicated by the color RED.

Bsed on the scatter plot, most countries are visibly under the 400m mark and range in corruption scores. This data is NOT normaly distributed and therefore we cannot say that population has an effect on a country's corruption score.