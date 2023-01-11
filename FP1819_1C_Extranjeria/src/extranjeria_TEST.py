# -*- coding: utf-8 -*-
'''
Created on 25 ene. 2019

@author: reinaqu
'''

"""
Descomenta y usa el que necesites
"""
#from extranjeria import *
from extranjeria_solucion import *

################################################################
#  tests
################################################################
  
def test_lee_registros(datos):
    print('Número total de registros con datos extranjeros:', len(datos)) 
    print('Mostrando los tres primeros registros leídos:', datos[:3], '\n')

def test_numero_nacionalidades_distintas(datos):
    n = numero_nacionalidades_distintas(datos)
    print('Hay {} nacionalidades distintas'.format(n))
    print('\n')

def test_secciones_distritos_con_extranjeros_nacionalidades(datos, paises):
    
    distritos = secciones_distritos_con_extranjeros_nacionalidades(datos, paises)
    print ('Los distritos que tienen extranjeros de alguna de las nacionalidades {} son '.format(paises))
    print(distritos)
        
def test_total_extranjeros_por_pais(datos):
    dicc = total_extranjeros_por_pais(datos)
    print('Extranjeros totales por pais')
    print(dicc)
 
def test_top_n_extranjeria(datos, n=3):
    res = top_n_extranjeria(datos, n) 
    print('El top-{} es: '.format(n))
    print (res)

def test_barrio_mas_multicultural(datos):
    print('El barrio mas multicultural es: ')
    res = barrio_mas_multicultural(datos)
    print (res)
    print('\n')
    
def test_barrio_con_mas_extranjeros(datos, tipo=None):
    if (tipo == None):
        label=''
    else:
        label=tipo    

    print('El barrio con mas inmigrantes {} es: '.format(label))
    res = barrio_con_mas_extranjeros(datos, tipo)
    print (res)
    
def nombres_distrito():
    return["Casco Antiguo", "Macarena",
           "Nervión", "Cerro-Amate",
           "Sur", "Triana",
           "Bellavista-La Palmera" ,
           "Norte", "San Pablo-Santa Justa",
           "Este-Alcosa-Torreblanca",
           "Los Remedios"
           ]

def test_pais_mas_representado_por_distrito(datos):
    dicc = pais_mas_representado_por_distrito(datos)
    print ('Los paises más representados en cada distrito son')
    print (dicc)
    
################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
   
    DATOS=lee_datos_extranjeros('../data/extranjerosSevillla_utf8.csv')
    print('APARTADO A:')
    #La salida esperada es:
    #Número total de registros con datos extranjeros: 19231
    #Mostrando los tres primeros registros leídos: [DatosExtranjeros(Distrito=' 01', Seccion=' 001', Barrio='SANTA CATALINA', Pais='ALEMANIA', Hombres=8, Mujeres=6), DatosExtranjeros(Distrito=' 01', Seccion=' 001', Barrio='SANTA CATALINA', Pais='ARGELIA', Hombres=0, Mujeres=1), DatosExtranjeros(Distrito=' 01', Seccion=' 001', Barrio='SANTA CATALINA', Pais='ARGENTINA', Hombres=2, Mujeres=4)]  
    test_lee_registros(DATOS)
    
    print('APARTADO B:')
    #La salida esperada es:
    #Hay 186 nacionalidades distintas
    test_numero_nacionalidades_distintas(DATOS)
    
    print('APARTADO C:')
    #La salida esperada es:
    #Los distritos que tienen extranjeros de alguna de las nacionalidades ('ALEMANIA', 'ITALIA') son 
    #[(' 01', ' 001'), (' 01', ' 002'), (' 01', ' 003'), (' 01', ' 004'), (' 01', ' 005'), (' 01', ' 006'), (' 01', ' 007'), (' 01', ' 008'), (' 01', ' 009'), (' 01', ' 010'), (' 01', ' 011'), (' 01', ' 012'), (' 01', ' 013'), (' 01', ' 014'), (' 01', ' 015'), (' 01', ' 016'), (' 01', ' 017'), (' 01', ' 018'), (' 01', ' 019'), (' 01', ' 020'), (' 01', ' 021'), (' 01', ' 022'), (' 01', ' 023'), (' 01', ' 024'), (' 01', ' 025'), (' 01', ' 026'), (' 01', ' 027'), (' 01', ' 028'), (' 01', ' 029'), (' 01', ' 030'), (' 01', ' 032'), (' 01', ' 033'), (' 01', ' 034'), (' 01', ' 035'), (' 01', ' 036'), (' 01', ' 037'), (' 01', ' 038'), (' 01', ' 039'), (' 01', ' 040'), (' 01', ' 041'), (' 01', ' 042'), (' 01', ' 043'), (' 01', ' 044'), (' 01', ' 045'), (' 01', ' 046'), (' 01', ' 047'), (' 01', ' 048'), (' 01', ' 049'), (' 01', ' 050'), (' 01', ' 051'), (' 02', ' 001'), (' 02', ' 002'), (' 02', ' 003'), (' 02', ' 004'), (' 02', ' 005'), (' 02', ' 006'), (' 02', ' 007'), (' 02', ' 008'), (' 02', ' 009'), (' 02', ' 010'), (' 02', ' 011'), (' 02', ' 012'), (' 02', ' 013'), (' 02', ' 014'), (' 02', ' 015'), (' 02', ' 016'), (' 02', ' 017'), (' 02', ' 018'), (' 02', ' 019'), (' 02', ' 020'), (' 02', ' 021'), (' 02', ' 022'), (' 02', ' 023'), (' 02', ' 024'), (' 02', ' 025'), (' 02', ' 026'), (' 02', ' 027'), (' 02', ' 028'), (' 02', ' 030'), (' 02', ' 031'), (' 02', ' 032'), (' 02', ' 033'), (' 02', ' 036'), (' 02', ' 038'), (' 02', ' 039'), (' 02', ' 040'), (' 02', ' 041'), (' 02', ' 043'), (' 02', ' 044'), (' 02', ' 045'), (' 02', ' 047'), (' 02', ' 048'), (' 02', ' 049'), (' 02', ' 050'), (' 02', ' 051'), (' 02', ' 052'), (' 02', ' 053'), (' 02', ' 054'), (' 02', ' 055'), (' 02', ' 056'), (' 02', ' 057'), (' 02', ' 058'), (' 02', ' 060'), (' 02', ' 061'), (' 02', ' 063'), (' 02', ' 064'), (' 02', ' 065'), (' 02', ' 066'), (' 02', ' 067'), (' 03', ' 001'), (' 03', ' 002'), (' 03', ' 003'), (' 03', ' 004'), (' 03', ' 005'), (' 03', ' 006'), (' 03', ' 007'), (' 03', ' 008'), (' 03', ' 009'), (' 03', ' 010'), (' 03', ' 011'), (' 03', ' 012'), (' 03', ' 013'), (' 03', ' 014'), (' 03', ' 015'), (' 03', ' 016'), (' 03', ' 017'), (' 03', ' 019'), (' 03', ' 020'), (' 03', ' 021'), (' 03', ' 022'), (' 03', ' 023'), (' 03', ' 024'), (' 03', ' 025'), (' 03', ' 026'), (' 03', ' 027'), (' 03', ' 028'), (' 03', ' 029'), (' 03', ' 030'), (' 03', ' 031'), (' 03', ' 032'), (' 03', ' 033'), (' 03', ' 034'), (' 03', ' 035'), (' 03', ' 036'), (' 03', ' 037'), (' 03', ' 038'), (' 03', ' 039'), (' 03', ' 041'), (' 04', ' 001'), (' 04', ' 002'), (' 04', ' 003'), (' 04', ' 004'), (' 04', ' 005'), (' 04', ' 006'), (' 04', ' 007'), (' 04', ' 009'), (' 04', ' 010'), (' 04', ' 011'), (' 04', ' 012'), (' 04', ' 014'), (' 04', ' 015'), (' 04', ' 016'), (' 04', ' 018'), (' 04', ' 019'), (' 04', ' 020'), (' 04', ' 021'), (' 04', ' 022'), (' 04', ' 023'), (' 04', ' 024'), (' 04', ' 025'), (' 04', ' 026'), (' 04', ' 027'), (' 04', ' 031'), (' 04', ' 032'), (' 04', ' 033'), (' 04', ' 034'), (' 04', ' 035'), (' 04', ' 036'), (' 04', ' 037'), (' 04', ' 038'), (' 04', ' 039'), (' 04', ' 040'), (' 04', ' 041'), (' 04', ' 042'), (' 04', ' 043'), (' 04', ' 044'), (' 04', ' 045'), (' 04', ' 046'), (' 04', ' 047'), (' 04', ' 048'), (' 04', ' 049'), (' 04', ' 050'), (' 04', ' 052'), (' 04', ' 054'), (' 04', ' 055'), (' 04', ' 056'), (' 04', ' 057'), (' 04', ' 058'), (' 04', ' 059'), (' 04', ' 060'), (' 04', ' 061'), (' 04', ' 062'), (' 04', ' 063'), (' 04', ' 064'), (' 04', ' 065'), (' 04', ' 066'), (' 04', ' 067'), (' 04', ' 068'), (' 04', ' 069'), (' 05', ' 001'), (' 05', ' 002'), (' 05', ' 003'), (' 05', ' 004'), (' 05', ' 005'), (' 05', ' 006'), (' 05', ' 008'), (' 05', ' 009'), (' 05', ' 010'), (' 05', ' 011'), (' 05', ' 012'), (' 05', ' 014'), (' 05', ' 015'), (' 05', ' 016'), (' 05', ' 017'), (' 05', ' 018'), (' 05', ' 019'), (' 05', ' 020'), (' 05', ' 021'), (' 05', ' 022'), (' 05', ' 023'), (' 05', ' 024'), (' 05', ' 025'), (' 05', ' 027'), (' 05', ' 029'), (' 05', ' 030'), (' 05', ' 031'), (' 05', ' 032'), (' 05', ' 033'), (' 05', ' 035'), (' 05', ' 036'), (' 05', ' 037'), (' 05', ' 038'), (' 05', ' 039'), (' 05', ' 040'), (' 05', ' 041'), (' 05', ' 042'), (' 05', ' 043'), (' 05', ' 044'), (' 05', ' 046'), (' 05', ' 047'), (' 05', ' 048'), (' 05', ' 049'), (' 05', ' 050'), (' 05', ' 051'), (' 05', ' 052'), (' 05', ' 054'), (' 05', ' 056'), (' 05', ' 057'), (' 06', ' 001'), (' 06', ' 002'), (' 06', ' 003'), (' 06', ' 004'), (' 06', ' 005'), (' 06', ' 006'), (' 06', ' 007'), (' 06', ' 008'), (' 06', ' 009'), (' 06', ' 010'), (' 06', ' 011'), (' 06', ' 012'), (' 06', ' 013'), (' 06', ' 014'), (' 06', ' 015'), (' 06', ' 016'), (' 06', ' 017'), (' 06', ' 018'), (' 06', ' 019'), (' 06', ' 020'), (' 06', ' 021'), (' 06', ' 022'), (' 06', ' 023'), (' 06', ' 024'), (' 06', ' 025'), (' 06', ' 026'), (' 06', ' 027'), (' 06', ' 028'), (' 06', ' 029'), (' 06', ' 030'), (' 06', ' 031'), (' 06', ' 032'), (' 06', ' 033'), (' 06', ' 034'), (' 06', ' 035'), (' 06', ' 036'), (' 06', ' 037'), (' 06', ' 038'), (' 06', ' 039'), (' 06', ' 040'), (' 06', ' 041'), (' 06', ' 042'), (' 06', ' 043'), (' 07', ' 001'), (' 07', ' 002'), (' 07', ' 003'), (' 07', ' 004'), (' 07', ' 005'), (' 07', ' 006'), (' 07', ' 007'), (' 07', ' 008'), (' 07', ' 009'), (' 07', ' 010'), (' 07', ' 011'), (' 07', ' 012'), (' 07', ' 013'), (' 07', ' 014'), (' 07', ' 015'), (' 07', ' 016'), (' 07', ' 017'), (' 07', ' 018'), (' 07', ' 019'), (' 07', ' 020'), (' 07', ' 021'), (' 07', ' 022'), (' 07', ' 023'), (' 07', ' 024'), (' 07', ' 025'), (' 07', ' 026'), (' 07', ' 027'), (' 07', ' 028'), (' 07', ' 029'), (' 07', ' 030'), (' 07', ' 031'), (' 07', ' 033'), (' 07', ' 034'), (' 07', ' 036'), (' 07', ' 037'), (' 07', ' 038'), (' 07', ' 039'), (' 07', ' 040'), (' 07', ' 041'), (' 07', ' 042'), (' 07', ' 043'), (' 07', ' 044'), (' 07', ' 045'), (' 07', ' 046'), (' 07', ' 047'), (' 07', ' 048'), (' 07', ' 049'), (' 07', ' 050'), (' 07', ' 051'), (' 08', ' 001'), (' 08', ' 002'), (' 08', ' 003'), (' 08', ' 004'), (' 08', ' 005'), (' 08', ' 006'), (' 08', ' 007'), (' 08', ' 008'), (' 08', ' 009'), (' 08', ' 010'), (' 08', ' 011'), (' 08', ' 013'), (' 08', ' 014'), (' 08', ' 015'), (' 08', ' 016'), (' 08', ' 017'), (' 08', ' 018'), (' 08', ' 019'), (' 08', ' 020'), (' 08', ' 021'), (' 08', ' 022'), (' 08', ' 023'), (' 08', ' 024'), (' 08', ' 025'), (' 08', ' 026'), (' 08', ' 028'), (' 08', ' 029'), (' 08', ' 030'), (' 08', ' 031'), (' 08', ' 032'), (' 08', ' 033'), (' 08', ' 034'), (' 08', ' 036'), (' 08', ' 037'), (' 08', ' 038'), (' 08', ' 039'), (' 08', ' 042'), (' 08', ' 043'), (' 08', ' 045'), (' 08', ' 046'), (' 08', ' 048'), (' 08', ' 049'), (' 08', ' 050'), (' 08', ' 051'), (' 08', ' 052'), (' 09', ' 001'), (' 09', ' 002'), (' 09', ' 003'), (' 09', ' 004'), (' 09', ' 005'), (' 09', ' 006'), (' 09', ' 007'), (' 09', ' 008'), (' 09', ' 009'), (' 09', ' 010'), (' 09', ' 011'), (' 09', ' 013'), (' 09', ' 014'), (' 09', ' 015'), (' 09', ' 016'), (' 09', ' 017'), (' 09', ' 018'), (' 09', ' 021'), (' 09', ' 022'), (' 09', ' 023'), (' 09', ' 024'), (' 09', ' 025'), (' 09', ' 026'), (' 09', ' 027'), (' 09', ' 028'), (' 09', ' 029'), (' 09', ' 030'), (' 09', ' 031'), (' 09', ' 032'), (' 09', ' 033'), (' 09', ' 034'), (' 09', ' 035'), (' 09', ' 036'), (' 09', ' 037'), (' 09', ' 038'), (' 09', ' 039'), (' 09', ' 040'), (' 09', ' 041'), (' 09', ' 042'), (' 09', ' 043'), (' 09', ' 044'), (' 09', ' 045'), (' 09', ' 046'), (' 09', ' 047'), (' 09', ' 048'), (' 09', ' 049'), (' 09', ' 050'), (' 09', ' 051'), (' 09', ' 052'), (' 09', ' 053'), (' 09', ' 054'), (' 09', ' 055'), (' 09', ' 056'), (' 09', ' 057'), (' 09', ' 058'), (' 09', ' 059'), (' 09', ' 060'), (' 09', ' 061'), (' 09', ' 062'), (' 09', ' 063'), (' 09', ' 064'), (' 09', ' 065'), (' 09', ' 066'), (' 09', ' 067'), (' 10', ' 001'), (' 10', ' 002'), (' 10', ' 003'), (' 10', ' 004'), (' 10', ' 005'), (' 10', ' 006'), (' 10', ' 007'), (' 10', ' 008'), (' 10', ' 009'), (' 10', ' 010'), (' 10', ' 011'), (' 10', ' 012'), (' 10', ' 013'), (' 10', ' 014'), (' 10', ' 015'), (' 10', ' 016'), (' 10', ' 017'), (' 10', ' 018'), (' 10', ' 019'), (' 10', ' 020'), (' 10', ' 021'), (' 10', ' 022'), (' 10', ' 023'), (' 10', ' 024'), (' 10', ' 025'), (' 10', ' 026'), (' 10', ' 027'), (' 11', ' 001'), (' 11', ' 002'), (' 11', ' 003'), (' 11', ' 004'), (' 11', ' 005'), (' 11', ' 006'), (' 11', ' 007'), (' 11', ' 008'), (' 11', ' 009'), (' 11', ' 010'), (' 11', ' 011'), (' 11', ' 012'), (' 11', ' 013'), (' 11', ' 014'), (' 11', ' 016'), (' 11', ' 017'), (' 11', ' 019')]
    #Los distritos que tienen extranjeros de alguna de las nacionalidades SANTA SEDE son 
    #[(' 01', ' 004'), (' 01', ' 015'), (' 01', ' 016'), (' 01', ' 017'), (' 01', ' 021'), (' 01', ' 023'), (' 01', ' 025'), (' 01', ' 028'), (' 01', ' 029'), (' 01', ' 032'), (' 01', ' 034'), (' 01', ' 036'), (' 01', ' 037'), (' 01', ' 041'), (' 01', ' 045'), (' 01', ' 047'), (' 01', ' 048'), (' 01', ' 051'), (' 02', ' 001'), (' 02', ' 003'), (' 02', ' 005'), (' 02', ' 006'), (' 02', ' 007'), (' 02', ' 017'), (' 02', ' 029'), (' 02', ' 031'), (' 02', ' 036'), (' 02', ' 038'), (' 02', ' 043'), (' 02', ' 044'), (' 02', ' 045'), (' 02', ' 049'), (' 02', ' 051'), (' 02', ' 053'), (' 02', ' 056'), (' 02', ' 061'), (' 02', ' 065'), (' 02', ' 066'), (' 03', ' 001'), (' 03', ' 003'), (' 03', ' 005'), (' 03', ' 006'), (' 03', ' 007'), (' 03', ' 009'), (' 03', ' 010'), (' 03', ' 011'), (' 03', ' 013'), (' 03', ' 015'), (' 03', ' 019'), (' 03', ' 023'), (' 03', ' 025'), (' 03', ' 026'), (' 03', ' 027'), (' 03', ' 028'), (' 03', ' 029'), (' 03', ' 031'), (' 03', ' 032'), (' 03', ' 036'), (' 03', ' 038'), (' 03', ' 039'), (' 03', ' 041'), (' 04', ' 011'), (' 04', ' 016'), (' 04', ' 023'), (' 04', ' 032'), (' 04', ' 038'), (' 04', ' 044'), (' 04', ' 046'), (' 04', ' 059'), (' 04', ' 068'), (' 05', ' 001'), (' 05', ' 004'), (' 05', ' 009'), (' 05', ' 017'), (' 05', ' 019'), (' 05', ' 020'), (' 05', ' 022'), (' 05', ' 024'), (' 05', ' 027'), (' 05', ' 037'), (' 05', ' 038'), (' 05', ' 049'), (' 05', ' 056'), (' 05', ' 057'), (' 06', ' 003'), (' 06', ' 005'), (' 06', ' 007'), (' 06', ' 010'), (' 06', ' 011'), (' 06', ' 012'), (' 06', ' 015'), (' 06', ' 016'), (' 06', ' 017'), (' 06', ' 018'), (' 06', ' 020'), (' 06', ' 021'), (' 06', ' 023'), (' 06', ' 028'), (' 06', ' 030'), (' 06', ' 031'), (' 06', ' 033'), (' 06', ' 042'), (' 07', ' 001'), (' 07', ' 003'), (' 07', ' 004'), (' 07', ' 013'), (' 07', ' 025'), (' 07', ' 026'), (' 07', ' 046'), (' 07', ' 049'), (' 08', ' 003'), (' 08', ' 005'), (' 08', ' 008'), (' 08', ' 011'), (' 08', ' 013'), (' 08', ' 018'), (' 08', ' 021'), (' 08', ' 023'), (' 08', ' 025'), (' 08', ' 036'), (' 08', ' 037'), (' 09', ' 004'), (' 09', ' 007'), (' 09', ' 031'), (' 09', ' 040'), (' 09', ' 048'), (' 09', ' 049'), (' 09', ' 053'), (' 09', ' 056'), (' 09', ' 058'), (' 10', ' 001'), (' 10', ' 009'), (' 10', ' 011'), (' 10', ' 016'), (' 10', ' 017'), (' 10', ' 018'), (' 10', ' 020'), (' 10', ' 022'), (' 10', ' 026'), (' 10', ' 027'), (' 11', ' 005'), (' 11', ' 006'), (' 11', ' 007'), (' 11', ' 008'), (' 11', ' 016'), (' 11', ' 018')]    test_secciones_distritos_con_extranjeros_nacionalidades(DATOS,('ALEMANIA','ITALIA'))
    test_secciones_distritos_con_extranjeros_nacionalidades(DATOS,('SANTA SEDE'))

    print('APARTADO D:')  
    #La salida esperada es:
    #{'ALEMANIA': 2074, 'ARGELIA': 505, 'ARGENTINA': 1515, 'ARMENIA': 624, 'AUSTRIA': 1202, 'AZERBAIAN': 208, 'BELGICA': 503, 'BOLIVIA': 3409, 'BRASIL': 1099, 'BULGARIA': 348, 'BURKINA FASSO': 305, 'CHECOSLOVAQUIA': 276, 'CHINA': 3232, 'COLOMBIA': 3284, 'CUBA': 872, 'DINAMARCA': 130, 'ECUADOR': 3100, 'ESLOVAQUIA': 188, 'ESLOVENIA': 73, 'ESTADOS UNIDOS DE AMERICA': 882, 'ETIOPIA': 74, 'FINLANDIA': 136, 'FRANCIA': 2252, 'GAMBIA': 103, 'HAITI': 21, 'IRLANDA': 269, 'ITALIA': 1538, 'JAPON': 125, 'MARRUECOS': 6035, 'MAURITANIA': 70, 'MEXICO': 631, 'MONACO': 45, 'MONTENEGRO': 503, 'NORUEGA': 385, 'NUEVA ZELANDA': 15, 'PAISES BAJOS': 475, 'PERU': 2650, 'POLONIA': 546, 'PORTUGAL': 1078, 'PRINCIPADO DE ANDORRA': 538, 'REINO UNIDO': 1283, 'REPUBLICA DOMINICANA': 778, 'RUMANIA': 2761, 'SERBIA Y MONTENEGRO': 90, 'SUIZA': 556, 'UCRANIA': 948, 'VENEZUELA': 1045, 'BIELORUSIA': 135, 'CHILE': 314, 'GRECIA': 78, 'GUATEMALA': 124, 'HONDURAS': 268, 'INDIA': 115, 'KENIA': 64, 'REPUBLICA CENTROAFRICANA': 59, 'REPUBLICA DE COREA': 51, 'REPUBLICA DEMOCRATICA DEL CONGO': 979, 'RUSIA': 1265, 'SUECIA': 232, 'CANADA': 98, 'GUINEA BISSAU': 106, 'ISLANDIA': 70, 'ISRAEL': 24, 'TANZANIA': 130, 'TURQUIA': 34, 'ALBANIA': 492, 'ESTONIA': 252, 'MACEDONIA': 49, 'NICARAGUA': 1058, 'PARAGUAY': 1375, 'REPUBLICA DEMOCRATICA ALEMANA': 58, 'SANTA SEDE': 191, 'ZAMBIA': 24, 'EL SALVADOR': 202, 'HUNGRIA': 152, 'MOZAMBIQUE': 30, 'OTROS PAISES SIN RELACION DIPLOMATICA': 106, 'SIERRA LEONA': 34, 'UGANDA': 18, 'URUGUAY': 232, 'ANGOLA': 65, 'AUSTRALIA': 88, 'CAMERUN': 108, 'COSTA DE MARFIL': 138, 'GEORGIA': 273, 'MADAGASCAR': 10, 'ARABIA SAUDITA': 7, 'FILIPINAS': 262, 'GUINEA': 112, 'NAMIBIA': 57, 'NO CONSTA': 227, 'PANAMA': 54, 'SANTO TOME Y PRINCIPE': 47, 'BOSNIA-HERZEGOVINA': 72, 'BOSTWANA': 33, 'GHANA': 83, 'LITUANIA': 120, 'NIGERIA': 880, 'SERBIA': 37, 'SIRIA': 147, 'TCHAD': 19, 'COSTA RICA': 70, 'LETONIA': 234, 'SAN MARINO': 17, 'REPUBLICA CHECA': 80, 'EGIPTO': 79, 'EMIRATOS ARABES UNIDOS': 6, 'RUANDA': 13, 'ANTIGUA YUGOSLAVIA': 73, 'COMORES': 19, 'LIECHTENSTEIN': 86, 'TUNEZ': 24, 'CABO VERDE': 17, 'LIBIA': 18, 'OTROS EUROPA SIN RELACION DIPL': 22, 'SAN VICENTE Y LAS GRANADINAS': 1, 'LIBANO': 46, 'MALI': 96, 'PAKISTAN': 181, 'BANGLA-DESH': 29, 'INDONESIA': 12, 'JORDANIA': 50, 'SENEGAL': 718, 'GUINEA ECUATORIAL': 134, 'MOLDAVIA': 59, 'VIET-NAM': 23, 'KAZAJSTAN': 26, 'OTROS TERR. ESPAÑOLES': 29, 'CROACIA': 50, 'NEPAL': 19, 'IRAN': 58, 'LUXEMBURGO': 51, 'DJIBUTI': 11, 'SWAZILANDIA': 25, 'TOGO': 11, 'CHIPRE': 37, 'LIBERIA': 36, 'BURUNDI': 12, 'GRANADA': 13, 'SINGAPUR': 7, 'ZIMBABWE': 15, 'MALTA': 41, 'TAIWAN': 5, 'GABON': 19, 'MAURICIO': 12, 'TAILANDIA': 5, 'MALASIA': 9, 'REPUBLICA SUDAFRICANA': 30, 'OTROS AFRICA SIN RELACION DIPL': 2, 'KUWAIT': 2, 'SUDAN': 21, 'BENIN': 14, 'LAOS': 1, 'UZBEKISTAN': 15, 'BRUNEI': 2, 'SOMALIA': 32, 'IRAK': 18, 'QATAR': 4, 'SEYCHELLES': 5, 'AZERBAIYAN': 15, 'SRI-LANKA': 4, 'YEMEN': 2, 'CONGO': 44, 'KIRGVISTAN': 9, 'LESHOTO': 9, 'DOMINICA': 9, 'BAHREIN': 1, 'MALAWI': 8, 'JAMAICA': 6, 'AFGANISTAN': 21, 'NIGER': 11, 'PALESTINA. ESTADO OBSERVADOR, NO MIEMBRO DE NACIONES UNIDAS': 1, 'GUYANA': 2, 'MONGOLIA': 3, 'CAMBOYA': 2, 'APATRIDA': 4, 'ERITREA': 6, 'TURKMENISTAN': 2, 'TADYIKISTAN': 2, 'BARBADOS': 2, 'TRINIDAD-TOBAGO': 1, 'SAN CRISTOBAL Y NIEVES': 1, 'SANTA LUCIA': 1, 'BAHAMAS': 1, 'BELICE': 1, 'SURINAM': 1}
    test_total_extranjeros_por_pais(DATOS)
    
    print('APARTADO E:')
    #La salida esperada es:
    #El top-3 es: 
    #[('MARRUECOS', 6035), ('BOLIVIA', 3409), ('COLOMBIA', 3284)]
    #El top-5 es: 
    #[('MARRUECOS', 6035), ('BOLIVIA', 3409), ('COLOMBIA', 3284), ('CHINA', 3232), ('ECUADOR', 3100)]
    test_top_n_extranjeria(DATOS)
    test_top_n_extranjeria(DATOS, 5)
    
    print('APARTADO F:')
    #La salida esperada es:
    #El barrio mas multicultural es: 
    #COLORES, ENTREPARQUES
    test_barrio_mas_multicultural(DATOS)

    print('APARTADO G:')
    #La salida esperada es 
    #El barrio con mas inmigrantes  es: 
    #COLORES, ENTREPARQUES
    #El barrio con mas inmigrantes Hombres es: 
    #LA PLATA
    #El barrio con mas inmigrantes Mujeres es: 
    #LOS REMEDIOS
    test_barrio_con_mas_extranjeros(DATOS, None)
    test_barrio_con_mas_extranjeros(DATOS, 'Hombres')
    test_barrio_con_mas_extranjeros(DATOS, 'Mujeres')
    

    print('APARTADO H:')
    #La salida esperada es
    #Los paises más representados en cada distrito son
    #{' 01': 'FRANCIA', ' 02': 'BOLIVIA', ' 03': 'MARRUECOS', ' 04': 'MARRUECOS', ' 05': 'MARRUECOS', ' 06': 'MARRUECOS', ' 07': 'MARRUECOS', ' 08': 'MARRUECOS', ' 09': 'COLOMBIA', ' 10': 'MARRUECOS', ' 11': 'MARRUECOS'}
    test_pais_mas_representado_por_distrito(DATOS)
    