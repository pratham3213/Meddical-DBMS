#Project on medical store management
import pickle
import os
import datetime
import math
def showmenu():
	#print("\n"*20)
	print("#"*20,end='')
	print(" SANJEEVANI MEDICAL STORE ",end='')
	print("#"*20,end='')
	print('\n\n')
	print('\t\t\t 1. ADD STOCK ')
	print('\t\t\t 2. UPDATE STOCK ')
	print('\t\t\t 3. DELETE MEDICINE ')
	print('\t\t\t 4. SELL MEDICINE ')
	print('\t\t\t 5. RE-ORDER LIST ')
	print('\t\t\t 6. UPCOMING EXPIRY MEDICINE LIST ')
	print('\t\t\t 7. SALE OF THE DAY ')
	print('\t\t\t 8. MONTHLY REPORT ')
	print('\t\t\t 9. SEARCH MEDICINE ')
	print('\t\t\t 10. EXIT ')
	print('\n'*2)
	print(' '*20,end='')
def checkValidDate(date):
	pos1 = date.index('/')
	pos2 = date.index('/',pos1+1)
	d = int(date[0:pos1])
	m = int(date[pos1+1:pos2])
	y = int(date[pos2+1:])
	if d<0 or d>31:
		return False
	elif m<0 or m>12:
		return False
	elif y<0:
		return False
	else:
		return True
def addStock():
	if os.path.exists('Medicines.dat'):
		f = open('Medicines.dat','r+b')
		medicines = pickle.load(f)
		mid = len(medicines)+1
	else:
		f = open('Medicines.dat','wb')
		medicines=[]
		mid = 1
	print('\n\n\t\t\t Medicine ID :',mid)
	mname = input('\n\n\t\t\t Enter Medicine Name :')
	brand = input('\n\n\t\t\t Enter Brand Name :')
	man_date = input('\n\n\t\t\t Enter Manufacturing Date (DD/MM/YYYY)')
	while not (checkValidDate(man_date)):
		print('\t\t\t ## INVALID DATE ##')
		man_date = input('\n\t\t\t Enter Manufacturing Date (DD/MM/YYYY)')

	exp_date = input('\n\n\t\t\t Enter Expiry Date (DD/MM/YYYY)')
	while not (checkValidDate(man_date)):
		print('\t\t\t ## INVALID DATE ##')
		exp_date = input('\n\n\t\t\t Enter Expiry Date (DD/MM/YYYY)')

	qty = int(input('\n\n\t\t\t Enter Quantity :'))
	type = int(input('\n\n\t\t\t Enter type of medicince (0-Syrup/1-Tablet/Capsule)'))
	qty_per=None
	if type==1:
		qty_per=int(input('\n\n\t\t\t Enter number of tablets per strip :'))
	price = int(input('\n\n\t\t\t Enter Price per strip/bottle :'))
	if type==0:
		amount = qty * price
	else:
		amount = qty/qty_per * price
	print('\n\n\t\t\t TOTAL AMOUNT : ',amount)

	medicines.append([mid,mname,brand,man_date,exp_date,qty,type,qty_per,price,amount])
	f.seek(0,0)
	pickle.dump(medicines,f)
	f.close()
	print('\n\t\t\t ## DATA SAVED ## ')
	key = input('\n\t\t\t\t\t...:::::Press Enter Key...')


def searchMedicine():
	if os.path.exists("Medicines.dat"):
		f = open("Medicines.dat","rb")
	medicines=pickle.load(f)
	print("\n\n\t##################### SEARCH SCREEN ######################")
	n = input('\n\n\t\t ENTER MEDICINE NAME ')
	found=False
	print('%7s'%'MED ID','%15s'%'MEDICINE NAME','%12s'%'EXPIRY DATE','%5s'%'QTY','%10s'%'TYPE','%8s'%'AMOUNT')
	print('-'*80)
	for med in medicines:
		if n.upper() in med[1]:
			print('%7s'%med[0],'%15s'%med[1],'%12s'%med[4],'%5s'%med[5],'%10s'%med[6],'%8s'%med[9])
			found=True
			break
		if not found:
			print('\n\t\t ## MEDICINE NOT FOUND ##')
			f.close()
		else:
			print('\n\t\t ## FILE NOT FOUND ##')
		input('press..')
def updateStock():
	if os.path.exists("Medicines.dat"):
		f = open("Medicines.dat","r+b")
		medicines=pickle.load(f)
		print("\n\n\t##################### UPDATE STOCK SCREEN ######################")
		n = input('\n\n\t\t ENTER MEDICINE NAME (FIRST FEW LETTERS) ')
		found=False
		print('%7s'%'MED ID','%15s'%'MEDICINE NAME','%12s'%'EXPIRY DATE','%5s'%'QTY','%10s'%'TYPE','%8s'%'PRICE','%8s'%'AMOUNT')
		print('-'*80)
		for i in range(len(medicines)):
			
			if n.upper() in medicines[i][1]:
				print('%7s'%medicines[i][0],'%15s'%medicines[i][1],'%12s'%medicines[i][4],'%5s'%medicines[i][5],'%10s'%medicines[i][6],'%8s'%medicines[i][8],'%8s'%medicines[i][9])
				print('\n\n')
				q = int(input('Enter Quantity to Add :'))
				medicines[i][5] = medicines[i][5]+q
				#print(medicines[i][6])
				if medicines[i][6]==0:
					medicines[i][9] = medicines[i][5]*medicines[i][8]
				else:
					medicines[i][9] = (medicines[i][5]/medicines[i][7]) * medicines[i][8]
					print('\n\n## STOCK UPDATED ##')
					found=True
					break
			if not found:
				print('\n\t\t ## MEDICINE NOT FOUND ##')
				f.seek(0,0)
				pickle.dump(medicines,f)
				f.close()
		else:
			print('\n\t\t ## FILE NOT FOUND ##')
		input('press..')

def deleteMedicine():
	if os.path.exists("Medicines.dat"):
		f = open("Medicines.dat","r+b")
		medicines=pickle.load(f)
		print("\n\n\t##################### DELETE MEDICINE SCREEN ######################")
		n = input('\n\n\t\t ENTER MEDICINE NAME (FIRST FEW LETTERS) ')
		found=False
		pos=None
		print('%7s'%'MED ID','%15s'%'MEDICINE NAME','%12s'%'EXPIRY DATE','%5s'%'QTY','%10s'%'TYPE','%8s'%'PRICE','%8s'%'AMOUNT')
		print('-'*80)
		for i in range(len(medicines)):
			if n.upper() in medicines[i][1]:
				print('%7s'%medicines[i][0],'%15s'%medicines[i][1],'%12s'%medicines[i][4],'%5s'%medicines[i][5],'%10s'%medicines[i][6],'%8s'%medicines[i][8],'%8s'%medicines[i][9])
				pos = i
				found=True
				break
			if not found:
				print('\n\t\t ## MEDICINE NOT FOUND ##')
			else:
				ans = input('Are you Sure to delete ?(y)')
				if ans.lower()=='y':
					medicines.pop(pos)
					print('\n# MEDICINE DELETED SUCCESSFULLY#')
			f.seek(0,0)
			pickle.dump(medicines,f)
			f.close()
		else:
			print('\n\t\t ## FILE NOT FOUND ##')
		input('press..')
def getQuantityRate(medicines,mname):
	found=False
	for i in range(len(medicines)):
		if mname.lower() in medicines[i][1].lower():
			pos=i
			found=True
			break
		if found:
			if medicines[pos][6]==0:
				return medicines[pos][5],medicines[pos][8],medicines[pos][6],medicines[pos][1]
			else:
				return medicines[pos][5],medicines[pos][7]/medicines[pos][8],medicines[pos][6],medicines[pos][1]
		else:
			return None

def sellMedicine():
	if os.path.exists("Medicines.dat"):
		f = open("Medicines.dat","r+b")
		medicines=pickle.load(f)
		print('\n\n\t\t################# SELL MEDICINE SCREEN ###################')
		ans='y'
		purchaselist = []
		while ans=='y':
			mn = input('Enter Medicine Name ')
			status = getQuantityRate(medicines,mn)
			if status==None:
				print('Sorry no such medicine')
			else:
				print('Medicine Name :',status[3])
				print('Total Quantity Available :',status[0])
				print('Rate :',status[1])
				q = int(input('Enter Quantity to purchase :'))
				cd = datetime.datetime.now()
				billd = str(cd.day)+'/'+str(cd.month)+'/'+str(cd.year)+''+str(cd.hour)+':'+str(cd.minute)+':'+str(cd.second)
				purchaselist.append([status[3],q,status[1],status[2],billd])
				ans = input('More Medicines (y) ?')
				print('\n\n\t\t ################# BILL INVOICE #######################')
				print('%20s'%'MEDICINE NAME','%10s'%'QUANTITY','%5s'%'TYPE','%10s'%'RATE','%10s'%'AMOUNT')
				print("*********************************************************************")
				total = 0
				for i in range(len(purchaselist)):
					if purchaselist[i][3]==0:
						typep='BOT'
					else:
						typep='TAB/CAP'
					amount = purchaselist[i][1] * purchaselist[i][2]
					print('%20s'%purchaselist[i][0],'%10s'%purchaselist[i][1],'%5s'%typep,'%10s'%round(purchaselist[i][2],2),'%10s'%round(amount,2))
					total+=amount
				print("===================================================================")
				print('\t\t\t\t GRANT TOTAL = ',round(total,2))
				print("===================================================================")
				print("Bill generated on :",billd)
				for p in purchaselist:
					for i in range(len(medicines)):
						if p[0] in medicines[i][1]:
							medicines[i][5] = medicines[i][5]-p[1]
							break
				f.seek(0,0)
				pickle.dump(medicines,f)
				f.close()
				if os.path.exists('Transaction.dat'):
					f2 = open('Transaction.dat','r+b')
					purchase_record = pickle.load(f2)
					f2.seek(0,0)
					purchase_record.append(purchaselist)
					pickle.dump(purchase_record,f2)
					f2.close()
				else:
					f2 = open('Transaction.dat','wb')
					pickle.dump(purchaselist,f2)
					f2.close()
		else:
			print('\n\t## FILE NOT FOUND ##')
		input('press..')


def ReOrderList():
	if os.path.exists("Medicines.dat"):
		f = open("Medicines.dat","r+b")
		medicines=pickle.load(f)
		print("\n\n\t##################### REORDER MEDICINE LIST (QTY<50) ######################")
		print('%7s'%'MED ID','%15s'%'MEDICINE NAME','%12s'%'EXPIRY DATE','%5s'%'QTY','%10s'%'TYPE','%8s'%'PRICE','%8s'%'AMOUNT')
		for med in medicines:
			if med[5]<50:
				print('%7s'%med[0],'%15s'%med[1],'%12s'%med[4],'%5s'%med[5],'%10s'%med[6],'%8s'%med[8],'%8s'%med[9])
			else:
				print('\n\n\t\t ## FILE NOT FOUND ##')


def ExpiryList():
	if os.path.exists("Medicines.dat"):
		f = open("Medicines.dat","r+b")
		medicines=pickle.load(f)
		print("\n\n\t##################### EXPIRY MEDICINE LIST (DATE IS OVER OR <=3 MONTHS) ######################")
		print('%7s'%'MED ID','%15s'%'MEDICINE NAME','%12s'%'EXPIRY DATE','%5s'%'QTY','%10s'%'TYPE','%8s'%'PRICE','%8s'%'AMOUNT')
		cur_date = datetime.datetime.now()
		for med in medicines:
			s = med[4]
			ed = datetime.datetime.strptime(s,'%d/%m/%Y')
			diff = cur_date - ed
			if diff.days>=0 or math.fabs(diff.days/30)<=4:
				print('%7s'%med[0],'%15s'%med[1],'%12s'%med[4],'%5s'%med[5],'%10s'%med[6],'%8s'%med[8],'%8s'%med[9])
			else:
				print('\n\n\t\t ## FILE NOT FOUND ##')


def SaleoftheDay():
	if os.path.exists('Transaction.dat'):
		f = open('Transaction.dat','rb')
		purchases = pickle.load(f)
		d = datetime.datetime.now()
		cur_date = str(d.day)+"/"+str(d.month)+"/"+str(d.year)
		print("TODAY IS : ",cur_date)
		total = 0
		print('%20s'%'MEDICINE NAME	','%10s'%'QUANTITY','%5s'%'TYPE','%10s'%'RATE','%10s'%'AMOUNT')
		print("*********************************************************************")
		for p in purchases:
			pos = p[4].index(' ')
			trans_date = p[4][:pos]
			if cur_date == trans_date:
				amount = p[1]*p[2]
			if p[3]==0:
				types="BOT"
			else:
				types="TAB/CAP"
		print('%20s'%p[0],'%10s'%p[1],'%5s'%types,'%10s'%round(p[2],2),'%10s'%round(amount,2))
		total+=amount
		print('------------------------------------------------------------------')
		print('\t\t\t\t TOTAL AMOUNT FOR DAY = Rs.',total)
		print('------------------------------------------------------------------\n\n')

	else:
		print('\n## FILE NOT FOUND ##')

def MonthlyReport():
	if os.path.exists('Transaction.dat'):
		f = open('Transaction.dat','rb')
		purchases = pickle.load(f)
		d = datetime.datetime.now()

		months=["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
		current_month = months[d.month-1]
		current_year = d.year

		print("REPORT OF : ",current_month,current_year)
		total = 0
		print('%20s'%'MEDICINE NAME','%10s'%'QUANTITY','%5s'%'TYPE','%10s'%'RATE','%10s'%'AMOUNT')
		print("*********************************************************************")
		for p in purchases:
			pos = p[4].index(' ')
			trans_date = p[4][:pos]
			#print(trans_date)
			inds = trans_date.index('/')
			#print(inds)
			inds2 = trans_date.index('/',inds+1)
			#print(inds2)
			mon = trans_date[inds+1:inds2]

			if d.month == int(mon):
				amount = p[1]*p[2]
			if p[3]==0:
				types="BOT"
			else:
				types="TAB/CAP"
		print('%20s'%p[0],'%10s'%p[1],'%5s'%types,'%10s'%round(p[2],2),'%10s'%round(amount,2))
		total+=amount
		print('------------------------------------------------------------------')
		print('\t\t\t\t TOTAL AMOUNT FOR DAY = Rs.',total)
		print('------------------------------------------------------------------\n\n')
	else:
		print('\n## FILE NOT FOUND ##')

choice=0
while choice!=None:
	showmenu()
	choice = int(input('Enter Your Choice :'))
	if choice==1:
		addStock()
	elif choice==9:
		searchMedicine()
	elif choice==2:
		updateStock()
	elif choice==3:
		deleteMedicine()
	elif choice==4:
		sellMedicine()
	elif choice==5:
		ReOrderList()
	elif choice==6:
		ExpiryList()
	elif choice==7:
		SaleoftheDay()
	elif choice==8:
		MonthlyReport()
	elif choice==10:
		print('\n\n\t\t\t\t\t THANK YOU!')
		choice=None
	else:
		print('\n\n\t\t ## PLEASE ENTER VALID CHOICES [1-10] ##')
