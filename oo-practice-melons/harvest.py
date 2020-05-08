############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing, *argv):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        for additional_argument in argv:
            self.pairings.append(additional_argument)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries', 'mint')
    all_melon_types.append(casaba)


    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 
                                  'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for food in melon.pairings:
            print(f"- {food}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_catalogue = {}

    for melon in melon_types:
        melon_catalogue[melon.code] =  melon_catalogue.get(melon.code, melon)

    return melon_catalogue

# melon_types = make_melon_types()
# print_pairing_info(melon_types)
# print(make_melon_type_lookup(melon_types))

# ###########
# Part 2   #
# ###########

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, 
                 color_rating, field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
  
    def is_sellable(self):
        if (self.shape_rating > 5 
            and self.color_rating > 5 
            and self.field != 3):
            
            return True
        else:
            return False

    #cmelons_by_id = make_melon_type_lookup(melon_types)

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_harvested = []

    melons_by_id = make_melon_type_lookup(melon_types)
    
    # Fill in the rest
    melon1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons_harvested.extend([melon1, melon2, melon3, melon4, melon5, melon6, 
                   melon7, melon8, melon9])

    return melons_harvested

def make_melons_from_file(filename):
    melons_harvested = [] 

    melons_by_id = make_melon_type_lookup(make_melon_types())

    harvest_log = open(filename)
    for line in harvest_log:
        info = line.strip().split(" ")
        (_, shape_rating, _, color_rating, 
        _, melon_type, _, _, harvester, _, _, 
        field) = info 
        
        melon = Melon(melons_by_id[melon_type], int(shape_rating), 
                      int(color_rating), int(field), harvester)

        melons_harvested.append(melon)

    harvest_log.close

    return melons_harvested



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() == True: 
            print(f"Harvested by {melon.harvester}from"
                  f"Field {melon.field} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvester} from"
                  f"Field {melon.field} (NOT SELLABLE)")




# melon_list = make_melon_types()

# melon_dictionary = make_melon_type_lookup(melon_list)

# melons_numbered_list = make_melons(melon_list)

# get_sellability_report(melons_numbered_list)

melons = make_melons_from_file('harvest_log.txt')
get_sellability_report(melons)



