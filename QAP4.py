# Description: New Insurance Policy information for customers at One Stop Insurance Company
# Author: Tyler Wall
# Date(s): March 17 - March 21, 2024

# Define required libraries
import datetime
import FormatValues as FV
import sys

# Define Constants
NEXT_POLICY_NUM = 1944
BASIC_PREM = 869.00
DIS_ADD_CARS = .25
EXTRA_LIA_RATE = 130.00
GLASS_COVERAGE = 86.00
LOANER_CAR = 58.00
HST_RATE = .15
PROCESS_FEE_MON = 39.99

CUR_DATE = datetime.datetime.now()

# Provinces using a list
PROV_LIST = ["NL", "NS", "NB", "PEI", "QC", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]

allowed_char = set("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-. '")
allowed_num = 1234567890


# Function 1
print()
while True:
    def DetCustInformation():
        while True:
            FirstName = input("Enter the customers first name (End to quit):           ").title()
            if FirstName.title() == "End":
                sys.exit()
            
            elif all(char in allowed_char for char in FirstName):
                break
                
            else:
                print("ERROR - Invalid character entry for name.")
        
        while True:
            LastName = input("Enter the customers last name:                          ").title()
            if all(char in allowed_char for char in LastName):
                break
                
            else:
                print("ERROR - Invalid character entry.")

        while True:
            StAdd = input("Enter the customers street address:                     ").capitalize()
            if all(char in allowed_char for char in StAdd):
                break
            elif any(char.isdigit() for char in StAdd):
                break
                
            else:
                print("ERROR - Street address must include valid numbers and characters.")

        while True:
            City = input("Enter the customers city:                               ").title()
            if all(char in allowed_char for char in City):
                break
                
            else:
                print("ERROR - Invalid entry. Only use letters, hyphens, apostrophies or periods.")

        # Validating the Provinces using the list above. 
        while True:
            Province = input("Enter the customers Province (XX):                      ").upper()
            if Province not in PROV_LIST:
                print("ERROR - Invalid entry for Province.")
            elif all(char in allowed_char for char in Province):
                break
            elif len(Province) != 2:
                print("ERROR - Province must be abbreviation only.")
            else:
                print("ERROR - Invalid character entry.")

        
        PostalCode = input("Enter the customers Postal Code (X9X9X9):               ").upper()
            

        while True:
            PhoneNum = input("Enter the customers phone number (999-999-9999):        ")
            if len(PhoneNum) != 12:
                print("ERROR - Phone number must be 12 characters.")
            else:
                break
            

        # Function 1 Returns
        return FirstName, LastName, StAdd, City, Province, PostalCode, PhoneNum

    # Function 2
    def VehicleInformation():
        while True:
            while True:
                NumCars = input("Enter the number of cars being insured:                 ")
                NumCars = int(NumCars)
                if NumCars == 0:
                    print("ERROR - Number of cars must be greater than 0.")
                
                else:
                    break
                
            while True:
                ExtraLiability = input("Does the customer want extra liability up to $1,000,000 (N/Y): ").upper()
                if ExtraLiability != "Y" and ExtraLiability != "N":
                    print("ERROR - Entry must be either Y or N.")
                else:
                    break
                
            while True:
                GlassCov = input("Does the customer want glass coverage (N/Y):                   ").upper()
                if GlassCov != "Y" and GlassCov != "N":
                    print("ERROR - Entry must either be Y or N.")
                else:
                    break

            while True:
                LoanerCar = input("Does the customer want a loaner car (N/Y):                     ").upper()
                if LoanerCar != "Y" and LoanerCar != "N":
                    print("ERROR - Entry must be either Y or N.")
                else:
                    break

            
            InsurancePrem = BASIC_PREM
            if NumCars > 1:
                InsurancePrem += (NumCars - 1) * (BASIC_PREM * DIS_ADD_CARS)
            
            ExtraLoanCost = 0
            if LoanerCar == "Y":
                ExtraLoanCost = LOANER_CAR * NumCars
            
            ExtraGlassCost = 0
            if GlassCov == "Y":
                ExtraGlassCost = GLASS_COVERAGE * NumCars
            
            ExtraLiaCost = 0
            if ExtraLiability == "Y":
                ExtraLiaCost = EXTRA_LIA_RATE * NumCars   
            
            TotExtraCost = ExtraLiaCost + ExtraGlassCost + ExtraLoanCost
            TotInsPrem = InsurancePrem + TotExtraCost
            HST = TotInsPrem * HST_RATE
            TotalCost = TotInsPrem + HST

            # Function 2 Returns
            return NumCars, ExtraLiability, GlassCov, LoanerCar, TotExtraCost, TotInsPrem, HST, TotalCost, InsurancePrem, ExtraLiaCost, ExtraGlassCost, ExtraLoanCost

    # Function 3
    def PaymentStatus(TotInsPrem, HST):
        TotalCost = TotInsPrem + HST
        
        MonthlyPayment = 0
        DownPay = 0
        while True:
            PAYMENT_METHODS = ["FULL","MONTHLY","DOWN"]
            print("Available Payment methods: ",PAYMENT_METHODS)
            
            PaymentMethod = input("How is the customer paying?:                             ").upper()
            if PaymentMethod not in PAYMENT_METHODS:
                print("ERROR - Invalid Payment type.")
            elif all(char in allowed_char for char in PaymentMethod):
                break
            elif PaymentMethod == "DOWN":
                while True:
                    DownPayEntry = input("Enter the amount the customer would like as a down payment (Include 2 decmial places):   ")
                    try:
                        DownPay = float(DownPayEntry)
                        break
                    except:
                        print("ERROR - Down Payment must be a proper number.")
            else:
                DownPay = 0
                break

        if PaymentMethod == "FULL":
            MonthlyPayment = TotalCost / 8
        elif PaymentMethod == "MONTHLY":
            MonthlyPayment = (TotalCost + PROCESS_FEE_MON) / 8
        elif PaymentMethod == "DOWN":
            MonthlyPayment = (TotalCost - DownPay + PROCESS_FEE_MON) / 8

        InvDate = CUR_DATE
        FirstPayDate = (CUR_DATE + datetime.timedelta(days=30)).replace(day=1)

        # Function 3 returns
        return DownPay, InvDate, FirstPayDate, PaymentMethod, MonthlyPayment, TotalCost, TotInsPrem, HST  

    # Function 4
    def Claims():
        while True:
            ClaimNum = input("Enter the claim number (99999)(0 to quit):               ")
            ClaimNum = int(ClaimNum)
            if ClaimNum == 0:
                sys.exit()
            else:
                break

        while True:
            ClaimDate = input("Enter the claim date (YYYY-MM-DD):                       ")
            ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
            break
            

        # Function 4 returns
        return ClaimNum, ClaimDate

    # Function 5
    def PrevClaims():
        # We need to include this in a formatted receipt at the end, therefore, include a LIST.
        # Put Claim No, Claim date, and Claim Amount into seperate lists.
        PrevClaimsNumLst = []
        PrevClaimDateLst = []
        PrevClaimAmtLst = []
        
        while True:
            print()
            PrevClaim = input("Are there any previous claims? (N to end)(Y/N):                    ").upper()
            if PrevClaim == "N":
                break
            elif PrevClaim != "Y":
                print("ERROR - Invalid entry. Must be Y or N.")
                continue
        
            while True:
                print()
                PrevClaimNum = input("Enter the customers previous claim number (99999)(-1 to end):           ")
                PrevClaimNum = int(PrevClaimNum)
                if PrevClaimNum == -1:
                    break
                
            
                while True:
                    PrevClaimDate = input("Enter the customers previous claim date (YYYY-MM-DD):                   ")
                    try:
                        PrevClaimDate = datetime.datetime.strptime(PrevClaimDate, "%Y-%m-%d")
                        break
                    except:
                        print("ERROR - Invalid date format. Please use YYYY-MM-DD.")
            
                
                PrevClaimAmt = input("Enter the customers previous claim amount (Include 2 decimal places):   ")
                while True:
                    try:
                        PrevClaimAmt = float(PrevClaimAmt)
                        break
                    except:
                        print("ERROR - Previous claim must be a proper number.")
                
                
                PrevClaimsNumLst.append(PrevClaimNum)
                PrevClaimDateLst.append(PrevClaimDate)
                PrevClaimAmtLst.append(PrevClaimAmt)

         
        # Function 5 returns
        return PrevClaimAmtLst, PrevClaimDateLst, PrevClaimsNumLst
    

# Call Functions and Gather the information for proper display.

    FirstName, LastName, StAdd, City, Province, PostalCode, PhoneNum = DetCustInformation()
    NumCars, ExtraLiability, GlassCov, LoanerCar, TotExtraCost, TotInsPrem, HST, TotalCost, InsurancePrem, ExtraLiaCost, ExtraGlassCost, ExtraLoanCost = VehicleInformation()
    DownPay, InvDate, FirstPayDate, PaymentMethod, MonthlyPayment, TotInsPrem, HST, TotalCost = PaymentStatus(TotInsPrem, HST)
    ClaimNum, ClaimDate = Claims()
    PrevClaimAmtLst, PrevClaimDateLst, PrevClaimsNumLst = PrevClaims()

# Display results in a well-designed RECEIPT.
    print()
    print("==============================================================")
    print(f"                ONE STOP INSURANCE COMPANY")
    print(f"                     POLICY RECEIPT")
    print("==============================================================")
    print()
    print(f"Invoice Date: {FV.FDateS(InvDate):>10s}")
    print(f"Policy Number:  {NEXT_POLICY_NUM:>4d}")
    print()
    print()
    print("Customer Information ")
    print("--------------------------------------------------------------")
    print(f"First Name:                           {FirstName:>20s}")
    print(f"Last Name:                            {LastName:>20s}")
    print(f"City:                                 {City:>20s}")
    print(f"Province:                                               {Province:>2s}")
    print(f"Postal Code:                                        {PostalCode:>6s}")
    print(f"Phone Number:                                 {PhoneNum:>12s}")
    print()
    print()
    print("Vehicle Information ")
    print("--------------------------------------------------------------")
    print(f"Number of Cars Insured:             {NumCars:>1d}            {FV.FDollar2(InsurancePrem):>9s}")
    print(f"Extra Liability Coverage:         {ExtraLiability:>3s}            {FV.FDollar2(ExtraLiaCost):>9s}")
    print(f"Glass Coverage:                   {GlassCov:>3s}            {FV.FDollar2(ExtraGlassCost):>9s}")
    print(f"Loaner Car:                       {LoanerCar:>3s}            {FV.FDollar2(ExtraLoanCost):>9s}")
    print()
    print()
    print("Insurance Premium Breakdown ")
    print("--------------------------------------------------------------")
    print(f"Total Extra Coverage Cost:                       {FV.FDollar2(TotExtraCost):>9s}")
    print(f"Total Premium:                                   {FV.FDollar2(TotInsPrem):>9s}")
    print(f"HST (15%):                                       {FV.FDollar2(HST):>7s}")
    print("--------------------------------------------------------------")
    print(f"Total Cost:                                      {FV.FDollar2(TotalCost):>9s}")
    print("--------------------------------------------------------------")
    print()
    print()
    print("Payment Details ")
    print("--------------------------------------------------------------")
    print(f"Payment Method:                               {PaymentMethod:>12s}")
    print(f"Down Payment:                                    {FV.FDollar2(DownPay):>9s}")
    print(f"Monthly Payment:                                 {FV.FDollar2(MonthlyPayment):>9s}")
    print(f"First Payment Date:                             {FV.FDateS(FirstPayDate):>10s}")
    print()
    print()
    print(f"Claims ")
    print("--------------------------------------------------------------")
    print(f"Claim Number:                                        {ClaimNum:>5d}")
    print(f"Claim Date:                                     {FV.FDateS(ClaimDate):>10s}")
    print()
    print()
    print("Previous Claims ")
    print("----------------")
    print( "Claim #                 Claim Date                   Amount")
    print("--------------------------------------------------------------")
    
    for i in range(len(PrevClaimsNumLst)):
        ClaimNo = PrevClaimsNumLst[i]
        ClaimD = PrevClaimDateLst[i]
        ClaimAmt = PrevClaimAmtLst[i]
        print()
        print(f" {str(ClaimNo):>5s}                  {FV.FDateS(ClaimD):>10s}                 {FV.FDollar2(ClaimAmt):>10s}")
  

    print("--------------------------------------------------------------")
    print()
    
    break

# Housekeeping
print("We look forward to helping you again soon!")
print()
    

        




    



    

