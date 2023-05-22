from django.db import models

class Food:
    def __init__(self, Food_ID, Food_Name, Food_Desc, Food_Category):
        self.Food_ID = Food_ID
        self.Food_Name = Food_Name
        self.Food_Desc = Food_Desc
        self.Food_Category = Food_Category

class Bin:
    def __init__(self, Bin_ID, Bin_Name, Bin_Size, Bin_Status, Bin_Area):
        self.Bin_ID = Bin_ID
        self.Bin_Name = Bin_Name
        self.Bin_Size = Bin_Size
        self.Bin_Status = Bin_Status
        self.Bin_Area = Bin_Area

class User:
    def __init__(self, User_ID, User_Name, User_ContactNo, User_Address):
        
        self.User_ID = User_ID
        self.User_Name = User_Name
        self.User_ContactNo = User_ContactNo
        self.User_Address = User_Address

class Waste:
    def __init__(self, Waste_ID, Waste_Date, Waste_Quantity, Waste_Type, Waste_Unit, Food_ID, Bin_ID, User_ID):
        self.Waste_ID = Waste_ID
        self.User_ID = User_ID
        self.Bin_ID = Bin_ID
        self.Food_ID = Food_ID
        self.Waste_Quantity = Waste_Quantity
        self.Waste_Date = Waste_Date
        self.Waste_Type = Waste_Type
        self.Waste_Unit = Waste_Unit
