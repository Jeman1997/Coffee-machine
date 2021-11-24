#1.50$-Expresso= 50ml water+18g coffee
#2.50$-Latte=200ml water+ 24g coffee+ 150ml milk
#3.00$-Cappuccino= 250ml water+24g coffee + 100ml milk
#Initial resources- 200ml w, 200m milk, 100g compile
#coins- penny-1cent, dime-10cents, nickel-5cents, quarter-25cents
#            -0.01$,     -0.10$,         -0.05$          -0.25$

def coffmach():
    prods=[{'n':'espresso','mk':{'water':50,'cpowd':18,'milk':0},'pr':1.50},{'n':'Latte','mk':{'water':200,'cpowd':24,'milk':150},'pr':2.50},{'n':'cappuccino','mk':{'water':250,'milk':100,'cpowd':24},'pr':3.00}]
    resrcs={'water':300,'cpowd':100,'milk':200}
    bought={'espressos bought':0,"Lattes bought":0,'cappuccinos bought':0}
    cashbox=0
    coins={'penny':0.01,'dime':0.10,'nickel':0.05,'quarter':0.25}
    
    run=True
    while run:
        custwant=input("Want to do like to have?(espresso or latte or Cappuccino)\n*To print report type 'resource report'\n")
        def resch(n):
            resrcs['water']-=prods[n]['mk']['water']
            resrcs['cpowd']-=prods[n]['mk']['cpowd']
            resrcs['milk']-=prods[n]['mk']['milk']   
        if custwant.lower()=='espresso':
            if resrcs['water']<prods[0]['mk']['water']:
                print('no enough water.\nTurning off..')
                print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
                return
            elif resrcs['cpowd']<prods[0]['mk']['cpowd']:
                print("no enough coffee.\nTurning off..")
                print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
                return
            elif resrcs['milk']<prods[0]['mk']['milk']:
                print("no enough milk.\nTurning off..")
                print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
                return
            cash={'p':float(input("Enter cash:\npennies:\n")),'n':float(input('nickels:\n')),'d':float(input('dimes:\n')),'q':float(input('quarters:\n'))}
            s=(coins['penny']*cash['p'])+(coins['nickel']*cash['n'])+(coins['dime']*cash['d'])+(coins['quarter']*cash['q'])
            if s>prods[0]['pr']:
                print(f"Here's the change:{s-prods[0]['pr']}$\nEnjoy the Espresso!")
                cashbox=cashbox+(s-(s-prods[0]['pr']))
                bought['espressos bought']+=1
                resch(0)
            elif s==prods[0]['pr']:
                print(f"Thank You!\nEnjoy the Espresso!") 
                cashbox=cashbox+(s-(prods[0]['pr']-s))
                bought['espressos bought']+=1
                resch(0)
            else:
                print(f'Not enough mondy.Money refunded.')
                coffmach()
        elif custwant.lower()=='latte':
            if resrcs['water']<prods[1]['mk']['water']:
                print('no enough water.\nTurning off..')
                print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
                return
            elif resrcs['cpowd']<prods[1]['mk']['cpowd']:
                print("no enough coffee.\nTurning off..")
                print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
                return
            elif resrcs['milk']<prods[1]['mk']['milk']:
                print("no enough milk.\nTurning off..")
                print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
                return
            cash={'p':float(input("Enter cash:\npennies:\n")),'n':float(input('nickels:\n')),'d':float(input('dimes:\n')),'q':float(input('quarters:\n'))}
            s=(coins['penny']*cash['p'])+(coins['nickel']*cash['n'])+(coins['dime']*cash['d'])+(coins['quarter']*cash['q'])
            if s>prods[1]['pr']:
                print(f"Here's the change:{s-prods[1]['pr']}$\nEnjoy the Latte!")
                cashbox=cashbox+(s-(s-prods[1]['pr']))
                bought['Lattes bought']+=1
                resch(1)
            elif s==prods[1]['pr']:
                print(f"Thank You!\nEnjoy the Latte!") 
                cashbox=cashbox+(s-(prods[1]['pr']-s))
                bought['Lattes bought']+=1
                resch(1)
            else:
                print(f'Not enough mondy.Money refunded.')
                coffmach()
        elif custwant.lower()=='cappuccino':
            if resrcs['water']<prods[2]['mk']['water']:
                print('no enough water.\nTurning off..')
                print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
                return
            elif resrcs['cpowd']<prods[2]['mk']['cpowd']:
                print("no enough coffee.\nTurning off..")
                print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
                return
            elif resrcs['milk']<prods[2]['mk']['milk']:
                print("no enough milk.\nTurning off..")
                print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
                return
            cash={'p':float(input("Enter cash:\npennies:\n")),'n':float(input('nickels:\n')),'d':float(input('dimes:\n')),'q':float(input('quarters:\n'))}
            s=(coins['penny']*cash['p'])+(coins['nickel']*cash['n'])+(coins['dime']*cash['d'])+(coins['quarter']*cash['q'])
            if s>prods[2]['pr']:
                print(f"Here's the change:{s-prods[2]['pr']}$\nEnjoy the Cappuccino!")
                cashbox=cashbox+(s-(s-prods[2]['pr']))
                bought['cappuccinos bought']+=1
                resch(2)
            elif s==prods[2]['pr']:
                print(f"Thank You!\nEnjoy the Cappuccino!") 
                cashbox=cashbox+(s-(prods[2]['pr']-s))
                bought['cappuccinos bought']+=1
                resch(2)
            else:
                print(f'Not enough mondy.Money refunded.')
                coffmach()
        elif custwant.lower()=='resource report':
            print(f'resources:\nWater:{resrcs["water"]}\nCoffee:{resrcs["cpowd"]}\nMilk:{resrcs["milk"]}\nespressos bought:{bought["espressos bought"]}\nlattes bought:{bought["Lattes bought"]}\ncappuccinos bought:{bought["cappuccinos bought"]}\ncash in machine: {cashbox}')
        elif custwant.lower()=='off':
            return
coffmach()