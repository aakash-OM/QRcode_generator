# QRcode_generator
# By providing link in the programme , we can get the QR Code related to given Link.

#Code

import qrcode
img=qrcode.make('https://motivationgrid.com/wp-content/uploads/2015/05/Tough-situation-Dwayne-Johnson-Quote.jpg')
img.save('theRock_qrcode.png')
img.show()
