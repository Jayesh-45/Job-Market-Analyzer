import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
import geopy
from geopy.geocoders import Nominatim
import folium

def plot_recruiter(company_dict):
    # Company dictionary stores the data of top-recruiters and corresponding number of openings
    # Create lists of keys and values from the dictionary
    keys_list = list(company_dict.keys())
    values_list = list(company_dict.values())
    # make dictionary contains key as field name and values the the list
    company_data = {
        'Company': keys_list,
        'Openings': values_list
    }   
    # Create dataframe for company data so that it will be easy to plot
    df = pd.DataFrame(company_data)
    # Sort the dataframe according to values column in descending order so the the visualization will look good
    df = df.sort_values(by='Openings', ascending=False)
    # Create a bar chart
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    sns.set(style="whitegrid")
    sns.barplot(x='Openings', y='Company', data=df, palette="viridis")

    # Labels and title
    plt.xlabel('Number of Openings')
    plt.ylabel('Company')
    plt.title('Top Recruiters')

    # Adding labels for the number of openings on the bars
    for index, row in df.iterrows():
        plt.text(row['Openings'], index, str(row['Openings']), va='center')

    plt.tight_layout()  # Ensure sufficient margin for company names
    plt.savefig('top_recruiter_plot.png') # Save figure 

def plot_remote(remote_dict):
    work_types = list(remote_dict.keys())
    count = list(remote_dict.values())
    # Create a pie chart
    plt.figure(figsize=(6, 6))  # Adjust the figure size as needed
    plt.pie(count, labels=work_types, autopct='%1.1f%%', colors=['lightblue', 'lightgreen'])
    # Add a title
    plt.title('Distribution of Work Types')
    # Add a legend
    plt.legend(loc='upper right')
    # Equal aspect ratio ensures that the pie is drawn as a circle.
    plt.axis('equal')

    # Display the pie chart
    plt.savefig("remote_plot.png")

def plot_salary_dist(salary_dict):
    salaries=list(salary_dict.keys())
    # salaries=list(map(lambda x: float(x[1:x.index('+')].replace(',', '')), salaries))
    job_count=list(salary_dict.values()) 
    # print("salary values", salary_values)
    # print("Job Count", job_count)
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    sns.set(style="whitegrid")
    sns.barplot(x=salaries, y=job_count, palette="viridis")

    plt.xlabel('Salary')
    plt.ylabel('Number of Jobs')
    plt.title('Salary Distribution and Job Offerings')

    plt.xticks(rotation=45)  # Rotate x-axis labels for readability

    plt.tight_layout()
    plt.savefig('salary_dist_plot.png')

def plot_skill_cloud(skills):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(skills)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Remove axes and labels
    # plt.title('Skill Cloud')
    plt.savefig('skill_could_plot.png')

def plot_education(education_dict):
    education_levels = list(education_dict.keys())
    job_openings = list(education_dict.values())  # Replace with your actual data

    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    sns.set(style="whitegrid")

    bar_plot = sns.barplot(x=education_levels, y=job_openings, palette="viridis")
    # Add count labels above the bars
    for index, value in enumerate(job_openings):
        bar_plot.text(index, value + 10, str(value), ha='center', fontsize=12)

    plt.ylabel('Number of Job Openings')
    plt.title('Education vs. Number of Job Openings')

    plt.tight_layout()
    plt.savefig('education_plot.png')

def plot_job_type(job_type_dict):
    job_types = list(job_type_dict.keys())
    job_openings = list(job_type_dict.values())
    labels = job_types
    sizes = job_openings
    # Get the "viridis" colormap
    cmap = cm.viridis

    # Extract a set of colors from the "viridis" colormap
    colors = [cmap(i / len(labels)) for i in range(len(labels))]
    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

    # Draw a circle in the center to create the donut chart
    center_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')

    plt.title('Job Types and Number of Openings')
    plt.savefig('job_type_plot.png')

def plot_job_language(job_language_dict):
    job_language = list(job_language_dict.keys())
    job_openings = list(job_language_dict.values())
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    sns.set(style="whitegrid")

    bar_plot = sns.barplot(x=job_language, y=job_openings, palette="viridis")
    # Add count labels above the bars
    for index, value in enumerate(job_openings):
        bar_plot.text(index, value + 10, str(value), ha='center', fontsize=12)
    plt.ylabel('Number of Job Openings')
    plt.title('Job Language and Number of Openings')

    plt.tight_layout() 
    plt.savefig('job_language_plot.png')

def get_location_data(job_location_dict):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="JobScan360")
    city_data = []
    for city in job_location_dict.keys():
        # Get the location of the input city
        location = geolocator.geocode(city)

        # Get the latitude and longitude of the location and save it to dictionary
        city_dict = {}
        city_dict['city'] = city
        city_dict['latitude'] = location.latitude
        city_dict['longitude'] = location.longitude
        city_dict['job_openings'] = job_location_dict[city]
        if('city' != 'Remote'):
            city_data.append(city_dict)
    # print(city_data)
    return city_data

def plot_locations(job_location_dict):
    
    # Call the get_location data function to get location data
    city_data = get_location_data(job_location_dict)

    # Create a clean map centered at India
    india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

    # Add markers with varying circle sizes for each city
    for city_info in city_data:
        city_name = city_info["city"]
        latitude = city_info["latitude"]
        longitude = city_info["longitude"]
        job_openings = city_info["job_openings"]

        # Calculate circle size based on the number of job openings
        circle_radius = job_openings / 500  # Adjust the scaling factor as needed

        # Create a circle marker for the city
        folium.CircleMarker(
            location=[latitude, longitude],
            radius=circle_radius,
            color='red',
            fill=True,
            fill_opacity=0.6,
            popup=f"{city_name}<br>Job Openings: {job_openings}"
        ).add_to(india_map)

    # Save the map to an HTML file
    india_map.save("job_openings_map.html")


job_location_dict = {'Bengaluru, Karnataka': 15917, 'Hyderabad, Telangana': 6330, 'Pune, Maharashtra': 6090, 'Chennai, Tamil Nadu': 4532, 'Mumbai, Maharashtra': 3663, 'Ahmedabad, Gujarat': 2510, 'Noida, Uttar Pradesh': 2491, 'Gurgaon, Haryana': 2421, 'Remote': 1695, 'Kolkata, West Bengal': 1174, 'Kochi, Kerala': 1013, 'Mohali, Punjab': 982, 'Jaipur, Rajasthan': 971, 'Delhi, Delhi': 954}
plot_locations(job_location_dict)