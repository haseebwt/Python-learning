# OOp - Practice

class Building:
    
    def __init__(self, season_in_year, appartment_number, appartment_size):
        self.season_in_year = season_in_year
        self.appartment_number = appartment_number
        self.appartment_size = appartment_size

    def rental_calculation(self):
        
        base_price_per_month = 2000

        season_price_buffer = 0
        
        if self.season_in_year == 'Summer':
            season_price_buffer = 1.5

        elif self.season_in_year == 'Winter':
            season_price_buffer = 1.1

        elif self.season_in_year == 'Spring':
            season_price_buffer = 1.4

        elif self.season_in_year == 'Autum':
            season_price_buffer = 1.3

        else:
            season_price_buffer = None


        if self.appartment_size > 130:
            season_price_buffer += 0.1

        total_rent = base_price_per_month * season_price_buffer
        print(f"The buffer is: {season_price_buffer}")
        print("The total percentage is %s " %total_rent)

        return total_rent
        
    def maintainance_pay(self, total_rent):
        
        maintainance = 0

        if total_rent > 3000:
            maintainance = 100

        else:
            maintainance = 50

        print(f"The maintainance is: {maintainance}")


lease_contract1 = Building('Summer', 4, 135)
tota_rent1 = lease_contract1.rental_calculation()
lease_contract1.maintainance_pay(tota_rent1)

print("\n")

lease_contract2 = Building('Spring', 6, 100)
tota_rent2 = lease_contract2.rental_calculation()
lease_contract2.maintainance_pay(tota_rent2)