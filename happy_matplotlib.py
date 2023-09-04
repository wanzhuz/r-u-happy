import matplotlib.pyplot as plt

# Function reads the happiness file 
def read_data_file():
    fname = "world_pop_gdp_happy.tsv"
    infile = open(fname)

    pop_list = []
    happy_list = []
    gdp_list = []
    country_list = []

    infile.readline() # ignore column header
    
    # loop over the lines of the input file and 
    # extract the data into four lists
    for line in infile:
        line = line.strip()
        
        # The columns are Country\tGDP per Capita\tPopulation in Millions\tHappiness
        cols = line.split("\t")
        
        country = cols[0]
        country_list.append(country)
        
        pop = float(cols[1])
        pop_list.append(pop)
        
        pc_gdp = float(cols[2])
        gdp_list.append(pc_gdp)
        
        happy = float(cols[3])
        happy_list.append(happy)
    
    return country_list,gdp_list,pop_list,happy_list
    
# Function creates a bubble plot of the data in the happiness file     
def plot_data(country_list,gdp_list,pop_list,happy_list):
    # New scatter plot
    # This sets the plot size
    plt.figure(figsize=(12,6))
    
    # The size of the points will bet determined by population
    plt.scatter(gdp_list,happy_list,s=pop_list,alpha=0.3)

    # Set labels
    plt.xlabel("Per Capita GDP")  # Label x axis
    plt.ylabel("Happiness Index") # Label y axis

    # This optional code adds labels
    # loop over the country names and add them to the plot
    # at the same coordinates as the bubble if the country
    # is larger than a minimum population
    if country_list != None:
        for i in range(len(country_list)):
            label = country_list[i]    # label point by country
            x = gdp_list[i]            # x-axis location of label
            y = happy_list[i]          # y-axis location of label
            plt.annotate(label, (x, y))# set label
    
    # This shows the plot
    plt.show()

# Main program
def main():
    # read the happiness file 
    country_list,gdp_list,pop_list,happy_list = read_data_file()
    # plot the happiness data
    plot_data(country_list,gdp_list,pop_list,happy_list)

main()
