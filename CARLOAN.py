class car_loan:
    def __init__(self,cust_name,cnic,gender):
        self.cust_name = cust_name
        self.cnic = cnic
        self.gender = gender
        
class cardetl(car_loan):
    def __init__(self,cust_name,cnic,gender,comp_name,car_name):
        super().__init__(cust_name,cnic,gender)
        self.comp_name = comp_name
        self.car_name = car_name
        
class loan_cal(cardetl):
    def __init__(self,cust_name,cnic,gender,comp_name,car_name,dura):
        super(). __init__(cust_name,cnic,gender,comp_name,car_name)
        self.dura = dura
    def loanpermonth(self):
        comps = {'Honda':{'S2000':['2006',12000000],'CR-Z':['2012',8600000]},'Toyota':{'GT 86':['2015',15000000],'Supra':['1995',30000000]},'Mitsubishi':{'Evo VIII':['2005',6500000],'Evo X':['2008',9800000]}}
        for x,y in comps.items():
            if x == self.comp_name:
                for m,n in y.items():
                    if m == self.car_name:
                        for i in n:
                            if i == str :
                                model_car = i
                            elif i == int :
                                price_car = i
                                pr = price_car / self.dur
                                
        print('')
        print('')
        print('')
        print('NAME: ', self.cust_name)
        print('CNIC: ', self.cnic[0:8]+'******')
        print('GENDER: ', self.gender)
        print('MAKER NAME: ', self.comp_name)
        print('CAR NAME: ', self.car_name)
        print('TOTAL COST: ', price_car , 'rupees')
        print('LOAN DURATION: ', self.dura ,'months')
        print('Your car loan per month is ', pr ,'rupees')

cust_name = input('enter name: ')
cnic = input('enter cnic: ')
gender = input('enter gender: ')
print('Honda,Toyota, Mitsubishi')
comp_name = input('enter company name: ')
print('Honda :(S2000:[Model:2006, Price:12000000]),CR-Z:[Model:2012, Price:8600000]},Toyota:(GT 86:[Model:2015,Price:15000000],Supra:[Model:1995,Price:30000000]),Mitsubishi:(Evo VIII:[Model:2005,Price:6500000],Evo X:[Model:2008,Price:9800000]')
car_name = input('enter car name: ')
dura = eval(input('enter duration: '))
c1 = loan_cal(cust_name,cnic,gender,comp_name,car_name,dura)

c1.loanpermonth()
