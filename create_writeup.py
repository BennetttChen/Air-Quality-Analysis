from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

def create_writeup():
    doc = SimpleDocTemplate(
        "chen_writeup.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30
    ))
    
    content = []
    
    # Title and Author
    content.append(Paragraph("Air Quality Analysis Project", styles['CustomTitle']))
    content.append(Paragraph("INFO 348 - Final Project", styles['Heading2']))
    content.append(Paragraph("Biao Chen", styles['Heading2']))
    content.append(Spacer(1, 30))
    
    # Project Goals
    content.append(Paragraph("Project Goals", styles['Heading2']))
    content.append(Paragraph("""
    For my final project in INFO 348, I decided to explore air quality data across different US cities. 
    As someone who has always been interested in environmental issues, I wanted to understand how 
    air pollution varies across different locations and what patterns we might find in the data. 
    
    I was particularly curious about which cities have the highest pollution levels and what types 
    of pollutants are most common. I also wanted to see if there were any interesting patterns 
    in how air quality changes throughout the day or week. This kind of analysis could be really 
    useful for understanding when and where air quality is at its worst, which could help people 
    make better decisions about when to spend time outdoors.
    """, styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Dataset Description
    content.append(Paragraph("Dataset Description", styles['Heading2']))
    content.append(Paragraph("""
    For this project, I worked with data from the OpenAQ API, which collects air quality measurements 
    from monitoring stations across the United States. Getting the data was actually one of the more 
    challenging parts of the project. I had to learn how to use API requests in Python and figure out 
    how to handle all the different types of data that came back.

    The data included measurements for several different pollutants like PM2.5, PM10, CO, and ozone. 
    Each measurement came with information about where and when it was taken. Before I could analyze 
    anything, I had to clean up the data quite a bit. This meant dealing with missing values, making 
    sure all the timestamps were in the same format, and organizing everything into a structure that 
    would be easy to work with.
    """, styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Completed Tasks
    content.append(Paragraph("What I Did", styles['Heading2']))
    content.append(Paragraph("""
    My project involved three main parts. First, I had to figure out how to get data from the OpenAQ API, 
    and it took some trial and error to get it right. I wrote code to make requests to the API and handle
    the responses, making sure to catch any errors that might come up.

    Once I had the data, I moved on to the analysis part. I used Python libraries like pandas to calculate 
    things like average pollution levels for different cities and look at how pollution levels changed 
    over time. This was probably the most interesting part because I started to see patterns in the data 
    that I hadn't expected.

    Finally, I created visualizations to help understand the patterns better. I used matplotlib and 
    seaborn to create different types of plots showing pollution levels across cities, how different 
    pollutants were distributed, and how they changed over time. Getting the visualizations to look 
    clear and informative took quite a bit of tweaking, but I think they ended up being really helpful 
    for understanding the data.
    """, styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Challenges
    content.append(Paragraph("Challenges I Faced", styles['Heading2']))
    content.append(Paragraph("""
    This project definitely had its challenging moments. The biggest hurdle was probably dealing with 
    the API at first. Sometimes the requests would fail, or the data wouldn't come back in the format 
    I expected. I learned that it's really important to test your code with different scenarios and 
    have good error handling.

    Another challenge was dealing with time zones in the data. Different monitoring stations reported 
    their times differently, and I had to figure out how to convert everything to a standard format 
    so I could compare measurements from different locations. This taught me a lot about working with 
    datetime data in Python.

    The visualizations also presented some challenges. When I first tried to create plots, they were 
    pretty messy and hard to understand. I had to spend time learning about different plotting options 
    and figure out the best ways to present the data clearly.
    """, styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Results
    content.append(Paragraph("What I Found", styles['Heading2']))
    content.append(Paragraph("""
    My analysis revealed some interesting patterns in air quality across different cities. I found that 
    La Casa NCORE had the highest levels of PM10 pollution, while Tulsa showed significant variations 
    in PM2.5 levels. CO levels were pretty consistent across all locations, which was surprising to me.

    I also noticed some clear patterns in how pollution levels change throughout the day. For example, 
    PM2.5 levels often peaked during morning and evening hours, which might be related to rush hour 
    traffic. Some pollutants, like ozone, showed strong patterns related to sunlight, with higher 
    levels during the middle of the day.

    One of the most interesting findings was how different cities had their own unique "pollution 
    profiles" - patterns of which pollutants were most common and how they varied over time. This 
    really showed me how local factors like traffic, industry, and geography can affect air quality.
    """, styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Future Work
    content.append(Paragraph("Future Ideas", styles['Heading2']))
    content.append(Paragraph("""
    While I'm happy with what I accomplished in this project, there's a lot more that could be done 
    with this data. It would be really interesting to look at how weather conditions affect pollution 
    levels. I think adding weather data to the analysis could help explain some of the patterns we see.

    Another interesting direction would be to collect data over a longer time period to look for 
    seasonal patterns. The current analysis only covers about a month, but air quality probably varies 
    quite a bit throughout the year.

    I also think it would be cool to add some kind of prediction capability - maybe using machine 
    learning to forecast pollution levels based on historical patterns. This could be really useful 
    for helping people plan outdoor activities.

    Overall, this project taught me a lot about working with real-world data and the challenges that 
    come with it. It was really satisfying to take raw data from an API and turn it into meaningful 
    insights about air quality in different cities.
    """, styles['Normal']))
    
    doc.build(content)

if __name__ == "__main__":
    create_writeup() 