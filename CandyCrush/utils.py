"""
    Bu modül yardımcı fonksiyonları içerir.
"""

import pygame
from config import *


def izgara_ciz(ekran):
    '''
    Oyun ızgarasının çerçevesini ve hücre çizgilerini çizer
    
    Args:
        ekran
    '''
    # Ana çerçeve
    pygame.draw.rect(ekran, SIYAH, 
                    (IZGARA_X - 5, IZGARA_Y - 5,
                     IZGARA_BOYUTU * HUCRE_BOYUTU + 10,
                     IZGARA_BOYUTU * HUCRE_BOYUTU + 10), 3)
    
    # Izgara çizgileri (hücre sınırları)
    for i in range(IZGARA_BOYUTU + 1):
        # Yatay çizgiler
        y = IZGARA_Y + i * HUCRE_BOYUTU
        pygame.draw.line(ekran, GRI,
                        (IZGARA_X, y),
                        (IZGARA_X + IZGARA_BOYUTU * HUCRE_BOYUTU, y), 1)
        
        # Dikey çizgiler
        x = IZGARA_X + i * HUCRE_BOYUTU
        pygame.draw.line(ekran, GRI,
                        (x, IZGARA_Y),
                        (x, IZGARA_Y + IZGARA_BOYUTU * HUCRE_BOYUTU), 1)


def bilgi_ciz(ekran, puan: int, hamle: int):
    '''
    Puan ve hamle bilgisini ekrana çizer
    
    Args:
        ekran (pygame.Surface): Çizim yapılacak ekran
        puan (int): Mevcut puan
        hamle (int): Kalan hamle sayısı
    '''
    puan_text = FONT_KUCUK.render(f"Puan: {puan}", True, SIYAH)
    hamle_text = FONT_KUCUK.render(f"Hamle: {hamle}/{MAKSIMUM_HAMLE}", True, SIYAH)
    
    ekran.blit(puan_text, (20, 20))
    ekran.blit(hamle_text, (20, 55))


def modal_ciz(ekran, puan: int):
    '''
    Oyun sonu modalını çizer
    
    Args:
        ekran (pygame.Surface): Çizim yapılacak ekran
        puan (int): Final puanı
    '''
    # Yarı saydam overlay
    overlay = pygame.Surface((GENISLIK, YUKSEKLIK))
    overlay.set_alpha(180)
    overlay.fill(SIYAH)
    ekran.blit(overlay, (0, 0))
    
    # Modal kutusu
    modal_genislik = 400
    modal_yukseklik = 300
    modal_x = (GENISLIK - modal_genislik) // 2
    modal_y = (YUKSEKLIK - modal_yukseklik) // 2
    
    # Modal arka plan (beyaz)
    pygame.draw.rect(ekran, BEYAZ, 
                    (modal_x, modal_y, modal_genislik, modal_yukseklik),
                    border_radius=20)
    
    # Modal çerçeve
    pygame.draw.rect(ekran, SIYAH, 
                    (modal_x, modal_y, modal_genislik, modal_yukseklik),
                    3, border_radius=20)
    
    # Başlık
    baslik = FONT_BUYUK.render("OYUN BİTTİ!", True, KIRMIZI)
    baslik_x = modal_x + (modal_genislik - baslik.get_width()) // 2
    ekran.blit(baslik, (baslik_x, modal_y + 40))
    
    # Puan
    puan_text = FONT_BUYUK.render(f"PUAN: {puan}", True, YESIL)
    puan_x = modal_x + (modal_genislik - puan_text.get_width()) // 2
    ekran.blit(puan_text, (puan_x, modal_y + 110))
    
    # Yeniden başlatma talimatı
    yeniden_text = FONT_ORTA.render("R - Yeniden Başlat", True, SIYAH)
    yeniden_x = modal_x + (modal_genislik - yeniden_text.get_width()) // 2
    ekran.blit(yeniden_text, (yeniden_x, modal_y + 190))
    
    # Çıkış talimatı
    cikis_text = FONT_KUCUK.render("ESC - Çıkış", True, GRI)
    cikis_x = modal_x + (modal_genislik - cikis_text.get_width()) // 2
    ekran.blit(cikis_text, (cikis_x, modal_y + 240))


def komsu_mu(seker1, seker2):
    '''
    İki şekerin komşu olup olmadığını (yatay veya dikey) kontrol eder
    
    Args:
        seker1 (Seker): İlk şeker
        seker2 (Seker): İkinci şeker
    
    Returns:
        bool: Komşu ise True, değilse False
    '''
    satir_fark = abs(seker1.satir - seker2.satir)
    sutun_fark = abs(seker1.sutun - seker2.sutun)
    
    # Komşu: ya aynı satırda yan yana, ya aynı sütunda üst üste
    return (satir_fark == 1 and sutun_fark == 0) or \
           (satir_fark == 0 and sutun_fark == 1)


def piksel_to_izgara(fare_x, fare_y):
    '''
    Fare koordinatlarını ızgara koordinatlarına çevirir
    
    Args:
        fare_x (int): Fare X koordinatı
        fare_y (int): Fare Y koordinatı
    
    Returns:
        tuple: (satir, sutun) veya None (ızgara dışındaysa)
    '''
    # Tıklama ızgara içinde mi kontrol et
    if (fare_x < IZGARA_X or fare_x > IZGARA_X + IZGARA_BOYUTU * HUCRE_BOYUTU or
        fare_y < IZGARA_Y or fare_y > IZGARA_Y + IZGARA_BOYUTU * HUCRE_BOYUTU):
        return None
    
    # Hangi hücreye tıklandığını hesapla
    sutun = (fare_x - IZGARA_X) // HUCRE_BOYUTU
    satir = (fare_y - IZGARA_Y) // HUCRE_BOYUTU
    
    return (satir, sutun)
