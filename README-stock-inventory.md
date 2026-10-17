## Stock Inventory Tracker ##

### Overview ###
A beginner Python console program created as part of my Year 1 programming practice. It asks for product details and demonstrates basic stock calculations and validation.
### Features ###
- Collects a product name, product ID, price and stock quantity through console input.
- Checks that the price and quantity of products entered in the add-stock loop are not negative.
- Calculates the stock value by multiplying the product price by its quantity.
- Displays the product details and calculated stock value.
- Prints a low-stock warning when the quantity is below five units.
### Concepts demonstrated ### 
- User input and variables
- float and int conversion
- while loops and if statements
- Boolean flags for validation
- Arithmetic calculations and formatted output
### Requirements ###
- Python 3
- No external libraries are required.
### How to run ###
1. Download or clone this repository.
2. Open a terminal in the folder containing stock_total_stock.py.
3. Run:
   python3 stock_total_stock.py
4. Enter the requested product information. When prompted, type yes to enter another product.
### Current limitations ###
This is a small learning exercise rather than a complete inventory system. It does not save products between runs, and non-numeric price or quantity input can cause an error. The current validation and stock-value output are inside the loop for additional products, so the first set of details is not processed in the same way. These limitations reflect the current version of the script.