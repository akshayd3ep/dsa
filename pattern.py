class Pattern:

    @staticmethod
    def square_pattern(n):

        center = int(n/2)
        remainder = n%2
        number_type = "even"
        if remainder != 0:
            number_type = "odd"

        for row in range(n):
            
            for col in range(n):
                if (number_type=="odd") and (col == center) and (row == center):
                    print("  ", end="")
                
                elif (number_type=="even") and (col in [center, center-1]) and (row in [center, center-1]):
                    print("  ", end="")
                else:

                    print("* ", end="")
            print("")
  
#  Pattern.square_pattern(8)

# Right-Angled Triangle Pattern
    @staticmethod
    def ratp(n:int):
        for star in range(n):
            print("*" * (star + 1))

# Pattern.ratp(5)

# Right-Angled Number Pyramid
    # method one
    @staticmethod
    def ranp1(n: int):
        for i in range(n+1):
            print("".join(map(lambda x: str(x), range(1,i+1))))

# Pattern.ranp(5)
    #method two
    @staticmethod
    def ranp2(n: int):
        for num in range(n+1):
            for ran in range(1,num+1):
                print(ran, end="")
            print("")

# Pattern.ranp2(5)

#  Right-Angled Number Pyramid - II

    @staticmethod
    def ranp_2(n: int):
        for num in range(1,n+1):
            print(str(num) * num)

# Pattern.ranp_2(5)

#  Inverted Right Pyramid
    @staticmethod
    def irp(n: int):
        for num in range(n):
            print("*"*(n-num))

# Pattern.irp(5)

    #  Inverted Numbered Right Pyramid
    @staticmethod
    def inrp(n: int):
        for num in range(n+1):
            num = (n+1)- num
            for rep in range(1,num):
                print(rep, end="")
            print("")
            

# Pattern.inrp(6)

# Star Pyramid


