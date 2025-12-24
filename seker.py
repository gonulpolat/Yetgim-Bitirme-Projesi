"""
    Bu modül Seker sınıfını içerir. Seker sınıfı bir tane şekeri temsil eder.
"""

import pygame
from config import *


class Seker:
    '''Her bir şekeri temsil eden sınıf'''
    
    def __init__(self, satir: int, sutun: int, tip: int):
        '''
        satir (int): Izgara üzerindeki satır pozisyonu (0-7)
        sutun (int): Izgara üzerindeki sütun pozisyonu (0-7)
        tip (int): Şekerin tipi (0-5 arası index)
        '''
        self.satir = satir 
        self.sutun = sutun
        self.tip = tip
        self.renk = SEKER_RENKLERI[tip]
        self.sembol = SEKER_SEMBOLLERI[tip]
        
        # Ekrandaki piksel koordinatları (hedef pozisyon)
        self.hedef_x = IZGARA_X + sutun * HUCRE_BOYUTU
        self.hedef_y = IZGARA_Y + satir * HUCRE_BOYUTU
        
        # Mevcut animasyon pozisyonu (başlangıçta hedefle aynı)
        self.x = self.hedef_x
        self.y = self.hedef_y
        
        self.secili = False  # Şeker seçili mi?
        self.animasyon_bitti = True  # Animasyon tamamlandı mı?
    
    def hedef_pozisyon_ayarla(self, yeni_satir: int, yeni_sutun: int):
        '''
        Şekerin yeni hedef pozisyonunu ayarla
        
        Args:
            yeni_satir (int): Yeni satır
            yeni_sutun (int): Yeni sütun
        '''
        self.satir = yeni_satir
        self.sutun = yeni_sutun
        self.hedef_x = IZGARA_X + yeni_sutun * HUCRE_BOYUTU
        self.hedef_y = IZGARA_Y + yeni_satir * HUCRE_BOYUTU
        
        # Eğer pozisyon değiştiyse animasyon başlat
        if self.y != self.hedef_y or self.x != self.hedef_x:
            self.animasyon_bitti = False
    
    def animasyon_guncelle(self):
        '''
        Şekerin düşme animasyonunu güncelle
        
        Returns:
            bool: Animasyon bitti mi?
        '''
        if self.animasyon_bitti:
            return True
        
        # Y ekseni animasyonu için : şekerler aşağı doğru düşer
        if self.y < self.hedef_y:
            self.y += DUSME_HIZI
            if self.y >= self.hedef_y:
                self.y = self.hedef_y
        elif self.y > self.hedef_y:
            self.y -= DUSME_HIZI
            if self.y <= self.hedef_y:
                self.y = self.hedef_y
        
        # X ekseni animasyonu 
        if self.x < self.hedef_x:
            self.x += DUSME_HIZI
            if self.x >= self.hedef_x:
                self.x = self.hedef_x
        elif self.x > self.hedef_x:
            self.x -= DUSME_HIZI
            if self.x <= self.hedef_x:
                self.x = self.hedef_x
        
        # Animasyon tamamlandı mı kontrol et
        if self.x == self.hedef_x and self.y == self.hedef_y:
            self.animasyon_bitti = True
            return True
        
        return False
    
    def ciz(self, ekran):
        '''
        Şekeri ekrana çizer
        
        Args:
            ekran
        '''
        # Arka plan hücresi (açık gri kare)
        pygame.draw.rect(ekran, ACIK_GRI,
                        (self.hedef_x + 2, self.hedef_y + 2,
                         HUCRE_BOYUTU - 4, HUCRE_BOYUTU - 4))
        
        # Eğer şeker seçiliyse arka plana yeşil renk
        if self.secili:
            pygame.draw.rect(ekran, YESIL_ACIK,
                           (self.hedef_x + 2, self.hedef_y + 2,
                            HUCRE_BOYUTU - 4, HUCRE_BOYUTU - 4))
            pygame.draw.rect(ekran, BEYAZ,
                           (self.hedef_x + 1, self.hedef_y + 1,
                            HUCRE_BOYUTU - 2, HUCRE_BOYUTU - 2), 3)
        
        # Renkli daire çiz (animasyon pozisyonunda)
        merkez_x = int(self.x + HUCRE_BOYUTU // 2)
        merkez_y = int(self.y + HUCRE_BOYUTU // 2)
        yaricap = HUCRE_BOYUTU // 2 - 8
        
        # Ana daire (renkli)
        pygame.draw.circle(ekran, self.renk, (merkez_x, merkez_y), yaricap)
        
        # Daire etrafına siyah çerçeve
        # pygame.draw.circle(ekran, SIYAH, (merkez_x, merkez_y), yaricap, 2)
        
        # İç parlama efekti (küçük beyaz daire)
        # parlama_yaricap = yaricap // 3
        # pygame.draw.circle(ekran, BEYAZ, 
        #                   (merkez_x - yaricap // 4, merkez_y - yaricap // 4), 
        #                   parlama_yaricap)
        
        # Emoji'yi ortaya çiz (opsiyonel - eğer font destekliyorsa)
        try:
            emoji_text = FONT_EMOJI.render(self.sembol, True, SIYAH)
            emoji_rect = emoji_text.get_rect()
            emoji_rect.center = (merkez_x, merkez_y)
            ekran.blit(emoji_text, emoji_rect)
        except:
            # Emoji render edilemezse, sadece renkli daire kalır
            pass
    
    def __repr__(self):
        '''Şekeri yazdırmak için kullanışlı (debug için)'''
        return f"Seker({self.satir}, {self.sutun}, tip={self.tip})"
