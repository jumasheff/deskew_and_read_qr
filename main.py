import qrtools
# Я изменил этот импорт
# чтобы класс Deskew брался из локального файла deskew.py
from .deskew import Deskew

# text_with_qr_30_deg.png is given for testing purposes.
# use your image here
input_file = 'text_with_qr_30_deg.png'
output_file = 'text_with_qr_30_deg_deskewed.png'


"""
===================================================
"""

d = Deskew(
    input_file=input_file,
    display_image=False,
    output_file=output_file,
    r_angle=0
)
d.run()

"""
===================================================
"""
qr = qrtools.QR()
qr.decode(output_file)

print qr.data
