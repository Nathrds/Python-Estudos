print('Conversor de medidas')
medida = float(input('Uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m corresponde a {:.0f}dm, {:.0f}cm, {:.0f}mm.'.format(medida, dm, cm, mm))
print('E a {}dam, {}hm, {}km.'.format(dam, hm, km))
