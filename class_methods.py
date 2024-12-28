# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 18:33:26 2024

@author: duman
"""

class Yazılımcı():
    
    def __init__(self,isim,soyisim,numara,maaş,diller):
                 self.isim = isim
                 self.soyisim = soyisim
                 self.numara = numara
                 self.maaş = maaş
                 self.diller = diller
                 
    def bilgileri_göster(self):
        print("""
              Yazılımcı objesinin özellikleri
              
              İsim = {}

              Soyisim = {}
              
              Numara = {}
              
              Maşş = {}
              
              Diller = {}
              
              
              """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def zam_yap(self,zam_miktarı):
        print('Zam yapılıyor...')
        self.maaş += zam_miktarı 
    def yeni_dil(self,dil):
        print('Yeni dil')
        self.diller.append(dil)
              
yazılımcı = Yazılımcı('Selahattin','Duman',123,10000,['python','javascript'])

print(yazılımcı.zam_yap(2))

print(yazılımcı.yeni_dil('GoLang'))
print(yazılımcı.bilgileri_göster())