from django.db import models

# Create your models here.

class Data_Model_table(models.Model):
    
    
    #Source of Waste Categories
    waste_source_id = models.IntegerField(help_text='Unique Code for source of waste')
    waste_source_profile = models.CharField(max_length=200, help_text='Source of waste ex. House, restaurant, hotel, etc.')
    
    #Food Data Categories
    food_name = models.CharField(max_length=200, help_text='Name of Food ex. apple, bread, juice, etc.')
    food_quantity = models.IntegerField(help_text='Quantity of the food item')
    food_price = models.DecimalField(max_digits=9, decimal_places=2, default=9999.99, help_text='Cost of the food item')
    
    #Waste Data Categories
    waste_date = models.DateTimeField(auto_now_add=False, help_text='Date of waste disposal.')
    waste_reason = models.CharField(max_length=200, help_text='Reason for disposing Waste.')
    waste_quantity = models.IntegerField(help_text='Weight of food waste in kgs.')
    
     
    
    def __str__(self):
        return f"{self.waste_source_id} {self.waste_source_profile} {self.food_name} {self.food_quantity} {self.food_price} {self.waste_date} {self.waste_reason} {self.waste_quantity}"
    
class Employee_Model(models.Model):
    # def __init__(self, emp_id, firstname, lastname, username, email):
        
    emp_id = models.IntegerField(null=True)
    firstname= models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        # return u'%s %s %s %s %s' % (self.emp_id, self.firstname, self.lastname, self.username, self.email)
        return f"{self.emp_id} {self.firstname} {self.lastname} {self.username} {self.email}"
        # return self.username
        # return f"Employee ID: {self.emp_id}\nFirst Name: {self.firstname}\nLast Name: {self.lastname}\nUsername: {self.username}\nEmail: {self.email}"

class Food_Model(models.Model):
    # def __init__(self, food_id, food_name, food_category, food_type, food_measurement):
    food_id = models.IntegerField(null=True)
    food_name = models.CharField(max_length=30)
    food_category = models.CharField(max_length=30)
    food_type = models.CharField(null=True, max_length=10)
    food_measurement = models.CharField(max_length=10)

    def ___str___(self):
        return self.fooditem_name

class Rubbishbin_Model(models.Model):
    # def __init__(self, bin_id, bin_name, bin_location, bin_capacity, bin_status):
    bin_id = models.IntegerField(null=True)
    bin_name = models.CharField(max_length=30)
    bin_location = models.CharField(max_length=30)
    bin_capacity = models.IntegerField()
    bin_status = models.CharField(max_length=30)
        
    def __Str___(self):
        return self.bin_name

class Waste_Model(models.Model):

    waste_id = models.IntegerField(null=True)
    waste_quantity = models.IntegerField()
    waste_date = models.DateField(auto_now_add=False)
    waste_reason = models.CharField(max_length=30)
    waste_location = models.CharField(max_length=30)
    waste_disposal_method = models.CharField(max_length=30)
    dollar_amount = models.DecimalField(max_digits=9, decimal_places=2)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    food = models.ManyToManyField(Food_Model)
    bin = models.ManyToManyField(Rubbishbin_Model)
    employeeid = models.ForeignKey(Employee_Model, on_delete=models.CASCADE)

    def ___str___(self):
        return self.food

