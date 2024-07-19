# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

# kerala bus
lists_k=[]
df_k=pd.read_csv("df_k.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#Andhra bus
lists_A=[]
df_A=pd.read_csv("df_A.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#Telungana bus
lists_T=[]
df_T=pd.read_csv("df_T.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

#Goa bus
lists_g=[]
df_G=pd.read_csv("df_G.csv")
for i,r in df_G.iterrows():
    lists_g.append(r["Route_name"])

#Rajastan bus
lists_R=[]
df_R=pd.read_csv("df_R.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])


# South bengal bus 
lists_SB=[]
df_SB=pd.read_csv("df_SB.csv")
for i,r in df_SB.iterrows():
    lists_SB.append(r["Route_name"])

# Haryana bus
lists_H=[]
df_H=pd.read_csv("df_H.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])

#Assam bus
lists_AS=[]
df_AS=pd.read_csv("df_AS.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv("df_UP.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

#West bengal bus
lists_WB=[]
df_WB=pd.read_csv("df_WB.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])

#setting up streamlit page
slt.set_page_config(layout="wide")

web=option_menu(menu_title="🚌OnlineBus",
                options=["Home","📍States and Routes"],
                icons=["house","info-circle"],
                orientation="horizontal"
                )
# Home page setting
if web=="Home":
    slt.image("t_500x300.jpg",width=200)
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":blue[Domain:]  Transportation")
    slt.subheader(":blue[Ojective:] ")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    slt.subheader(":blue[Overview:]") 
    slt.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data...")
    slt.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    slt.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                    and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    slt.subheader(":blue[Skill-take:]")
    slt.markdown("Selenium, Python, Pandas, MySQL,mysql-connector-python, Streamlit.")
    slt.subheader(":blue[Developed-by:]  Kavitha Thangavel")

# States and Routes page setting
if web=="📍States and Routes":    
    S=slt.selectbox("Lists of States",["Kerala","Adhra Pradesh","Telugana","Goa",
                                    "Rajastan","South Bengal","Haryana","Assam","Utrra Pradesh","West Bengal"])
    
    select_fare=slt.radio("choose bus fare range",("50-1000","1000-2000","2000 and above")) 

    # Kerala bus fare filtering
    if S=="Kerala":
        K=slt.selectbox("list of routes",lists_k)

        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{K}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
         
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{K}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{K}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
    
    # Adhra Pradesh bus fare filtering
    if S=="Adhra Pradesh":
        A=slt.selectbox("list of routes",lists_A)
        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{A}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
               
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{A}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{A}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

    # Telugana bus fare filtering
    if S=="Telugana":
        T=slt.selectbox("list of routes",lists_T)
        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{T}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
               
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{T}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{T}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

    # Goa bus fare filtering
    if S=="Goa":
        G=slt.selectbox("list of routes",lists_g)

        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{G}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
               
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{G}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{G}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

    # Rajastan bus fare filtering
    if S=="Rajastan":
        R=slt.selectbox("list of routes",lists_R)

        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{R}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
               
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{R}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{R}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

    # South Bengal bus fare filtering       
    if S=="South Bengal":
        SB=slt.selectbox("list of rotes",lists_SB)
        
        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{SB}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
               
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{SB}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{SB}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

    # Haryana bus fare filtering
    if S=="Haryana":
        H=slt.selectbox("list of rotes",lists_H)
        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{H}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
               
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{H}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{H}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)

    # Assam bus fare filtering
    if S=="Assam":
        AS=slt.selectbox("list of rotes",lists_AS)

        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{AS}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
               
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{AS}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{AS}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

    # Utrra Pradesh bus fare filtering
    if S=="Utrra Pradesh":
        UP=slt.selectbox("list of rotes",lists_UP)
        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{UP}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
               
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{UP}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{UP}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 
    
    # West Bengal bus fare filtering
    if S=="West Bengal":
        WB=slt.selectbox("list of rotes",lists_WB)

        if select_fare=="50-1000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 50 and 1000 and Route_name="{WB}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df)
               
        if select_fare=="1000-2000":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price Between 1000 and 2000 and Route_name="{WB}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

        if select_fare=="2000 and above":
            conn=mysql.connector.connect(host="localhost", user="root", password="kavi",database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            query=f'''select * from bus_details 
                                where Price > 2000 and Route_name="{WB}"
                                order by Price desc '''
            my_cursor.execute(query)
            out=my_cursor.fetchall()
            df=pd.DataFrame(out,columns=["ID","Bus_name","Bus_type","Start_time","End_time","Total_duration",
                                            "Price","Seats_Available","Ratings","Route_link","Route_name"])
            slt.write(df) 

