from selenium import webdriver
import pyautogui,time
import turtle 




driver=webdriver.Chrome(r'C:\chromedriver.exe')
#driver.get('https://www.youtube.com/c/PhysicsWallah/featured')

#NCERT MATHS CLASS 11

chap1m='https://ncert.nic.in/ncerts/l/kemh101.pdf'

chap2='https://ncert.nic.in/ncerts/l/kemh102.pdf'

chap3='https://ncert.nic.in/ncerts/l/kemh103.pdf'

chap4='https://ncert.nic.in/ncerts/l/kemh104.pdf'

chap5='https://ncert.nic.in/ncerts/l/kemh105.pdf'

chap6='https://ncert.nic.in/ncerts/l/kemh106.pdf'

chap7='https://ncert.nic.in/ncerts/l/kemh107.pdf'

chap8='https://ncert.nic.in/ncerts/l/kemh108.pdf'

chap9='https://ncert.nic.in/ncerts/l/kemh109.pdf'

chap10='https://ncert.nic.in/ncerts/l/kemh110.pdf'

chap11='https://ncert.nic.in/ncerts/l/kemh111.pdf'

chap12='https://ncert.nic.in/ncerts/l/kemh112.pdf'

chap13='https://ncert.nic.in/ncerts/l/kemh113.pdf'

chap14='https://ncert.nic.in/ncerts/l/kemh114.pdf'

chap15='https://ncert.nic.in/ncerts/l/kemh115.pdf'

chap16='https://ncert.nic.in/ncerts/l/kemh116.pdf'

#NCERT MATHS CLASS 12

chap1m12='https://ncert.nic.in/ncerts/l/lemh101.pdf'

chap2m12='https://ncert.nic.in/ncerts/l/lemh102.pdf'

chap3m12='https://ncert.nic.in/ncerts/l/lemh103.pdf'

chap4m12='https://ncert.nic.in/ncerts/l/lemh104.pdf'

chap5m12='https://ncert.nic.in/ncerts/l/lemh105.pdf'

chap6m12='https://ncert.nic.in/ncerts/l/lemh106.pdf'

chap7m12='https://ncert.nic.in/ncerts/l/lemh201.pdf'

chap8m12='https://ncert.nic.in/ncerts/l/lemh202.pdf'

chap9m12='https://ncert.nic.in/ncerts/l/lemh203.pdf'

chap10m12='https://ncert.nic.in/ncerts/l/lemh204.pdf'

chap11m12='https://ncert.nic.in/ncerts/l/lemh205.pdf'

chap12m12='https://ncert.nic.in/ncerts/l/lemh206.pdf'

chap13m12='https://ncert.nic.in/ncerts/l/lemh207.pdf'

#NCERT PHYSICS CLASS 11

chap1p='https://ncert.nic.in/ncerts/l/keph101.pdf'

chap2p='https://ncert.nic.in/ncerts/l/keph102.pdf'

chap3p='https://ncert.nic.in/ncerts/l/keph103.pdf'

chap4p='https://ncert.nic.in/ncerts/l/keph104.pdf'

chap5p='https://ncert.nic.in/ncerts/l/keph105.pdf'

chap6p='https://ncert.nic.in/ncerts/l/keph106.pdf'

chap7p='https://ncert.nic.in/ncerts/l/keph107.pdf'

chap8p='https://ncert.nic.in/ncerts/l/keph108.pdf'

chap9p='https://ncert.nic.in/ncerts/l/keph201.pdf'

chap10p='https://ncert.nic.in/ncerts/l/keph202.pdf'

chap11p='https://ncert.nic.in/ncerts/l/keph203.pdf'

chap12p='https://ncert.nic.in/ncerts/l/keph204.pdf'

chap13p='https://ncert.nic.in/ncerts/l/keph205.pdf'

chap14p='https://ncert.nic.in/ncerts/l/keph206.pdf'

chap15p='https://ncert.nic.in/ncerts/l/keph207.pdf'

#NCERT PHYSICS CLASS 12

chap1p12='https://ncert.nic.in/ncerts/leph101.pdf'

chap2p12='https://ncert.nic.in/ncerts/leph102.pdf'

chap3p12='https://ncert.nic.in/ncerts/leph103.pdf'

chap4p12='https://ncert.nic.in/ncerts/leph104.pdf'

chap5p12='https://ncert.nic.in/ncerts/leph105.pdf'

chap6p12='https://ncert.nic.in/ncerts/leph106.pdf'

chap7p12='https://ncert.nic.in/ncerts/leph201.pdf'

chap8p12='https://ncert.nic.in/ncerts/leph202.pdf'

chap9p12='https://ncert.nic.in/ncerts/leph203.pdf'

chap10p12='https://ncert.nic.in/ncerts/leph204.pdf'

chap11p12='https://ncert.nic.in/ncerts/leph205.pdf'

chap12p12='https://ncert.nic.in/ncerts/leph206.pdf'

chap13p12='https://ncert.nic.in/ncerts/l/leph207.pdf'

chap14p12='https://ncert.nic.in/ncerts/l/leph208.pdf'

chap15p12='https://ncert.nic.in/ncerts/l/leph209.pdf'


#NCERT CHEMISTRY CLASS 11


chap1c='https://ncert.nic.in/ncerts/l/kech101.pdf'

chap2c='https://ncert.nic.in/ncerts/l/kech102.pdf'

chap3c='https://ncert.nic.in/ncerts/l/kech103.pdf'

chap4c='https://ncert.nic.in/ncerts/l/kech104.pdf'

chap5c='https://ncert.nic.in/ncerts/l/kech105.pdf'

chap6c='https://ncert.nic.in/ncerts/l/kech106.pdf'

chap7c='https://ncert.nic.in/ncerts/l/kech107.pdf'

chap8c='https://ncert.nic.in/ncerts/l/kech201.pdf'

chap9c='https://ncert.nic.in/ncerts/l/kech202.pdf'

chap10c='https://ncert.nic.in/ncerts/l/kech203.pdf'

chap11c='https://ncert.nic.in/ncerts/l/kech204.pdf'

chap12c='https://ncert.nic.in/ncerts/l/kech205.pdf'

chap13c='https://ncert.nic.in/ncerts/l/kech206.pdf'

chap14c='https://ncert.nic.in/ncerts/l/kech207.pdf'


# NCERT CLASS 12 CHEMSITRY

chap1c12='https://ncert.nic.in/ncerts/l/lech101.pdf'

chap2c12='https://ncert.nic.in/ncerts/l/lech102.pdf'

chap3c12='https://ncert.nic.in/ncerts/l/lech103.pdf'

chap4c12='https://ncert.nic.in/ncerts/l/lech104.pdf'

chap5c12='https://ncert.nic.in/ncerts/l/lech105.pdf'

chap6c12='https://ncert.nic.in/ncerts/l/lech106.pdf'

chap7c12='https://ncert.nic.in/ncerts/l/lech107.pdf'

chap8c12='https://ncert.nic.in/ncerts/l/lech108.pdf'

chap9c12='https://ncert.nic.in/ncerts/l/lech109.pdf'

chap10c12='https://ncert.nic.in/ncerts/l/lech201.pdf'

chap11c12='https://ncert.nic.in/ncerts/l/lech202.pdf'

chap12c12='https://ncert.nic.in/ncerts/l/lech203.pdf'

chap13c12='https://ncert.nic.in/ncerts/l/lech204.pdf'

chap14c12='https://ncert.nic.in/ncerts/l/lech205.pdf'

chap15c12='https://ncert.nic.in/ncerts/l/lech206.pdf'

chap16c12='https://ncert.nic.in/ncerts/l/lech207.pdf'




#class 11
chemistry='https://ncert.nic.in/textbook.php?kech1=0-7'
physics='https://ncert.nic.in/textbook.php?keph1=0-8'
maths='https://ncert.nic.in/textbook.php?kemh1=0-16'

#class 11 part-2
chemistry2='https://ncert.nic.in/textbook.php?kech2=0-7'
physics2='https://ncert.nic.in/textbook.php?keph2=0-7'


#class 12 
chemistry12='https://ncert.nic.in/textbook.php?lech1=0-9'
physics12='https://ncert.nic.in/textbook.php?leph1=0-8'
maths12='https://ncert.nic.in/textbook.php?lemh1=0-6'

#class 12 part-2
chemistry122='https://ncert.nic.in/textbook.php?lech2=0-7'
physics122='https://ncert.nic.in/textbook.php?leph2=0-6'
maths122='https://ncert.nic.in/textbook.php?lemh2=0-7'

nta_test='https://nta.ac.in/quiz'
jee_adv_questions='https://jeeadv.ac.in/pastqp.php'

dataset={"chem":chemistry,"phy":physics,"math":maths,"chem2":chemistry2,"phy2":physics2," chem12 ":chemistry12,"phy12":physics12,"math12":maths12}


time.sleep(4)

print('FOR CHEMISTRY USE => chem ')
print('FOR PHYSICS USE => phy')
print('FOR MATHEMATICS USE => math')
print('FOR CHEMISTRY PART 2 USE => chem2 ')
print('FOR PHYSICS PART 2 USE => phy2')
print('FOR CHEMISTRY OF X|| USE => chem12 ')
print('FOR PHYSICS OF X|| USE=> phy12')
print('FOR MATHEMATICS OF X|| USE => math12')
print("FOR MOCK TEST USE =>test ")
print("FOR PYQs USE => jee")
print("FOR JEE MAIN CHAPTER WISE QUESTIONS USE => maintopic")
print("FOR JEE ADVANCED CHAPTER WISE QUESTIONS USE => advtopic")
print("FOR JEE MAIN YEAR WISE QUESTIONS USE =>mainyear")
print("FOR JEE ADVANCED YEAR WISE QUESTIONS USE => advyear ")
print("FOR PHYSICS FORMULA SHEET USE => cheatsheet")
print("TO VISIT JEE MAIN SITE USE => mainsite")
print("TO VISIT JEE ADVANCED SITE USE => advsite")
print("FOR REACTION MECHANISM DPP USE => gocdpp")
print("WRITE 1st WORD OF ANY CHAPTER AND GET ITS PDF")
print("FOR D BLOCK AND F BLOCK ELEMENTS USE=>dfblock ")
print("TO VISIT FLIPKART USE=> flipkart")
print("TO VISIT AMAZON USE => amazon")
print("FOR INTRODUCTION TO 3D GEOMETRY USE =>3dgeometry")
print("FOR FUNCTIONS AND RELATIONS OF X|| USE => relations2  ")
print("FOR APPLICATION OF INTEGRALS USE => applicationi")
print("FOR APPLICATION OF DERAVITIVES USE => applicationd")
print("FOR 3 DIMENSIONAL GEOMETRY USE =>three")
print("FOR THERMODYNAMICS OF PHYSICS USE =>thermodynamics1 ")
print("FOR THERMODYNAMICS OF CHEMISTRY USE =>thermodynamics2")
print("FOR ISOLATION OF ELEMENTS USE => general")
print("FOR P BLOCK OF X|| USE => pblock12")
print("FOR MECHANICAL PROPERTIES OF FLUIDS USE =>mechanicalf ")
print("FOR MECHANICAL PROPERTIES OF SOLIDS USE=>mechanicals")
print("FOR SPOTIFY LOGIN USE => spotify")
print("FOR AMAZON USE => amazon")
print("FOR FLIPKART USE=> flipkart")
print("FOR SONGS USE => songs")










while True:
    choice=input('choose options from the list below : ')

    if choice=="chem":
        driver.get(chemistry)
    elif choice=="phy":
        driver.get(physics)
    elif choice=="math":
        driver.get(maths)
    elif choice=="phy2":
        driver.get(physics2)
    elif choice=="chem2":
        driver.get(chemistry2)
    elif choice=="phy12":
        driver.get(physics12)
    elif choice=="chem12":
        driver.get(chemistry12)
    elif choice=="math12":
        driver.get(maths12)
    elif choice=="math122":
        driver.get(maths122)
    elif choice=="chem122":
        driver.get(chemistry122)
    elif choice=="phy122":
        driver.get(physics122)
    elif choice=="test":
        driver.get(nta_test)
        pyautogui.hotkey('ctrl','t')
        driver.get(nta_test)
    elif choice=="jee":
        driver.get(jee_adv_questions)
        year=driver.find_element_by_xpath('//*[@id="quicklinks"]/div/div/div[1]/div/table/thead/tr[14]/td[2]/a[1]')
        year.click()
    elif choice=="maintopic":
        driver.get('https://questions.examside.com/past-years/jee/jee-main/')
    elif choice=="advtopic":
        driver.get('https://questions.examside.com/past-years/jee/jee-advanced/')
    elif choice=="mainyear":
        driver.get('https://questions.examside.com/past-years/year-wise/jee/jee-main/')
    elif choice=="advyear":
        driver.get('https://questions.examside.com/past-years/year-wise/jee/jee-advanced/')
    elif choice=="formulasheet":
        driver.get('https://drive.google.com/file/d/1aTf4ksFMIFuBc1aadJsc6Ut7h1HcqV-T/view')
    elif choice=="advsite":
        driver.get('https://jeeadv.ac.in/')
    elif choice=="mainsite":
        driver.get('https://jeemain.nta.nic.in/webinfo2021/Page/Page?PageId=1&LangId=P')
    elif choice=="GOCdpp":
        driver.get('https://unacademy.com/lesson/solution-of-dpp-1-reaction-mechanism/SR17NJHL')

#11 Maths
    elif choice=="sets":
        driver.get(chap1m)
    elif choice=="relations1":
        driver.get(chap2)
    elif choice=="trignometric":
        driver.get(chap3)
    elif choice=="principle":
        driver.get(chap4)
    elif choice=="complex":
        driver.get(chap5)
    elif choice=="linear":
        driver.get(chap6)
    elif choice=="permutations":
        driver.get(chap7)
    elif choice=="binomial":
        driver.get(chap8)
    elif choice=="sequence":
        driver.get(chap9)
    elif choice=="straight":
        driver.get(chap10)
    elif choice=="conic":
        driver.get(chap11)
    elif choice=="3dgeometry":
        driver.get(chap12)
    elif choice=="limits":
        driver.get(chap13)  
    elif choice=="mathematical":
        driver.get(chap14)  
    elif choice=="statistics":
        driver.get(chap15)
    elif choice=="probability":
        driver.get(chap16)

#12 Maths

    elif choice=='''relations2''':
        driver.get(chap1m12)

    elif choice=="inverse":
        driver.get(chap2m12)

    elif choice=="matrices":
        driver.get(chap3m12)
    
    elif choice=="determinants":
        driver.get(chap4m12)

    elif choice=="continuity":
        driver.get(chap5m12)

    elif choice=="applicationd":
        driver.get(chap6m12)

    elif choice=="integrals":
        driver.get(chap7m12)

    elif choice=="applicationi":
        driver.get(chap8m12)

    elif choice=="differential":
        driver.get(chap9m12) 

    elif choice=="vectors":
        driver.get(chap10m12) 

    elif choice=="three":
        driver.get(chap11m12) 

    elif choice=="linear":
        driver.get(chap12m12) 

    elif choice=="probability2":
        driver.get(chap13m12) 

#Physics 11

    elif choice=="physical":
        driver.get(chap1p) 

    elif choice=="units":
        driver.get(chap2p) 
    
    elif choice=="straightmotion":
        driver.get(chap3p) 

    elif choice=="planemotion":
        driver.get(chap4p) 

	           
    elif choice=="nlm":
        driver.get(chap5p) 

    elif choice=="work":
        driver.get(chap6p) 

    elif choice=="system":
        driver.get(chap7p) 

    elif choice=="gravitation":
        driver.get(chap8p) 

    elif choice=="mechanicals":
        driver.get(chap9p) 


    elif choice=="mechanicalf":
        driver.get(chap10p) 

    elif choice=="thermal":
        driver.get(chap11p) 

    elif choice=="thermodynamics1":
        driver.get(chap12p) 

    elif choice=="kinetic":
        driver.get(chap12p) 
    
    elif choice=="oscillation":
        driver.get(chap12p) 
    
    elif choice=="waves":
        driver.get(chap12p) 
    

#Physics 12


    elif choice=="electric":
        driver.get(chap1p12) 
    
    elif choice=="electrostatic":
        driver.get(chap2p12) 
    
    elif choice=="current":
        driver.get(chap3p12) 

    elif choice=="moving":
        driver.get(chap4p12) 

    elif choice=="magnetism":
        driver.get(chap5p12) 

    elif choice=="emi" or choice=="electromagneticinduction":
        driver.get(chap6p12) 

    elif choice=="ac" or choice=="alternating":
        driver.get(chap7p12) 
    
    elif choice=="emw" or choice=="electromagnetic":
        driver.get(chap8p12) 
    
    elif choice=="rayoptics" or choice=="optics":
        driver.get(chap9p12) 

    elif choice=="waveoptics":
        driver.get(chap10p12) 

    elif choice=="dual" or choice=="dualnature":
        driver.get(chap11p12) 

    elif choice=="atoms":
        driver.get(chap12p12) 

    elif choice=="nuclei":
        driver.get(chap13p12) 

    elif choice=="semiconductor":
        driver.get(chap14p12) 

    elif choice=="communication" or choice=="communicationsystem":
        driver.get(chap15p12) 
    
    
    
    

#11 CHEMSITRY

    elif choice=="some":
        driver.get(chap1c) 
    
    elif choice=="structure":
        driver.get(chap2c) 

    elif choice=="classification":
        driver.get(chap3c) 

    elif choice=="chemical":
        driver.get(chap4c) 

    elif choice=="states":
        driver.get(chap5c) 

    elif choice=="thermodynamics2":
        driver.get(chap6c) 

    elif choice=="equilibrium":
        driver.get(chap7c) 

    elif choice=="redox":
        driver.get(chap8c) 

    elif choice=="hydrogen":
        driver.get(chap9c) 

    elif choice=="sblock":
        driver.get(chap10c) 

    elif choice=="pblock":
        driver.get(chap11c) 

    elif choice=="organic":
        driver.get(chap12c) 

    elif choice=="hydrocarbons":
        driver.get(chap13c) 

    elif choice=="environmental":
        driver.get(chap14c) 

#12 CHEMISTRY

    elif choice=="thesolidstate" or choice=="solid" or choice=="solidstate":
        driver.get(chap1c12) 
    
    elif choice=="solutions":
        driver.get(chap2c12) 
   
    elif choice=="electrochemistry":
        driver.get(chap3c12) 

    elif choice=="chemical":
        driver.get(chap4c12) 

    elif choice=="surface":
        driver.get(chap5c12) 

    elif choice=="general":
        driver.get(chap6c12) 

    elif choice=="pblock12":
        driver.get(chap7c12) 

    elif choice=="dfblock":
        driver.get(chap8c12) 

    elif choice=="coordination":
        driver.get(chap9c12) 

    elif choice=="haloalkanes":
        driver.get(chap10c12)

    elif choice=="alcohols":
        driver.get(chap11c) 

    elif choice=="aldehydes":
        driver.get(chap12c) 

    elif choice=="amines":
        driver.get(chap13c) 

    elif choice=="biomolecules":
        driver.get(chap14c12)

    elif choice=="polymers":
        driver.get(chap15c12)

        
    elif choice=="everydaylife":
        driver.get(chap16c12) 

    elif choice=="song" or choice=="songs":
        driver.get('https://www.youtube.com/watch?v=mLQsZ8DYP6M&ab_channel=iGadget')

    elif choice=="about":
        driver.get('https://django-website-9f086.web.app/')

    elif choice=="amazon":
        driver.get('https://www.amazon.in/')

    elif choice=="flipkart":
        driver.get('https://www.flipkart.com/')

    elif choice=="spotify":
        driver.get('https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F')

    else:
    
        print("\n ****** PLEASE USE KEYWORDS FROM THE GIVEN LIST ONLY !! *****")





    
    
	                                                                                      
















