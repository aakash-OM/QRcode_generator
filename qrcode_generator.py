import qrcode
img=qrcode.make('https://motivationgrid.com/wp-content/uploads/2015/05/Tough-situation-Dwayne-Johnson-Quote.jpg')
img.save('theRock_qrcode.png')
img.show()
