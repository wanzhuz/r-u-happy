# happy1.py
#
# Wanzhu Zheng
# Returns a dictionary mapping country names to their happiness index

def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()
    
    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)



def make_happy_dict():
    hi_to_country = {} # creates an empty dictionary
    infile = open("happiness.csv")
    infile.readline()
    
    # loops through the file
    for line in infile:
        line = line.strip() # removes whitespace
        indices = line.split(",")
        country = indices.pop(0) # first element in the list is a country

        # maps the happiness index to the country
        for index in indices:
            hi_to_country[country] = index
            
    # formats the output
    for pos in hi_to_country:
        print(pos, hi_to_country[pos])
    return hi_to_country

def read_gdp_data(happy_dict):
    return

def lookup_happiness_by_country(happy_dict):
    return

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if type(D) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(D.keys()):
        print(key, D[key])
        
main()
