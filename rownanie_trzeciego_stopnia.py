#Wprowadzenie parametrów równania

print('Podaj parametry równania\n')
print('a*x^3+b*x^2+c*x+d=0\n')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
d=float(input('d='))

#Funkcja która zamienia wartość liczzbową na string i dopisuje znak "+" jeżeli wartość jet >0
def znak(wyr):
    if wyr>=0 : znak = '+'+str(wyr)
    else : znak = str(wyr)
    return znak

#Wypisanie równania
print('\n')
print('Równanie ma postać:\n')
print(str(a)+'*x^3 '+znak(b)+'*x^2 '+znak(c)+'*x '+znak(d)+' = 0\n')

#Obliczenie delty

delta=-4*pow(c,3)*a+pow(c,2)*pow(b,2)+18*c*b*a*d-27*pow(d,2)*pow(a,2)-4*d*pow(b,3)

#Obliczenie składowych rozwiązań - czyli części rozwiązań powtarzających się w każdym rozwiązaniu

mod_1=pow((9*c*b*a-27*d*pow(a,2)-2*pow(b,3)+3*a*pow(-3*delta,(1/2)))/(2*pow(a,3)),(1/3))
mod_2=(3*c*a-pow(b,2))/(pow(a,2)*mod_1)
mod_3=b/(3*a)

#Oblizcenie rozwiązań

x1=1/3*mod_1-1/3*mod_2-mod_3
x2=(-1+pow(-3,1/2))/6*mod_1+(1+pow(-3,1/2))/6*mod_2-mod_3
x3=-(1+pow(-3,1/2))/6*mod_1+(1-pow(-3,1/2))/6*mod_2-mod_3

#Wypisanie delty i trzech rozwiązań

print('delta= ')
print(delta)
print('')
print('x1= ')
print(x1)
print('x2= ')
print(x2)
print('x3= ')
print(x3)
