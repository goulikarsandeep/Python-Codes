# -*- coding: utf-8 -*-
"""
@author: Sandeep Goulikar
"""
import pandas as pd
import numpy as np
class parking_lot_mgr:
   
    def create_parking_lot(lot_size):
        #print(parking_lot.describe)
        global parking_lot
        parking_lot = pd.DataFrame(columns = ['Slot','Vehicle_Number','Vehicle_color'])
        parking_lot.Slot = range(1,lot_size+1)
    
    def allocate_slot(Vehicle_Number,Vehicle_color):
        if  len(parking_lot.loc[parking_lot.Vehicle_Number.isna(),'Slot']) == 0:
            print("Sorry, parking lot is full")
        else:
            indi = parking_lot.loc[parking_lot.Vehicle_Number.isna(), 'Slot'].values[0]
            parking_lot.loc[parking_lot.Slot == indi,['Vehicle_Number','Vehicle_color']] = [Vehicle_Number,Vehicle_color]
            print("Your vehicle is parked in slot number :", indi)
    def parking_lot_status() :
        print(parking_lot[pd.notna(parking_lot['Vehicle_Number'])])
    def remove_vehicle (car_slot):
        if parking_lot.loc[parking_lot.Slot == car_slot, 'Vehicle_Number'].values[0]== np.nan:
            print('Slot is already empty')
        else:
            parking_lot.loc[parking_lot.Slot == car_slot,['Vehicle_Number', 'Vehicle_color']] = [np.nan, np.nan]
            Vehicle_Number = parking_lot.loc[parking_lot.Slot == car_slot,'Vehicle_Number']
            print('Vehicle Number : '+Vehicle_Number + 'from slot : '+str(car_slot)+ 'has been removed')
    def query(Slot = None, Vehicle_Number = None, Vehicle_color = None):
        if Vehicle_Number is None and Vehicle_color is None:
            print(parking_lot[parking_lot.Slot == Slot])
        if Slot is None and Vehicle_color is None:
            print(parking_lot[parking_lot.Vehicle_Number == Vehicle_Number])
        if Vehicle_Number is None and Slot is None:
            print(parking_lot[parking_lot.Vehicle_color == Vehicle_color])
            
myparking = parking_lot_mgr
lot_size = 3
myparking.create_parking_lot(lot_size = lot_size)
myparking.allocate_slot(Vehicle_Number ='NBR 07 1234',Vehicle_color= 'Red')
myparking.allocate_slot('NBR 07 2345','Passion Red')
myparking.allocate_slot('NBR 07 3456','Blue')

myparking.parking_lot_status()
myparking.query(Vehicle_Number = 'TS 07 2345')
