"""
    Bu modül oyunun ana döngüsünü ve olay yönetimini içerir.
"""

import pygame
import sys
from config import *
from oyun import CandyCrush



def main():
    '''
    Ana oyun döngüsü
    Oyunu başlatır ve kullanıcı çıkana kadar çalışır
    '''
    # Ekran oluştur
    ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    pygame.display.set_caption("Candy Crush 🍬 by GonulPolat")
    
    # Saat objesi (FPS kontrolü için)
    saat = pygame.time.Clock()
    
    # Oyunu başlat
    oyun = CandyCrush()
    
    # Ana döngü
    calisma = True
    while calisma:
        # Olayları işle
        for event in pygame.event.get():
            # Pencere kapatma
            if event.type == pygame.QUIT:
                calisma = False
            
            # Fare tıklama
            elif event.type == pygame.MOUSEBUTTONDOWN:
                fare_x, fare_y = pygame.mouse.get_pos()
                oyun.tiklama_isle(fare_x, fare_y)
            
            # Klavye
            elif event.type == pygame.KEYDOWN:
                # R tuşu: Oyunu yeniden başlat
                if event.key == pygame.K_r:
                    oyun.sifirla()
                # ESC tuşu: Çıkış
                elif event.key == pygame.K_ESCAPE:
                    calisma = False
        
        # Oyun durumunu güncelle (animasyonlar, otomatik işlemler)
        oyun.guncelle()
        
        # Oyunu çiz
        oyun.ciz(ekran)
        
        # Ekranı güncelle
        pygame.display.flip()
        
        # FPS sınırla
        saat.tick(FPS)
    
    # Temizlik ve çıkış
    pygame.quit()
    sys.exit()



# Program buradan başlar
if __name__ == "__main__":
    main()
