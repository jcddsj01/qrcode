# Instalação de biblioteca
# pip install qrcode[pil]

# Exemplo: Lista de sites de E-commerce de informática
import qrcode

links_sites = {
  'KaBum': 'https://www.kabum.com.br/',
  'Pichau': 'https://www.pichau.com.br/',
  'ChipArt': 'https://www.chipart.com.br/',
  'Terabyteshop': 'https://www.terabyteshop.com.br/',
  'MegaMamute': 'https://www.megamamute.com.br/',
  'Amazon': 'https://www.amazon.com.br/',
  'Submarino': 'https://www.submarino.com.br/'
}

for ecommerce in links_sites:
  link = links_sites[ecommerce]
  imagem_qrcode = qrcode.make(link)
  imagem_qrcode.save(f'qrcode_ecommerce_{ecommerce}.png')
