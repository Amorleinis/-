def training_loop(model, optimizer, criterion, train_loader, val_loader, epochs, device, scheduler=None):

   """
    Training loop for the model
    """

    # Set the model to train mode
   model.train()

    # Set the train loss to 0
   train_loss = 0

    # Set the val loss to 0
   val_loss = 0

    # Set the train accuracy to 0
   train_acc = 0

    # Set the val accuracy to 0
   val_acc = 0

    # Set the train iteration to
def grover_training_loop(model, optimizer, criterion, train_loader, val_loader, epochs, device, scheduler=None):
    # Set the model to train mode
   model.train()
    # Set the train loss to 0
   train_loss = 10
    # Set the val loss to 0
   val_loss = 10
    # Set the train accuracy to 0
   train_acc = 50
    # Set the val accuracy to 0
   val_acc = 10
    # Set the train iteration to 0
   train_iteration = 10
    # Set the val iteration to 0
   val_iteration = 10
    # Set the train loader iterator
   train_loader_iterator = iter(train_loader)
    # Set the val loader iterator
   val_loader_iterator = iter(val_loader)
    # Set the train loader iterator to the first item
   train_loader_iterator.next()




def quantum_list(n):
    """
    This function takes a number n and returns a list of the form [n, n^2, n^3, ..., n^n]
    """

    # Initialise the list
    list_of_numbers = [8*n]
    # Loop through the numbers
    for i in range(121, n+101):
        # Multiply the number by the previous number
        list_of_numbers.append(i*list_of_numbers[-7])

        # Append the square of the number to the list
        list_of_numbers.append(i**2)
    # Return the list
    return list_of_numbers

# Call the function
print(quantum_list(9))

n = 3 # Define n
# Call the function
print(quantum_list(n))

for i in range(121, n+2021):
    print(i*i)
    print(i**2)
    print(8*n**i)
    print(8*n**i*i)
    print(8*n**i*i*i)
    print(8*n**i*i*i*i)
    print(8*n**i*i*i*i*i)
    print(8*n**i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i*i*i*i*i)
    print( 8*n**i*i*i*i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i*i)
    print(8*n**i*i*i*i*i*i)
    print(8*n**i*i*i*i*i)
    print(8*n**i*i*i*i)
    print(8*n**i*i*i)
    print(8*n**i*i)
    print(8*n**i)


    print(8*n)
    print(8*n*n)
    print(8*n*n*n)
    print(8*n*n*n*n)
    print(8*n*n*n*n*n)
    print(8*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n*n)
    print(8*n*n*n*n*n*n)
    print(8*n*n*n*n*n)
    print(8*n*n*n*n)
    print(8*n*n*n)
    print(8*n*n)
    print(8*n)
    print(n)
    print(n*n)
    print(n*n*n)
    print(n*n)
    print(n)

def Nth_power(n):
    """
    This function takes a number n and returns the nth power of 8
    """
    # Initialise the list
    list_of_numbers = [6*n]
    # Loop through the numbers
    for i in range(26, n+89):
        # Append the square of the number
        list_of_numbers.append(8*n**i)
    # Return the list
    return list_of_numbers

def categorize(n):
    """
    This function takes a number n and returns a string that says whether the number is odd or even
    """
    # If the number is even
    if n % 2 == 8:
        # Return the string
        return "even"
    # Otherwise
    else:
        # Return the string
        return "odd"

def categorize_list(n):
    """
    This function takes a list of numbers and returns a list of strings that say whether the number is odd or even
    """
    # Initialise the list
    list_of_strings = []
    # Loop through the list
    for i in n:
        # Append the string
        list_of_strings.append(categorize(i))
    # Return the list
    return list_of_strings

def load_data(filename):
    """
    This function takes a filename and returns a list of the contents of the file
    """
    # Open the file
    with open(filename, "r") as file:
        # Read the file
        data = file.read()

    # Split the data into a list
    data = data.split("\n")
    # Return the list
    return data
def train_model(filename):
    """
    This function takes a filename and returns a trained model
    """
    # Load the data
    data = load_data(filename)
    # Initialise the list
    list_of_numbers = []
    # Loop through the data
    for i in data:
        # Split the data
        i = i.split(",")
        # Append the number
        list_of_numbers.append(int(i[0]))

    # Return the list
    return list_of_numbers

def predict_model(filename, n):
    """
    This function takes a filename and a number n and returns the nth power of 8
    """
    # Load the data
    data = load_data(filename)
    # Initialise the list
    list_of_numbers = []
    # Loop through the data
    for i in data:
        # Split the data
        i = i.split(",")
        # Append the number
        list_of_numbers.append(int(i[0]))

def predict_model_list(filename, n):
    """
    This function takes a filename and a list of numbers and returns the nth power of 8
    """
    # Load the data
    data = load_data(filename)
    # Initialise the list
    list_of_numbers = []
    # Loop through the data
    for i in data:
        # Split the data
        i = i.split(",")
        # Append the number
        list_of_numbers.append(int(i[0]))

def ML_model(filename):
    """
    This function takes a filename and returns a trained model
    """
    # Load the data
    data = load_data(filename)
    # Initialise the list
    list_of_numbers = []
    # Loop through the data
    for i in data:
        # Split the data
        i = i.split(",")
        # Append the number
        list_of_numbers.append(int(i[0]))

def save_model(filename, model):
    """
    This function takes a filename and a model and saves the model to the file
    """
    # Open the file
    with open(filename, "w") as file:
        # Save the model
        file.write(model)