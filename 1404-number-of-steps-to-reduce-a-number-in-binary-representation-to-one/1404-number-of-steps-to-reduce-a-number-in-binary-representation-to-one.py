class Solution:
    def numSteps(self, s: str) -> int:
        # Convert the binary string to a decimal (base 10) integer
        num = int(s,2)
        # Counter to track number of operations performed
        steps = 0
        
        # Continue until the number becomes 1
        while num != 1:
            # If number is even → divide by 2
            # (because last binary bit is 0)
            if num % 2 == 0:
                num //= 2
            # If number is odd → add 1
            # (this makes it even so it can later be divided by 2)
            else:
                num += 1
            # Increment step count after each operation
            steps += 1
        
        # Return total steps needed to reduce number to 1
        return steps
        