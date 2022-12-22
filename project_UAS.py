class Warga:
    def _init_(Warga,nama,umur):
        warganama = nama
        wargaumur = umur
    def _str_(warga):
        return f"{warga}({warga})"

p1 = ("Dhani", 19)
p3 = ("Rahma", 20)
p2 = ("Nita", 18)
p5 = ("Ilham",22)
p6 = ("Faqih",17)
p4 = ("Munif",23)
p7 = ("Ayu",19)

print (p1,p2,p3,p4,p5,p6,p7)
#output pertamanya adalah ('Dhani',19)('Nita',18)('Rahma',20)('Munif',23)('Faqih',17)('Ayu',19)



def  pemecah_sukukata4(kata):
    hurufawal2=kata[:2]
    hurufakhir2=kata[2:]
    hasil=hurufawal2+'-'+hurufakhir2
    print('hasil suku kata ' ,hasil)

def  pemecah_sukukata3(kata):
    hurufawal1=kata[:1]
    hurufakhir2=kata[1:]
    hasil=hurufawal1+'-'+hurufakhir2
    print('hasil suku kata' ,hasil)

def  pemecah_sukukata5(kata):  
    hurufakhir=kata[4:]
    print('huruf akhir',hurufakhir)
    nil=test_huruf(hurufakhir)
    if( nil==0): 
        hurufawal3=kata[:3]
        hurufakhir2=kata[3:]
        if(hurufakhir2=="__"):
             hurufawal3=kata[:2]
             hurufakhir2=kata[2:]   
             hasil=hurufawal3+'-'+hurufakhir2
        else : 
            hasil=hurufawal3+'-'+hurufakhir2 
    else:
        if(nil==1):
          hurufawal3=kata[:2]
          hurufakhir2=kata[2:]
          hasil=hurufawal3+'-'+hurufakhir2
    print('hasil suku kata:' ,hasil)


def test_huruf(huruf):
    if(huruf in "aiueo"):
      test_huruf = 0  
    else:
      test_huruf = 1
    return  test_huruf       
      


print('pemecah suku kata  :\n')
print('masukan  kata:')
kata = input()
print('kata yang di input, ' + kata) 
jumlah_karater=len(kata)
print('jumlah karakter, ' , jumlah_karater)

if (jumlah_karater==4):
    pemecah_sukukata4(kata)
else:
    if (jumlah_karater==5):
        pemecah_sukukata5(kata)
    if (jumlah_karater==3):
        pemecah_sukukata3(kata)
#pemecah suku kata 4 outputnya adalah masukan kata:
                                      #nisa
                                      #kata yang di input,nisa
                                      #jumlah karakter, 4
                                      #hasil suku katanya ni-sa
#pemecah suku kata 3 outputnya adalah masukan kata:
                                      #Ayu
                                      #kata yang di input,Ayu
                                      #jumlah karakter,3
                                      #hasil suku katanya A-yu
#pemecah suku kata 5 outputnya adalah masukan kata:
                                      #ilham
                                      #kata yang di input, ilham
                                      #jumlah karakter,5
                                      #huruf akhir m 
                                      #hasil suku kata:il-ham
    #pemecah suku kata 5 outputnya adalah masukan kata:
                                      #kursi 
                                      #kata yang di input,kursi 
                                      #jumlah karakter,5
                                      #huruf akhir i
                                      #hasil suku kata: kur-si
                                    
