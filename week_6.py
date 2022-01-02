word = '<html> <body> <h1> Of course NIU CSIE is the best </h1> </body> </html>'
# 將word 以<h1>為中心，切成兩等份，a[0]=<html> <body> 、a[1]=Of course NIU CSIE is the best </h1> </body> </html>
a = word.split(sep='<h1>', maxsplit=1)
# 將a[1] 以</h1>為中心，切成兩等份，b[0]=Of course NIU CSIE is the best、b[1]=</body> </html>
b = a[1].split(sep='</h1>', maxsplit=1)
c = b[0]
print(c[c.find('best'):])  # 尋找'best'的索引值後，顯示索引值後的所有元素
print(c[c.find('NIU'):c.find('IE')])  # 尋找'N'、'E'的索引值，顯示 N~E 的所有元素
print(c[c.find('ou'):c.find('t')+1:3])  # 尋找'o'、't'的索引值，從'o'到't'每三個字元顯示一次
# 2022/1/2 修改
