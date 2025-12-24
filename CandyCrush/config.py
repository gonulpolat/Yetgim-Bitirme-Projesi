"""
    Bu modül oyundaki tüm sabit değişkenleri içerir.
"""

import pygame
import sys

pygame.init() # Pygame'i başlat

GENISLIK = 600 # Pencere ayarları
YUKSEKLIK = 700

IZGARA_BOYUTU = 8  # 8x8 şeker tablosu
HUCRE_BOYUTU = 60  # Her şeker 60x60 piksel
IZGARA_X = (GENISLIK - IZGARA_BOYUTU * HUCRE_BOYUTU) // 2  # şeker tablosunu ekranda ortala
IZGARA_Y = 100

# Renk tanımları (RGB)
BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)
GRI = (200, 200, 200)
ACIK_GRI = (230, 230, 230)
YESIL_ACIK = (144, 238, 144)
KIRMIZI = (255, 50, 50)
YESIL = (50, 255, 50)
MAVI = (50, 50, 255)
SARI = (255, 255, 50)
MOR = (200, 50, 200)
TURUNCU = (255, 165, 0)
MODAL_OVERLAY = (0, 0, 0, 180)  # Yarı saydam siyah


SEKER_RENKLERI = [KIRMIZI, YESIL, MAVI, SARI, MOR, TURUNCU]
SEKER_SEMBOLLERI = ['🍩', '🍉', '🍇', '🍌', '🍔', '🍗']

DUSME_HIZI = 15  # Şekerlerin düşme hızı (piksel/frame)

FPS = 60  # Saniyede kare sayısı
PUAN_CARPANI = 10  # Her eşleşen şeker için puan
MAKSIMUM_HAMLE = 20  # Oyuncu toplam 20 hamle yapabilir


try:
    # Windows emoji fontu
    if sys.platform == 'win32':
        FONT_EMOJI = pygame.font.SysFont('segoeuisymbol', 40)
    else:
        # MacOS veya Linux için varsayılan
        FONT_EMOJI = pygame.font.SysFont('applegothic', 40)
except:
    FONT_EMOJI = pygame.font.Font(None, 40)

FONT_BUYUK = pygame.font.Font(None, 48)
FONT_KUCUK = pygame.font.Font(None, 32)
FONT_ORTA = pygame.font.Font(None, 36)
