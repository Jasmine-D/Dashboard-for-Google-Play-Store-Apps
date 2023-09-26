# Dashboard for Google Play Store Apps
demo: https://drive.google.com/file/d/1m-EgsPgP30YkaP2_3osDpOuY0VoPaxll/view?usp=drive_link
## Description
Analyzing the Google Play Store Apps dataset, the objectives are to determine the correlations between ratings, 
reviews, and installs, assess the distribution of app categories and price types within each content rating, 
identify the category with the highest number of apps, and investigate whether this category also boasts the 
highest average number of reviews, indicating its popularity.

## Requirements
dash 1.20.0

numpy 1.20.3

pandas 1.2.4

plotly 4.14.3

## Run
1. Install the dependencies.
2. Run `google-apps-dash.py`.

## Data cleaning
<img width="501" alt="image" src="https://github.com/Jasmine-D/Dashboard-for-Google-Play-Store-Apps/assets/49736511/fe19a1a6-ba20-4be0-b065-5a123fb67d6a">

After data cleaning, the whole dataset is decreased from 10840 to 8103.

## Layout of the Dashboard
### Interface of the Dashboard
<img width="780" alt="image" src="https://github.com/Jasmine-D/Dashboard-for-Google-Play-Store-Apps/assets/49736511/fbd481f6-8c1a-40c8-86ff-783877d259c4">

### Scatter Chart
<img width="715" alt="image" src="https://github.com/Jasmine-D/Dashboard-for-Google-Play-Store-Apps/assets/49736511/7aeb6b6f-1862-4684-8668-b976d6aec5bd">

- The majority of rating ranges from 3 to 5. 
- Most of the reviews ranges from 0 to 10M.
- High score does not mean a lot of reviews and installment, so we cannot simply 
say that the application with the highest score must be the best. Maybe it just 
lack enough people to use and make comment.
- Apps with high review fall into two categories----social and communication, 
which means social and communication apps get lots of attention from people 
than other apps. Socializing is an integral part of people's lives.

### Sunburst Chart
<img width="548" alt="image" src="https://github.com/Jasmine-D/Dashboard-for-Google-Play-Store-Apps/assets/49736511/4ff3f374-c2e3-4dbe-a16e-ce470cd0d223">

- Most of the apps are free.
- A large proportion of free apps can be used by everyone . 
- Communication apps rank highest in free apps for everyone. 
- Social apps rank highest in free apps for teenages.
- Game apps rank top in free apps for 'Everyone 10+'
- ......

### Bar Chart & Line Chart
<img width="714" alt="image" src="https://github.com/Jasmine-D/Dashboard-for-Google-Play-Store-Apps/assets/49736511/8ad0d234-e4ff-4166-86e9-52ef02137837">

- The largest proportion of apps are family apps.
- The largest number does not have direct relationship with great number in 
average review.
- Finance apps ranks highest in average reviews. People make a lot of comments 
on finance apps, which means people focus more on how to manage money or 
other money issues. As the rise of electronic payment, more and more people 
begin to use such kind of apps to manage their cash.
- Family apps ranks the second highest in average reviews, which indicates that 
education and other apps for children and family is getting more attention. 
Parents may play games with children for entertainment or play some puzzle 
games to cultivate logical thinking and so on.


