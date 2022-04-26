"""برای رند کردن یک رقم اعشاری از این دستور استفاده میکنیم"""
a = 1.23456
print("01.\n", round(a,1))
print("\n__________________________________________________\n")
"""فرمت دهی رشته ها با استفاده از % درصد """ 
b = 1
c = 2.123456789
print('02.\nb is: %i\nc is: %f\nd is: %s\ne is: %c' % (b, c, 'farbod', (100 )))
print("\n__________________________________________________\n")
#%o :رقم را به  برمبنای 8 نشان میدهد
print('03.\n', "%o" % (222))
print("\n__________________________________________________\n")
#%x :رقم را برمبنای 16 نشان میدهد 
print('04.\n', "%x" %(10), '%X' %(10))
print("\n__________________________________________________\n")
#%e :برای نشان دادن نماد علمی رقم استفاده میشود
print('05.\n', "%e" %(101213),"%E" %(101213))  
print("\n__________________________________________________\n")
#%.2f :با تغییر رقم بعد نقطه میتوانیم نمایش ارقام اعشاری را کمترل کنیم
f = 1.23456789
print('06.\n', "%.4f" %(f))
print("%+4.2f" %(f))
print("\n__________________________________________________\n")
#میتوانیم از دیکشنری ها نیز درین امر استفاده کنیم
g = {'a': 1, 'b': 2.3,'c': "farbod" }
print('07.\n', '%(a)i\n%(b)f\n%(c)s' %(g))
print("\n__________________________________________________\n")
#برای زمانی که میخواهیم از کاربر ورودی بگبریم از اپراتور * استفاده میکنیم
"""h = 9.876543210
i = int(input("i: "))
j = int(input("j: "))
print('08.\n', "%0*.*f" %(i, j, ))"""

print("\n__________________________________________________\n")
"""تغیر فرمت با استفاده از دستور format """
a = 10
b =  1.37757024
print('09.\n', 'a is {}\nb is {}\nc is {}'.format(10, b, 'farbod'))
 
#اگر بخواهیم ترتیب را رعایت نکنیم میتوانیم از جایگزاری اعداد استفاده کنیم 
#اعداد همیشه باید از رقم 0 شروع شود
print('10.\n', 'a is {2}\nb is {1}\nc is {0}'.format(5, b, 'farbod' ))
#استفاده از دیکشنری ها در دستور format
#با استفاده از 2ستاره
d = {'x':77, 'y':13.77, 'z':"farbod"}
print('11.\n', 'a is {z}\nb is {x}\nc is {y}\ne is {z}'.format(**d))
#حتی میتوان از رشته ها نیز استفاده کرد
#با استفاده از یک ستاره
print('12.\na is {0}\nb is {1}\nc is {2}\nd is {3}\ne is {4}\nf is {5}'.format(*"farbod"))
print("\n__________________________________________________\n")
"""ترتیب بندی کد در دستور format"""
#اختیاری هستند جز تایپ
#"{"[filed_name(کد باینری یا اسم کلیدی کاراکتر)] ["!"conversion(نوع داده را مشخص میکند)] [":"format_spec(فرمت را اینجا مشخص میکنیم اجباری)]}
#مواردی که بعد از ":" نوشته میشوند
#تمامااختیاری[[fill(جای خالی را با چی پر کند)]align(جهت چینش را مشخص میکند)][sign(بودن رقم را نشان بدهد+.-)][#][0(جاهای خالی را با 0 پر میکند)][width(طول میدان)][grouping_option(جدا کننده دسته ها)][.precision][type]]
#برای اضافه کردن این مشخصات از خارج برنامه باید ورودی های مشخص شده از سوی کاربر را بعدد از .format نیز صدا کرد
#برای توضیحات کاملتر با داکیومنت پایتون مراجعه شود
print('finaly')
