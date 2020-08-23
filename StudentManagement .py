# Sinifdeki ushaqlar
# Ad ve qeydiyyat nomreleri


class Student(object):
    def __init__(self, Ad, Soyad, mobil, email):
        self.Ad = Ad
        self.Soyad = Soyad
        self.mobil = mobil
        self.email= email

    def getmobil(self):
        return self.mobil

    def getsoyad(self):
        return self.Soyad 

    def getemail(self):
        return self.email
    
    
    def __str__(self):
        return self.Ad + ' ' +  str(self.getsoyad()) +' :'+  str(self.getmobil()) + ' - ' + str(self.getemail())
  
# funksiyanın təyin edilməsi
# bütün tələbələrin siyahısını yaradır 
def Siyahi(rec, Ad, Soyad, mobil , email):
    rec.append(Student(Ad, Soyad, mobil, email))
    return rec

# Əsas kod
say = 10

userList = []
x = 1
while x <=say:
    Ad = input('Şagirdin adı: ')
    Soyad = input('Soyadı: ')
    Nomre = input('Nömrəsi: ')
    email = input('e-mail address: ')
    userList = Siyahi(userList, Ad, Soyad, Nomre, email)
    x+=1
    #x = input('Növbəti şagird? y/n: ')
    
# Tələbə siyahısının çapı


n = 1
for i in userList:
    print(n,')', i)
    n = n + 1