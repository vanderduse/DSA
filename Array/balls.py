
def uniquetiumbers(input1, input2, input3):
        # Initialize a set to store unique numbers of marbles
        unique_numbers = set()
        
        # Function to perform operations to remove marbles and update unique numbers
        def perform_operations(num):
            if num >= input1:
                unique_numbers.add(num - input1)
            if num >= input2:
                unique_numbers.add(num - input2)
            if num >= input3:
                unique_numbers.add(num - input3)
        
        # Initialize the set with the initial number of marbles (N)
        unique_numbers.add(input1)
        unique_numbers.add(input2)
        unique_numbers.add(input3)
        
        # Keep performing operations until no new unique numbers can be obtained
        previous_length = 0
        while len(unique_numbers) != previous_length:
            previous_length = len(unique_numbers)
            new_numbers = list(unique_numbers)  # Make a copy to avoid RuntimeError
            for num in new_numbers:
                perform_operations(num)
        
        # Return the total number of unique positive integers left in the jar
        return len(unique_numbers)

print(uniquetiumbers(4,1,2))