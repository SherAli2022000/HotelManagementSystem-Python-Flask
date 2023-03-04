from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
from datetime import datetime

try:
    connection = mysql.connector.connect(host='localhost',database='hotel',user='root',password='')
    if connection.is_connected():
        serverInfo = connection.get_server_info()
        cursor = connection.cursor()
        cursor.execute("select database();")
        data = cursor.fetchone()

except Error:
    print("Error while connecting to MySQL", Error)


class Room:
    room_id = 0
    room_type = ""
    room_price = 0
    room_description = ""
    room_floor = 0
    room_wing = ""
    status = False

    def __init__(self,room_id,room_type,room_price,room_description,room_floor,room_wing,status):
        self.room_id = room_id
        self.room_type = room_type
        self.room_price = room_price
        self.room_description = room_description
        self.room_floor = room_floor
        self.room_wing = room_wing
        self.status = status

    def displayRoom(self):
        print("\n")
        print ('Room id : ', self.room_id)
        print ('Room type : ', self.room_type)
        print ('Room price : ', self.room_price)
        print ('Room description : ', self.room_description)
        print ('Room floor : ',self.room_floor)
        print ('Room wing : ',self.room_wing)
        print ('Room status : ', self.status)

    def updatePrice(self,newPrice):
        if newPrice>0:
            self.room_price=newPrice
            return 1
        else:
            print("\nPrice can not be less than 1,Price is not changed : ")
            return 0

class Employee:
    emp_id = 0
    emp_name = ""
    emp_address = ""
    emp_phone = ""
    emp_salary = 0
    emp_jobtype = ""

    def __init__(self, emp_id, emp_name, emp_address, emp_phone, emp_salary, emp_jobtype):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_address = emp_address
        self.emp_phone = emp_phone
        self.emp_salary = emp_salary
        self.emp_jobtype = emp_jobtype

    def change_salary(self, sal):
        if sal>0:
            self.emp_salary = sal
            return 1
        return 0

    def change_job(self,jobType):
        if jobType=="Receptionist" or jobType=="Cleaner" or jobType=="Waiter":
            self.emp_jobtype=jobType
            return 1
        else:
            return 0

    def printDetails(self):
        print("\nFollowing are the details of the employee: ")
        print(self.emp_id)
        print(self.emp_name)
        print(self.emp_jobtype)
        print(self.emp_address)
        print(self.emp_phone)
        print(self.emp_salary)

class Reservation:
    reservation_ID = 0
    room_ID = -1
    cust_ID = -1
    Data_Added = "-"

    def __init__(self,rID,roomID,CustID):
        self.reservation_ID=rID
        self.room_ID=roomID
        self.cust_ID=CustID
        date = datetime.now().strftime("%Y-%m-%d")
        self.Data_Added = date

    def reserve(self,rID,cID,resID):
        self.room_ID=rID
        self.cust_ID=cID
        self.reservation_ID=resID
        date = datetime.now().strftime("%Y-%m-%d")
        self.Data_Added = date
        return self

    def reserve(self,rID,cID,resID,date):
        self.room_ID=rID
        self.cust_ID=cID
        self.reservation_ID=resID
        self.Data_Added = date
        return self


    def printDetails(self):
        print("\nReservation ID : ",self.reservation_ID)
        print("Room ID : ",self.room_ID)
        print("Customer ID : ",self.cust_ID)
        print("Date Added : ",self.Data_Added)

class foodServices:

    def __init__(self):
        self.charge=-1
        self.description="-"

    def getService(self,choice):
        if choice == 1:
            print("you ordered Chicken, food will be sent to your room ")
            print("Your Bill for this food is 500 rupees")
            self.charge = 500
            self.description = "Chicken ordered"
            return self
        elif choice == 2:
            print("you ordered beef, food will be sent to your room ")
            print("Your Bill for this food is 600 rupees")
            self.charge = 600
            self.description = "Beef ordered"
            return self
        elif choice == 3:
            print("you ordered mutton, food will be sent to your room ")
            print("Your Bill for this food is 700 rupees")
            self.charge = 700
            self.description = "Mutton ordered"
            return self
        else:
            print("You entered invalid number : ")
            self.charge = 0
            self.description = "-"
            return self

class Laundary():
    charge = -1
    description = "-"

    def __init__(self, c, desc):
        self.charge = c
        self.description = desc

    def getService(self,numOfClothes):
        if numOfClothes > 0:
            self.charge = numOfClothes * 10
            self.description = f"Laundary ordered with {numOfClothes} clothes"
            print("Your clothes will be laundered")
        else:
            print("number of clothes can not be less than 1")

        return self

class Cleaning:
    charge = -1
    description = "-"

    def __init__(self, c, desc):
        self.charge = c
        self.description = desc

    def getService(self):
        self.charge = 100
        self.description = "Room cleaning ordered"
        print("You ordered room cleaning")
        return self

class ServicesFactory:
    charge = -1
    description = "-"

    def __init__(self, c, desc):
        self.charge = c
        self.description = desc

    def availService(self,choice,choice2):
        if choice==1:
            return foodServices.getService(self,choice2)
        elif choice==3:
            return Cleaning.getService(self)
        elif choice==2:
            return Laundary.getService(self,choice2)

class Customer:
    customer_id =-1
    password = "-"
    name="-"
    age=0
    address="-"
    phone_no="-"
    room_id=-1
    services=[]

    def __init__(self,ID,password,name,age,add,phone):
        self.customer_id=ID
        self.password=password
        self.name=name
        self.age=age
        self.address=add
        self.phone_no=phone
        self.services=[]

    def displayDetails(self):
        print("\n")
        print("Customer ID : ",self.customer_id)
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Address : ", self.address)
        print("Phone Nuumber : ", self.phone_no)
        print("Room ID : ", self.room_id)
        print("Password: ", self.password)

    def Avail_Service(self,choice,choice2):
        if self.room_id!=-1:
           if choice ==1 :
                serv= ServicesFactory
                serv.availService(serv,1,choice2)
                self.services.append(serv)
                return serv
           elif choice ==2 :
                serv = ServicesFactory
                serv.availService(serv, 2,choice2)
                self.services.append(serv)
                return serv
           elif choice==3:
                serv = ServicesFactory
                serv.availService(serv, 3,choice2)
                self.services.append(serv)
                return serv
           else:
                print("You entered invalid input")
        else:
            print("You have not booked any room")

        serv =ServicesFactory
        return serv

    def printAllServicesAvailed(self):
        for i in self.services:
            print("Charge :",i.charge," for ", i.description)

class Payment:
    payment_id=-1
    cust_id =-1
    cust_name="-"
    total=0
    status="Not Paid"
    desc="-"
    desc="-"

    def __init__(self,pay_id,cust_id,cust_name,total,status,desc):
        self.payment_id=pay_id
        self.cust_id=cust_id
        self.cust_name=cust_name
        self.total=total
        self.status=status
        self.desc=desc
        date = datetime.now().strftime("%Y-%m-%d")
        self.Date = date

    def pay(self,pay_id,cust_id,cust_name,total,status,desc,date):
        self.payment_id = pay_id
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.total = total
        self.status = status
        self.desc = desc
        self.Date = date

    def displayPayment(self):
        print("\nPayment_ID : ",self.payment_id)
        print("Customer_ID : ",self.cust_id)
        print("Total : ",self.total)
        print("Status : ",self.status)
        print("Description : ",self.desc)
        print("Date : ",self.Date)

class Hotel:
    rooms= []
    employees = []
    customers =[]
    reservations= []
    payments=[]
    totalpayements = 0

    def addCustomer(self,cID,name,age,add,phone,password):
        if self.checkCustID(self,cID)==1:
            if len(name)>2:
                if age>0:
                    if len(add)>3:
                        if len(phone)>6:
                          if len(password)>5:
                                c=Customer(cID,password,name,age,add,phone)
                                self.customers.append(c)
                                return 1
                          else:
                              print("length of password is less than 6")
                        else:
                            print("Phone length can not be less than 7 digits")
                    else:
                        print("Address length can not be less than 3")
                else:
                    print("Age can not be less than 1")
            else:
                print("name can not be less than 3 letters")
        else:
            print("You entered an existing customer ID")
        return 0

    def printAllCustomers(self):
        for i in self.customers:
            i.displayDetails()


    def checkCustID(self,ID):
        for i in self.customers:
            if i.customer_id == ID:
                return 0
        return 1

    def checkLoginCustomer(self,ID,password):
        for i in self.customers:
            if i.customer_id==ID and i.password==password:
                print("found")
                return i
        print("not found")
        c= Customer
        return c


    def addEmployee(self,empID,name,add,phone,job,sal):
       if self.checkEmpId(self,empID)==1:
            if len(name)>2:
                if len(add)>2:
                    if len(phone)>6:
                        if job=="Receptionist" or job=="Cleaner" or job=="Waiter" or job=="Cook":
                            if (sal > 0):
                                emp=Employee(empID,name,add,phone,sal,job)
                                self.employees.append(emp)
                                return 1
                            else:
                                print("Salary can no tbe less than 0")
                        else:
                            print("you entered an invalid job type")
                    else:
                        print("Employee phoone number lenght can not be less than 7 digits")
                else:
                    print("Employee address length can not be less than 3")
            else:
                print("Employee name length can not be less than 3")
       else:
            print("You entered an existing employee ID")
       return 0

    def printAllEmployees(self):
        for i in self.employees:
            i.printDetails()


    def checkEmpId(self,ID):
        for i in self.employees:
            if i.emp_id == ID:
                return 0
        return 1

    def getEmp(self, ID):
        for i in self.employees:
            if i.emp_id == ID:
                return i

    def deleteEmp(self,eID):
        if self.checkEmpId(self,eID)==0:
            self.employees.remove(self.getEmp(self,eID))
            print(f"\nEmployee with ID { eID} is deleted")
            return 1
        else:
            print("\nEmployee with that id does not exits : ")
            return 0

    def updateEmpJob(self,eID,jobType):
        if self.checkEmpId(self, eID ) == 0:
            e=self.getEmp(self,eID)
            if e.change_job(jobType)==1:
                return 1
            else:
                return 0
        else:
            print("\nEmployee with that id does not exits : ")
            return 0

    def updateEmpsal(self,eID,sal):
       if self.checkEmpId(self, eID ) == 0:
            e=self.getEmp(self,eID)
            if e.change_salary(sal)==1:
                return 1
            else:
                return 0
       else:
            print("\nEmployee with that id does not exits : ")
            return 0

    def addRoom(self,rID,rType,rPrice,rDesc,rFloor,rWing):
        print("Add the details of the new room : ")
        if self.checkRoomID(self,rID) == 1:
           if self.checkRoomType(self,rType)==1:
               if rPrice > 0:
                   if len(rDesc)>3:
                       if rFloor>0:
                            if rWing=="Right" or rWing== "Left":
                                r=Room(rID,rType,rPrice,rDesc,rFloor,rWing,False)
                                self.rooms.append(r)
                                return 1
                            else:
                                print("You entered invalid wing information ")
                       else:
                            print("Floor can not be less than 1")
                   else:
                        print("length of description should be greator than 3 letters")
               else:
                    print("Error: Room price can not be less than or equal to 0")
           else:
                print("You enetered an invalid type")
        else:
            print("\nError : You entered an existing room ID : ")
        return 0

    def deleteRoom(self,rID):
        if self.checkRoomID(self,rID)==0:
            self.rooms.remove(self.getRoom(self,rID))
            print(f"\nRoom with ID { rID} is deleted")
            return 1
        else:
            print("\nRoom with that id does not exits : ")
            return 0

    def updateRoom(self,rID,price):
        if self.checkRoomID(self, rID) == 0:
            r=self.getRoom(self,rID)
            if r.updatePrice(price)==1:
                return 1
            else:
                return 0
        else:
            print("\nRoom with that id does not exits : ")
            return 0

    def checkRoomType(self,T):
        if T =="Suite" or T=="Normal" or T=="Presidential":
            return 1
        return 0

    def getRoom(self,ID):
        for i in self.rooms:
            if i.room_id == ID:
                return i

    def checkRoomID(self,ID):
        for i in self.rooms:
            if i.room_id == ID:
                return 0
        return 1

    def bookRoom(self,customer,roomID):
        if customer.room_id==-1:
            if self.checkRoomID(self, roomID)==0:
                r= self.getRoom(self,roomID)

                if r.status=='False':
                    r.status='True'

                    cursor = connection.cursor()
                    query = """UPDATE room set status= %s where room_id= %s"""
                    row = ('True', r.room_id)
                    cursor.execute(query, row)
                    connection.commit()

                    customer.room_id=r.room_id

                    cursor = connection.cursor()
                    query = """UPDATE customer set room_id= %s where customer_id= %s"""
                    row = (r.room_id,customer.customer_id)
                    cursor.execute(query, row)
                    connection.commit()

                    index=1
                    while(True):
                        found=0
                        for res in self.reservations:
                            if res.reservation_ID==index:
                               found=1

                        if found==0:
                            break
                        index=index+1

                    newReserve = Reservation(index,r.room_id,customer.customer_id)

                    cursor = connection.cursor()
                    cursor.execute("select count(*) from payment")
                    totalc=cursor.fetchone()[0]

                    self.totalpayements=totalc+1

                    pay= Payment(self.totalpayements,customer.customer_id,customer.name,r.room_price,"Not Paid",f"Booked Room: {r.room_id}")
                    self.payments.append(pay)
                    self.reservations.append(newReserve)

                    cursor = connection.cursor()
                    query = """INSERT INTO reservation (reservation_ID,room_ID,cust_ID,date_Added) VALUES (%s, %s,%s,%s)"""
                    row = (newReserve.reservation_ID,newReserve.room_ID,newReserve.cust_ID,newReserve.Data_Added)
                    cursor.execute(query, row)
                    connection.commit()

                    cursor = connection.cursor()
                    query = """INSERT INTO payment (payment_id,cust_id,cust_name,total,Description,status,DateAdd) VALUES (%s, %s,%s,%s,%s,%s,%s)"""
                    row = (pay.payment_id,pay.cust_id,pay.cust_name,pay.total,pay.desc,pay.status,pay.Date)
                    cursor.execute(query, row)
                    connection.commit()


                    print("Room booked successfully : ")
                    return 1
                else:
                    print("That rpoom is already booked : ")
            else:
                print("That room does not exist : ")
        else:
            return 0
        return 0


    def addPayment(self,customer,serv):
        self.totalpayements = self.totalpayements + 1
        pay = Payment(self.totalpayements, customer.customer_id, serv.charge, "Not Paid", serv.description)
        self.payments.append(pay)

    def printAllRooms(self):
        for r in self.rooms:
            r.displayRoom()

    def printAvailableRooms(self):
        for r in self.rooms:
            if r.status == False:
                r.display()
                print("Yes")

    def printAllPayments(self):
        for p in self.payments:
            p.displayPayment()


    def printAllReservations(self):
        for res in self.reservations:
            res.printDetails()

    def getReservation(self,custID,roomID):
        for res in self.reservations:
            if res.cust_ID==custID and res.room_ID==roomID:
                return res


    def custCheckOut(self,cust):

        for allpay in self.payments:
            if allpay.cust_id == cust.customer_id:
                allpay.status="Paid"

        r=h.getRoom(h,cust.room_id)
        r.status=False
        h.reservations.remove(h.getReservation(h,cust.customer_id,r.room_id))
        h.customers.remove(cust)

    def getTotal(self,cust):
        total = 0
        for allpay in self.payments:
            if allpay.cust_id == cust.customer_id and allpay.cust_name==cust.name and allpay.status=="Not Paid":
                total = total + allpay.total
        return total

    def extra(self):
        sql_select_Query = "select * from Room"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        data = cursor.fetchall()
        for r in data:
            r = Room(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
            h.rooms.append(r)

        sql_select_Query = "select * from Employee"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        data = cursor.fetchall()
        for e in data:
            e = Employee(e[0], e[1], e[2], e[3], e[4], e[5])
            h.employees.append(e)

        sql_select_Query = "select * from Customer"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        data = cursor.fetchall()
        for c in data:
            c = Customer(c[0], c[1], c[2], c[3], c[4], c[5])
            h.customers.append(c)


        sql_select_Query = "select * from reservation"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        data = cursor.fetchall()
        for res in data:
            room=Reservation
            room.reserve(room,res[0], res[1], res[2], res[3])
            h.reservations.append(room)


        sql_select_Query = "select * from payment"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        data = cursor.fetchall()
        for payEntry in data:
            pay1=Payment
            pay1.pay(pay1,payEntry[0], payEntry[1], payEntry[2], payEntry[3], payEntry[5], payEntry[4], payEntry[6])
            h.payments.append(pay1)


    def checkAdminInfo(id, password):
        if id=="Admin" and password=="1234":
            return 1
        return 0



h=Hotel
h.extra(h)


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')


@app.route("/loginowner")
def owner_login():
    return render_template("loginowner.html")

@app.route("/admin", methods=['POST', 'GET'])
def owner_main():
    if request.method == 'POST':
        ID = request.form['ID']
        password = request.form['pass']
        if h.checkAdminInfo(ID,password)==1:
            return render_template("Admin/admin.html")
        else:
            return render_template("loginowner.html")
    else:
        return render_template("loginowner.html")

@app.route("/addroom",methods=['POST', 'GET'])
def AdminAddRoom():
    return render_template("Admin/add_room.html")

@app.route("/checkNewRoom", methods=['POST', 'GET'])
def newRoomCheck():
    if request.method == 'POST':
        rID = int(request.form['room_ID'])
        rType = request.form['room_type']
        rPrice = int(request.form['room_price'])
        rDesc = request.form['room_description']
        rFloor = int(request.form['room_floor'])
        rWing = request.form['room_wing']
        if h.addRoom(h,rID,rType,rPrice,rDesc,rFloor,rWing)==1:
            cursor = connection.cursor()
            query = """INSERT INTO Room (room_id, room_type,room_price,room_description,room_floor,room_wing,Status) VALUES (%s, %s,%s,%s,%s,%s,%s)"""
            row = (rID, rType, rPrice, rDesc, rFloor, rWing, 'False')
            cursor.execute(query, row)
            connection.commit()
            return render_template("Admin/admin.html")
    return render_template("Admin/add_room.html")


@app.route("/addemp")
def AdminAddEmp():
    return render_template("Admin/addemp.html")


@app.route("/checkNewEmployee", methods=['POST', 'GET'])
def checkNewEmployee():
    if request.method == 'POST':
        eID = int(request.form['emp_id'])
        name = request.form['emp_name']
        address = request.form['emp_add']
        phone = request.form['emp_phone']
        salary = int(request.form['emp_sal'])
        job = request.form['emp_job']
        if h.addEmployee(h,eID,name,address,phone,job,salary)==1:
            cursor = connection.cursor()
            query = """INSERT INTO Employee (emp_id, emp_name,emp_address,emp_phone,emp_salary,emp_jobtype) VALUES (%s, %s,%s,%s,%s,%s)"""
            row = (eID, name, address, phone, salary, job)
            cursor.execute(query, row)
            connection.commit()
            return render_template("Admin/admin.html")

    return render_template("Admin/addemp.html")


@app.route("/change_emp_job")
def AdminChangeEmpJob():
    return render_template("Admin/change_emp_job.html")

@app.route("/checkAndChangeJob", methods=['POST', 'GET'])
def checkandChangeEmpJob():
    if request.method == 'POST':
        eID = int(request.form['emp_id'])
        jobType = request.form['emp_jobtype']
        if h.updateEmpJob(h,eID,jobType)==1:
            cursor = connection.cursor()
            query = """UPDATE employee set emp_jobtype= %s where emp_id= %s"""
            row = (jobType,eID)
            cursor.execute(query, row)
            connection.commit()
            return render_template("Admin/admin.html")
    return render_template("Admin/change_emp_job.html")

@app.route("/change_emp_sal")
def AdminChangeEmpSal():
    return render_template("Admin/change_emp_salary.html")


@app.route("/checkAndChangeEmpSal", methods=['POST', 'GET'])
def checkAndChangeEmpSal():
    if request.method == 'POST':
        eID = int(request.form['emp_id'])
        sal = int(request.form['emp_salary'])
        if h.updateEmpsal(h,eID,sal)==1:
            cursor = connection.cursor()
            query = """UPDATE employee set emp_salary= %s where emp_id= %s"""
            row = (sal, eID)
            cursor.execute(query, row)
            connection.commit()
            return render_template("Admin/admin.html")
    return render_template("Admin/change_emp_salary.html")

@app.route("/change_room_price")
def AdminChangeRoomPrice():
    return render_template("Admin/change_room_price.html")


@app.route("/checkAndChangeRoomPrice", methods=['POST', 'GET'])
def CheckAndChangeRoomPrice():
    if request.method == 'POST':
        rID = int(request.form['room_id'])
        newPrice = int(request.form['room_price'])
        if h.updateRoom(h,rID,newPrice)==1:
            cursor = connection.cursor()
            query = """UPDATE room set room_price= %s where room_id= %s"""
            row = (newPrice, rID)
            cursor.execute(query, row)
            connection.commit()
            return render_template("Admin/admin.html")
    return render_template("Admin/change_room_price.html")



@app.route("/delete_emp")
def AdminDelEmp():
    return render_template("Admin/delemp.html")


@app.route("/checkAndDeleteEmp", methods=['POST', 'GET'])
def checkAndDeleteEmp():
    if request.method == 'POST':
        eID = int(request.form['emp_id'])
        if h.deleteEmp(h,eID)==1:
            cursor = connection.cursor()
            query = """Delete from employee where emp_id = %s"""
            row = (eID,)
            cursor.execute(query, row)
            connection.commit()
            return render_template("Admin/admin.html")
    return render_template("Admin/delemp.html")


@app.route("/delete_room")
def AdminDeleteRoom():
    return render_template("Admin/delete_room.html")

@app.route("/checkAndDeleteRoom", methods=['POST', 'GET'])
def checkAndDeleteRoom():
    if request.method == 'POST':
        rID = int(request.form['room_id'])
        if h.deleteRoom(h,rID)==1:
            cursor = connection.cursor()
            query = """Delete from room where room_id = %s"""
            row = (rID,)
            cursor.execute(query, row)
            connection.commit()
            return render_template("Admin/admin.html")

    return render_template("Admin/delete_room.html")


@app.route("/disp_cust")
def AdminDisplayCust():
    return render_template("Admin/disp_customers.html",data=h.customers)

@app.route("/disp_pays")
def AdminDispPays():
    return render_template("Admin/disp_pay.html",data=h.payments)

@app.route("/disp_revs")
def AdminDisplayRev():
    return render_template("Admin/disp_reserv.html",data=h.reservations)

@app.route("/disp_rooms")
def AdminDisplayRooms():
    return render_template("Admin/disp_rooms.html",data=h.rooms)

@app.route("/disp_emps")
def AdminDisplayEmps():
    return render_template('Admin/display_emp.html', data=h.employees)

# ========================================================================================================
# ========================================================================================================
# TODO : customer pages
@app.route("/loginresident")
def customer_login():
    return render_template("loginresident.html")

@app.route("/signupSuccess", methods=['POST','GET'])
def newcustomerCheck():
    if request.method == 'POST':
        cID = request.form['ID']
        name = request.form['custName']
        age = int(request.form['age'])
        add = request.form['address']
        phone = request.form['phone']
        password = request.form['password']
        if h.addCustomer(h,cID,name,age,add,phone,password)==1:
            cursor = connection.cursor()
            query="""INSERT INTO Customer (customer_id, password,name,age,Address,phone_no,room_id) VALUES (%s, %s,%s,%s,%s,%s,%s)"""
            row=(cID,password,name,age,add,phone,-1)
            cursor.execute(query,row)
            connection.commit()
            return render_template("loginresident.html")

    return render_template("signup.html")


@app.route("/resident", methods=['POST', 'GET'])
def resident_main():
    if request.method == 'POST':
        ID = int(request.form['ID'])
        password = request.form['pass']
        global a
        a= h.checkLoginCustomer(h,ID,password)
        if a.customer_id!=-1:
            return render_template("resident/resident.html",data=a)
        else:
            return render_template("loginresident.html")
    else:
        return render_template("loginresident.html")

@app.route("/disp_available_rooms")
def DispAvailRooms():
    return render_template("resident/disp_available_rooms.html",data=h.rooms)

@app.route("/book_room")
def BookRoom():
    return render_template("resident/book_room.html")


@app.route("/checkAndBookRoom", methods=['POST', 'GET'])
def checkAndBookRoom():
    if request.method == 'POST':
        rID = int(request.form['room_id'])
        if h.bookRoom(h, a, rID) == 1:
            return render_template("resident/resident.html")
    return render_template("resident/book_room.html")


@app.route("/avail_services")
def AvailServices():
    return render_template("resident/avail_service.html")



@app.route("/checkAndAvailService", methods=['POST', 'GET'])
def checkAndAvailService():
    if request.method == 'POST':
        sID = int(request.form['service_choice'])
        if sID==1:
            return render_template("resident/foodService.html")
        elif sID==2:
            return render_template("resident/Laundry.html")
        elif sID==3:
            serv=ServicesFactory
            serv.availService(serv, 3, sID)
            cursor = connection.cursor()
            cursor.execute("select count(*) from payment")
            totalc = cursor.fetchone()[0]
            h.totalpayements = totalc + 1

            pay = Payment(h.totalpayements, a.customer_id, a.name, serv.charge, "Not Paid", serv.description)
            h.payments.append(pay)

            cursor = connection.cursor()
            query = """INSERT INTO payment (payment_id,cust_id,cust_name,total,status,Description,DateAdd) VALUES (%s, %s,%s,%s,%s,%s,%s)"""
            row = (pay.payment_id, pay.cust_id, pay.cust_name, pay.total, pay.status, pay.desc, pay.Date)
            cursor.execute(query, row)
            connection.commit()
            return render_template("resident/resident.html")
            return render_template("resident/Laundry.html")
    return render_template("resident/avail_service.html")


def orderLaundry():
    return render_template("resident/Laundry")

@app.route("/OrderLaundry", methods=['POST', 'GET'])
def checkAndlaundry():
    if request.method == 'POST':
        sID = int(request.form['service_choice'])
        serv = ServicesFactory
        if sID>0:
            serv.availService(serv,2,sID)
            cursor = connection.cursor()
            cursor.execute("select count(*) from payment")
            totalc = cursor.fetchone()[0]
            h.totalpayements = totalc + 1

            pay = Payment(h.totalpayements, a.customer_id, a.name, serv.charge, "Not Paid", serv.description)
            h.payments.append(pay)

            cursor = connection.cursor()
            query = """INSERT INTO payment (payment_id,cust_id,cust_name,total,status,Description,DateAdd) VALUES (%s, %s,%s,%s,%s,%s,%s)"""
            row = (pay.payment_id, pay.cust_id, pay.cust_name, pay.total, pay.status, pay.desc, pay.Date)
            cursor.execute(query, row)
            connection.commit()
            return render_template("resident/resident.html")
    return render_template("resident/avail_service.html")

def Orderfood():
    return render_template("resident/foodService.html")

@app.route("/OrderFood", methods=['POST', 'GET'])
def checkAndFood():
    if request.method == 'POST':
       sID = int(request.form['service_choice'])
       serv = ServicesFactory

       if sID>0 and sID<=3:
           if sID==1:
                serv=a.Avail_Service(1,1)
           elif sID==2:
                serv = a.Avail_Service(1, 2)
           elif sID==3:
                serv = a.Avail_Service(1, 3)

           cursor = connection.cursor()
           cursor.execute("select count(*) from payment")
           totalc = cursor.fetchone()[0]
           h.totalpayements = totalc + 1

           pay = Payment(h.totalpayements, a.customer_id, a.name, serv.charge, "Not Paid",serv.description)
           h.payments.append(pay)

           cursor = connection.cursor()
           query = """INSERT INTO payment (payment_id,cust_id,cust_name,total,status,Description,DateAdd) VALUES (%s, %s,%s,%s,%s,%s,%s)"""
           row = (pay.payment_id, pay.cust_id, pay.cust_name, pay.total, pay.status, pay.desc, pay.Date)
           cursor.execute(query, row)
           connection.commit()
           return render_template("resident/resident.html")
    return render_template("resident/avail_service.html")




@app.route("/print_details")
def PrintDetails():
    return render_template("resident/print_details.html",data=a)

@app.route("/checkout")
def CheckOut():
    total=h.getTotal(h,a)
    return render_template("resident/checkout.html",data=total)

@app.route("/checkAndCheckOut", methods=['POST', 'GET'])
def checkAndCheckOut():
    if request.method == 'POST':
        confirm = request.form['conf']
        if confirm=='Yes':
            room=a.room_id
            cursor = connection.cursor()
            query = """UPDATE room set status= 'False' where room_id= %s"""
            row = (room,)
            cursor.execute(query, row)
            connection.commit()

            cursor = connection.cursor()
            query = """UPDATE payment set status= 'Paid' where cust_id= %s and cust_name=%s"""
            row = (a.customer_id,a.name)
            cursor.execute(query, row)
            connection.commit()

            cursor = connection.cursor()
            query = """Delete from reservation where cust_id= %s"""
            row = (a.customer_id,)
            cursor.execute(query, row)
            connection.commit()


            cursor = connection.cursor()
            query = """Delete from customer where customer_id= %s"""
            row = (a.customer_id,)
            cursor.execute(query, row)
            connection.commit()

            h.custCheckOut(h,a)
            return render_template("index.html")
    return render_template("resident/resident.html")

# ========================================================================================================
# ========================================================================================================
# TODO : signup pages
@app.route("/signup")
def cust_signup():
    return render_template("signup.html")



if __name__ == "__main__":
    app.run(debug=True)




if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
