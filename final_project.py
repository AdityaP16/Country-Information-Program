### ARYAN KARADIA UCID: 30140288, ADITYA PRASAD UCID: 30148859, ENDG 233 Final Project

import numpy as np
import matplotlib.pyplot as plt

# Class is defined here
class Country:
    """
    Class is used to create a Country Object. 

    Attributes:
        name (str): Represents country name 
        continent (str): Represents continent name
        sub region (str): Represents sub-region within country
        sq_km (str): Represents sq_km 

    """
    def __init__(self, name, continent, sub_region, sq_km):
        self.name = name
        self.continent = continent
        self.sub_region = sub_region
        self.sq_km = sq_km
    
    def all_info(self):
        """
        A basic function that prints the name and code of the Country instance

        No Parameters
        Returns nothing

        """
        print(f'\n{self.name} resides in {self.continent}, more specifically in {self.sub_region}. {self.name} has an area of {self.sq_km} square Km.\n')

def index_finder(wanted_country, from_list):
    """
    A Function that finds the user index from the list run through the function

    Parameters: 
        wanted_country: The country put into the function needed to find the index for
        from_list: The list put through the parameter that pertains to the country (taken from CSV file)

    Returns needed index for further use in the code. 
    """
    needed_index = 0
    for i in range(len(from_list)):
        if from_list[i] == wanted_country:
            needed_index = i
            return needed_index

def mean(pops_row):
    """
    A function that finds the mean from the given list(s)

    Parameters:
    pops_row: The population row inputted into the function
    
    Returns the mean for the population inputted. 
    """
    pops_mean = sum(pops_row) // len(pops_row)
    
    return pops_mean

# Main Function for code defined 
def main():

    # Importing the data from the three CSV files provided. Named "Countries", "Population", and "Threatened"        
    countries = np.genfromtxt('Country_data.csv', delimiter=',', skip_header = True, dtype = str)
    population = np.genfromtxt('Population_data.csv', delimiter=',', skip_header = True, dtype = np.int64) ### Changed dtype for runtimewarning "overflow encountered in long_scalars" ### https://stackoverflow.com/questions/7559595/python-runtimewarning-overflow-encountered-in-long-scalars
    threatened = np.genfromtxt('Threatened_Species.csv', delimiter=',', skip_header = True, dtype = int)

    # Created a list with all the countries from the countries CSV file 
    country_list = countries[:,0]

    print('\n***ENDG 233 Country Information Program***\n')

    # While loop used so that if a Country from the Country_list isnt inputted, it prompts the user to input one until its inside the list. 
    while(1):
        
        usr_country = str(input('Enter Country (First letter must be capitalized): '))
        if usr_country in country_list:
            break
        else:
            print('Please enter a valid country.')
    
    # By using the index_finder function, the users index is initialized 
    usr_index = index_finder(usr_country, country_list)
        
    # The values usr_x are equal to the specific values within the countries CSV file at the users index     
    usr_continent = countries[usr_index][1]
    usr_sub_region = countries[usr_index][2]
    usr_sq_km = countries[usr_index][3]

    # Class instance is called and the usr 
    usr_info = Country(usr_country, usr_continent, usr_sub_region, usr_sq_km)
    Country.all_info(usr_info)

    while(1):
        usr_stats = str(input('| (1) Popluation Statistics              |\n| (2) Endangered Animals statistics      |\n| (3) Exit Program                       |\n'))
         
        # If user wants to exit program
        if usr_stats == '3':
            print("\nThank you for using our Country Information program.")
            break


        while usr_stats != '3':
                if usr_stats == '1':
                    
                        print("\nThis option will allow you to see the mean population over your chosen years, the population between selected years on a graph, as well as the years with the minimum and maximum populations.\n")
                        lwr_bound = int(input('Please input minimum year: '))
                        uppr_bound = int(input('Please input maximum year: '))
                        
                        # Finds index of user's chosen years in the population_data csv file
                        lwr_index = lwr_bound - 2000 + 1
                        uppr_index = uppr_bound - 2000 + 1

                        # Creates a list starting at the users lowest year to the users highest year
                        pop_row = population[usr_index][lwr_index:uppr_index + 1]

                        # Finds the mean population over the given period
                        mean(pop_row)

                        print(f'\nThe mean population for {usr_country} from {lwr_bound} to {uppr_bound} is: {mean(pop_row)} people\n')

                        # Creates a list with every population value for user country, then finds the max population using max()
                        max_row = population[usr_index][1:]
                        max_pop = max(max_row)
                        
                        # Initializes maximum year, then iterates through ever year to find maximum year value. Finds year by adding 2000 + index
                        year = 0
                        for i in range(len(max_row)):
                            if max_row[i] == max_pop:
                                year = 2000 + i

                        print(f'\nThe maximum population for {usr_country}, is: {max_pop} people, during the year {year}\n')

                        # Creates a list with every population value for user country, then finds the min population using min()
                        min_row = population[usr_index][1:]
                        min_pop = min(min_row)

                        # Initializes minimum year, then iterates through ever year to find minimum year value. Finds year by adding 2000 + index
                        year = 0
                        for i in range(len(min_row)):
                            if min_row[i] == min_pop:
                                year = 2000 + i

                        print(f'\nThe minimum population for {usr_country}, is: {min_pop} people, during the year {year}\n')

                        ################ Graphing the Population ##########################

                        usr_input_pop_data = pop_row.tolist()

                        year = list(range(lwr_index + 2000 - 1, uppr_index + 2000))
                        
                        plt.plot(year, usr_input_pop_data, '-o', label = 'Number of Citizens')
                        plt.title(f"{usr_country}'s Population From {lwr_bound} to {uppr_bound}")
                        plt.xlabel('Years')
                        plt.ylabel('Population')
                        plt.legend (loc = 'upper left')
                        plt.xticks(year)

                        plt.show()

                        print('\nReturning to Main Menu...\n')
                        break

                elif usr_stats == '2':

                    print(f"\n This option shows you the total amount of endangered animals within a given country, then graphs the total amount of each endagered animal within {usr_country}'s sub region.\n ")

                    # Uses the csv file to find specific endangered species within user country, takes specific amount and finds sum
                    usr_species = threatened[usr_index][1:] 
                    total_animals = sum(usr_species)

                    print(f'\nThe total amount of endangered animals in {usr_country} is {total_animals}.\n')

                    sub_region_country = []

                    for i in range(len(countries)):

                        # Creats a list of every country within the sub region of the users country.
                        if countries[usr_index][2] == countries[i][2]:
                            sub_region_country.append(countries[i][0])
                        
                    total_plant = 0
                    total_fish = 0
                    total_bird = 0
                    total_mammal = 0

                    for i in range(len(sub_region_country)):

                        # For every country within the same sub-region, Finds total amount of every type of endangered species.
                        country_index = index_finder(sub_region_country[i], country_list)

                        total_plant += threatened[country_index][1]
                        total_fish += threatened[country_index][2]
                        total_bird += threatened[country_index][3]
                        total_mammal += threatened[country_index][4]

                    # X and Y axis' for the graph
                    sub_region_total = [total_plant, total_fish, total_bird, total_mammal] 
                    species = ['Plants', 'Fish', 'Birds', 'Mammals']

                    ################ Graphing the Endangered Species ##########################

                    plt.bar(species, sub_region_total)
                    plt.title(f"Total Amount of Endangered Species in the Sub-Region of {countries[usr_index][2]}")
                    plt.xlabel('Species')
                    plt.ylabel('Number of Endangered Species')
                    plt.show()

                    print('\nReturning to Main Menu...\n')
                    break

                else:

                    # If user's input is not recognized allows for another input from user.
                    print('\nPlease enter a valid input.\n')
                    break

        

if __name__ == '__main__':
    main()
