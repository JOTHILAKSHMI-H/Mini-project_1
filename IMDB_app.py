import streamlit as st 
import pymysql
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Center the title using HTML
st.title("🎥 IMDB 2024 MOVIES")



# Database connection
dbconnection = pymysql.connect(
    host="localhost",
    database="mat2",
    user="mat2",
    password="0701"
)

# Fetch the data from the database(collect)
def load_data():
    query = "SELECT * from imdbmovies"
    data = pd.read_sql(query, dbconnection)
    return data

# Load data   
movies_data = load_data()


# Convert duration from seconds to hours
movies_data['Duration'] = movies_data['Duration'] / 3600

#create sidebar

r = st.sidebar.radio(label='choose an option', options=('🏠 HOME', '📈 VISUALIZATION', '📊 FILTERATION'))
if r == '🏠 HOME':
    st.write('Welcome to home page!🎉')
    st.image('c:/Users/ADMIN/Downloads/IMDb-TV-02-1-1420x681.webp')
    

if r == '📊 FILTERATION':
    st.subheader('🍿Filter Your Movie')
    with st.form(key='🍿Filter Your Movie'):
        Gener = st.selectbox('Gener', ['--select--', 'War', 'Action', 'Biography', 'Adventure', 'Animation'])
        Duration = st.selectbox('Duration', ['--select--', '<=2hrs', '2 - 3hrs', '>=3hrs'])
        Voting = st.selectbox('Voting', ['--select--', '1 - 100', '100 - 300', '300 - 500', '500 - 700','700 - 1000','1000 - 1200', '1200 - 1500', '1500 - 3000', '3000 - 5000', '5000 - 10000','10000 - 50000', '50000 - 100000', '>=100000'])
        Rating = st.selectbox('Rating', ['--select--', '1.0 - 3.0', '3.0 - 4.0','4.0 - 5.0', '5.0 - 6.0', '6.0 - 7.0','7.0 - 8.0', '8.0 - 9.0', '9.0 - 10.0'])
        submit_button = st.form_submit_button(label='Submit')
        
    if submit_button:
        filtered_data = movies_data.copy()
        
        # Apply filter based on user input
        if Gener:
            filtered_data = filtered_data[filtered_data['Gener'] == Gener]
            
        if Duration:
            if Duration == '<=2hrs':
                filtered_data = filtered_data[filtered_data['Duration'] <= 2]
            elif Duration == '2 - 3hrs':
                filtered_data = filtered_data[(filtered_data['Duration'] >= 2) & (filtered_data['Duration'] <= 3)]
            elif Duration == '>=3hrs':
                filtered_data = filtered_data[filtered_data['Duration'] >= 3]
        
        if Voting:
            if Voting != '--select--':
             if 'Voting' in filtered_data.columns:
                if Voting == '1 - 100':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 1) & (filtered_data['Voting'] <= 100)]
                elif Voting == '100 - 300':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 100) & (filtered_data['Voting'] <= 300)]
                elif Voting == '300 - 500':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 300) & (filtered_data['Voting'] <= 500)]
                elif Voting == '500 - 700':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 500) & (filtered_data['Voting'] <= 700)]
                elif Voting == '700 - 1000':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 700) & (filtered_data['Voting'] <= 1000)]
                elif Voting == '1000 - 1200':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 1000) & (filtered_data['Voting'] <= 1200)]
                elif Voting == '1200 - 1500':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 1200) & (filtered_data['Voting'] <= 1500)]
                elif Voting == '1500 - 3000':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 1500) & (filtered_data['Voting'] <= 3000)]
                elif Voting == '3000 - 5000':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 3000) & (filtered_data['Voting'] <= 5000)]
                elif Voting == '5000 - 10000':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 5000) & (filtered_data['Voting'] <= 10000)]
                elif Voting == '10000 - 50000':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 10000) & (filtered_data['Voting'] <= 50000)]
                elif Voting == '50000 - 100000':
                    filtered_data = filtered_data[(filtered_data['Voting'] >= 50000) & (filtered_data['Voting'] <= 100000)]
                elif Voting == '>=100000':
                    filtered_data = filtered_data[filtered_data['Voting'] >= 100000]
            else:
                st.error("Column 'Voting' not found in the dataframe.")
        
        # Filter by Rating         
        if Rating != '--select--':
            if 'Rating' in filtered_data.columns:
                if Rating == '1.0 - 3.0':
                    filtered_data = filtered_data[(filtered_data['Rating'] >= 1.0) & (filtered_data['Rating'] <= 3.0)]
                elif Rating == '3.0 - 4.0':
                    filtered_data = filtered_data[(filtered_data['Rating'] >= 3.0) & (filtered_data['Rating'] <= 4.0)]
                elif Rating == '4.0 - 5.0':
                    filtered_data = filtered_data[(filtered_data['Rating'] >= 4.0) & (filtered_data['Rating'] <= 5.0)]
                elif Rating == '5.0 - 6.0':
                    filtered_data = filtered_data[(filtered_data['Rating'] >= 5.0) & (filtered_data['Rating'] <= 6.0)]
                elif Rating == '6.0 - 7.0':
                    filtered_data = filtered_data[(filtered_data['Rating'] >= 6.0) & (filtered_data['Rating'] <= 7.0)]
                elif Rating == '7.0 - 8.0':
                    filtered_data = filtered_data[(filtered_data['Rating'] >= 7.0) & (filtered_data['Rating'] <= 8.0)]
                elif Rating == '8.0 - 9.0':
                    filtered_data = filtered_data[(filtered_data['Rating'] >= 8.0) & (filtered_data['Rating'] <= 9.0)]
                elif Rating == '9.0 - 10.0':
                    filtered_data = filtered_data[(filtered_data['Rating'] >= 9.0) & (filtered_data['Rating'] <= 10.0)]
            else:
                st.error("Column 'Rating' not found in the dataframe.")

        st.dataframe(filtered_data)

#
# dbconnection.close()



if r == '📈 VISUALIZATION':
    query_option = st.sidebar.radio(label='SQL Query', options=(['TOP 10 MOVIES BY RATINGS AND VOTING',
                                                                 'COUNT OF MOVIES FOR EACH GENER', 
                                                                 'AVERAGE MOVIE DURATION PER GENER', 
                                                                 'AVERAGE VOTING COUNTS ACROSS DIFFERENT GENER', 
                                                                 'RATING DISTRIBUTION',
                                                                 'TOP RATED MOVIES FOR EACH GENER', 
                                                                 'GENERS WITH HIGHEST TOTAL VOTING COUNTS', 
                                                                 'SHOW THE SHORTEST AND LONGEST MOVIES', 
                                                                 'COMPARE AVERAGE RATINGS ACROSS GENERS', 
                                                                 'RELATIONSHIP BETWEEN RATINGS AND VOTING COUNTS']))
    
    
    #QUERY 1
    
    if query_option == 'TOP 10 MOVIES BY RATINGS AND VOTING':
        #write the first query 
        #top 10 movies by rating and voting
        query_1 = '''
        SELECT movie_name, voting, rating
        from imdbmovies
        order by rating DESC, voting DESC
        limit 10;
        '''
         
        # Fetch the data from sql
        data = pd.read_sql(query_1, dbconnection)

        #display the dataframe
        st.header('TOP 10 MOVIES BY RATINGS AND VOTINGS')
        st.dataframe(data)
    
        #plotting
    
        #rating
        st.subheader('TOP 10 MOVIES BY RATING')
        fig, ax= plt.subplots(figsize= (18,12))
        sns.barplot(x = 'rating', y ='movie_name', data=data, ax = ax)
        ax.set_xlabel('rating')
        ax.set_ylabel('movie_name')
        plt.title('TOP 10 MOVIES BY RATING')
        st.pyplot(fig)
    
        #voting 
        st.subheader('TOP 10 MOVIES BY VOTING')
        fig, ax = plt.subplots(figsize=(18,12))
        sns.barplot(x ='voting', y= 'movie_name', data=data, ax = ax )
        ax.set_xlabel('voting')
        ax.set_ylabel('movie_name')
        plt.title('TOP 10 MOVIES BY VOTING')
        st.pyplot(fig)


    #QUERY_2
    if query_option == 'COUNT OF MOVIES FOR EACH GENER':
       #write the 2nd the query
       #Genre Distribution: count of movies for each genre    
        query_2 = '''
        SELECT gener, count(*) as movie_count
        from imdbmovies
        group by gener
        order by movie_count DESC;
        '''
        #fetch the data from the sql
        data = pd.read_sql(query_2, dbconnection)
    
        #display the dataframe 
        st.header('COUNT OF MOVIES FOR EACH GENER')
        st.dataframe(data)
        
        # Plotting 
        st.subheader('COUNT OF MOVIES FOR EACH GENER')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='movie_count', y='gener', data=data, ax=ax)
        ax.set_xlabel('Number of Movies')
        ax.set_ylabel('gener')
        st.pyplot(fig)
    
    #query_3    
    #average movie duration per gener
    if query_option == 'AVERAGE MOVIE DURATION PER GENER':
        query_3 = '''
        SELECT gener, AVG(Duration / 3600) as average_duration
        from imdbmovies
        group by gener
        order by average_duration DESC;
        '''
        data = pd.read_sql(query_3, dbconnection)
        #display the dataframe
        st.header('AVERAGE MOVIE DURATION PER GENER')
        st.dataframe(data)
        
        #plotting
        st.subheader('AVERAGE MOVIE DURATION PER GENER')
        fig, ax =plt.subplots(figsize =(10, 6))
        sns.barplot(x='average_duration', y = 'gener', data = data, ax=ax)
        ax.set_xlabel('average_duration')
        ax.set_ylabel('gener')
        st.pyplot(fig)
        
        
    #Query_4
    # average voting counts across different gener
    if query_option == 'AVERAGE VOTING COUNTS ACROSS DIFFERENT GENER':
        query_4  = '''
        SELECT gener, AVG(voting) as average_voting 
        from imdbmovies
        group by gener
        order by average_voting DESC;
        '''
        
        data = pd.read_sql(query_4, dbconnection)
        #display the dataframe
        st.header('AVERAGE VOTING COUNTS ACROSS DIFFERENT GENER')
        st.dataframe(data)
        
        #plotting
        st.subheader('AVERAGE VOTING COUNTS ACROSS DIFFERENT GENER')
        fig, ax =plt.subplots(figsize =(10, 6))
        sns.barplot(x='average_voting', y = 'gener', data = data, ax=ax)
        ax.set_xlabel('average_voting')
        ax.set_ylabel('gener')
        st.pyplot(fig)
        
    #query_5
    #Rating Distribution: Display a histogram or boxplot of movie ratings.
    if query_option == 'RATING DISTRIBUTION':
        query_5 = '''
        SELECT rating, COUNT(*) as count
        FROM imdbmovies
        GROUP BY rating
        ORDER BY rating;
            '''
        #fetch the data from the sql
        data = pd.read_sql(query_5, dbconnection)
    
        #display the dataframe 
        st.header('RATING DISTRIBUTION')
        st.dataframe(data)
        
        # Plotting 
        # Plotting - Histogram
        st.subheader('HISTOGRAM MOVIE RATING')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data['rating'])
        ax.set_xlabel('Rating')
        ax.set_ylabel('Count')
        st.pyplot(fig)

        # Plotting - Boxplot
        st.header('BOXPLOT MOVIE RATING')
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.boxplot(x=data['rating'], ax=ax)
        ax.set_xlabel('Rating')
        st.pyplot(fig)
        
    #query_6
    #Genre-Based Rating Leaders: Highlight the top-rated movie for each genre in a table
    if query_option == 'TOP RATED MOVIES FOR EACH GENER':
        query_6 = '''
        SELECT gener, movie_name, rating
        FROM imdbmovies AS m1
        WHERE rating = (
            SELECT MAX(rating)
            FROM imdbmovies AS m2
            WHERE m1.gener = m2.gener
        )
        ORDER BY gener;
        '''
        #fetch the data from the sql
        data = pd.read_sql(query_6, dbconnection)
    
        #display the dataframe 
        st.header('TOP RATED MOVIES FOR EACH GENER')
        st.dataframe(data)
        
        # Plotting
        st.subheader('TOP RATED MOVIES FOR EACH GENER')
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x='rating', y='gener', data=data, ax = ax)
        ax.set_xlabel('Rating')
        ax.set_ylabel('Gener')
        st.pyplot(fig)
        
     #query_7
     #Most Popular Genres by Voting: Identify genres with the highest total voting counts in a pie chart.   
    if query_option == 'GENERS WITH HIGHEST TOTAL VOTING COUNTS':
        query_7 = '''
        SELECT gener, SUM(voting) as total_voting
        FROM imdbmovies
        GROUP BY gener
        ORDER BY total_voting DESC;
        '''
         #fetch the data from the sql
        data = pd.read_sql(query_7, dbconnection)
    
        #display the dataframe 
        st.header('GENERS WITH HIGHEST TOTAL VOTING COUNTS')
        st.dataframe(data)
        
        
        # Plotting - Pie Chart
        st.subheader('GENERS WITH HIGHEST TOTAL VOTING COUNTS')
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.pie(data['total_voting'], labels=data['gener'], autopct='%1.1f%%', startangle=140)
        ax.axis('equal')  # Equal ratio for pie is drawn as a circle
        st.pyplot(fig)
        
        
    #query_8
    #Duration Extremes: Use a table or card display to show the shortest and longest movies.
    if query_option == 'SHOW THE SHORTEST AND LONGEST MOVIES':
        query_shortest= '''
        SELECT movie_name, gener, duration
        FROM imdbmovies
        ORDER BY duration ASC
        LIMIT 1;
        '''
        
        query_longest='''
        SELECT movie_name, gener, duration
        FROM imdbmovies
        ORDER BY duration DESC
        LIMIT 1;
        '''
        #fetch the data from the sql
        data_shortest = pd.read_sql(query_shortest, dbconnection)
        data_longest = pd.read_sql(query_longest, dbconnection)
        
        #combine the data
        data_combined = pd.concat([data_shortest,data_longest])
        
        # Convert duration from minutes to hours
        data_combined['duration'] = data_combined['duration'] / 3600
    
        #display the dataframe 
        st.header('SHOW THE SHORTEST AND LONGEST MOVIES')
        st.dataframe(data_combined)
        
        
        
        # Plotting the combined results
        st.subheader('SHOW THE SHORTEST AND LONGEST MOVIES')
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.barh(data_combined['movie_name'], data_combined['duration'], color='skyblue')
        ax.set_xlabel('Duration (hours)')
        ax.set_ylabel('Movie Name')
        st.pyplot(fig)
        
        
            
     #query_9
    #Ratings by Gener: Use a heatmap to compare average ratings across genres
    if query_option == 'COMPARE AVERAGE RATINGS ACROSS GENERS':
        query_9= '''
        SELECT gener, AVG(rating) as average_rating
        FROM imdbmovies
        GROUP BY gener
        ORDER BY average_rating DESC;
        '''
        
        #fetch the data from the sql
        data = pd.read_sql(query_9, dbconnection)
    
        #display the dataframe 
        st.header('COMPARE AVERAGE RATINGS ACROSS GENERS')
        st.dataframe(data)

        
        # Plotting - Heatmap
        st.subheader('COMPARE AVERAGE RATINGS ACROSS GENERS')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(data.set_index('gener'))#.T, cmap='coolwarm', annot=True, cbar=True)
        ax.set_xlabel('gener')
        ax.set_ylabel('Average Rating')
        st.pyplot(fig)
        
        
     #query_10
    #Correlation Analysis: Analyze the relationship between ratings and voting counts using a scatter plot..
    if query_option == 'RELATIONSHIP BETWEEN RATINGS AND VOTING COUNTS':
        query_10= '''
        SELECT rating, voting
        FROM imdbmovies;
        '''
        #fetch the data from the sql
        data = pd.read_sql(query_10, dbconnection)
        
    
        #display the dataframe 
        st.header('RELATIONSHIP BETWEEN RATINGS AND VOTING COUNTS')
        st.dataframe(data)
        
        # Plotting - Scatter Plot
        st.subheader('RELATIONSHIP BETWEEN RATINGS AND VOTING COUNTS')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='rating', y='voting', data=data, ax=ax)
        ax.set_xlabel('Rating')
        ax.set_ylabel('Voting Counts')
        st.pyplot(fig)    
        
       