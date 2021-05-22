import requests
from bs4 import BeautifulSoup
import csv

lista = ["lista de no encontrados"]
prefijo = 'url_base'

csv_file = open('filename.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['identificador',
                     'link_info',
                     'nombre_recurso',
                     'ruta_recurso',
                     'titulo',
                     'autor',
                     'asesor',
                     'facultad',
                     'grado',
                     'area1', 'area2',
                     'clave1', 'clave2', 'clave3', 'clave4', 'clave5', 'clave6',
                     'resumen', 'summary',
                     'fecha_disponible',
                     'curp_autor',
                     'curp_asesor'])

for i in range(1, 2000):
    
    identificador = str(i)
    liga = 'url/handle/123456789/' + str(i) + '?mode=full'
    source = requests.get(liga).text
    soup = BeautifulSoup(source, 'lxml')

    validar = soup.find('div', class_='container').h1

    if validar == 'Identificador inválido':
        identificador = 'none' 
        link_info = 'none'
        nombre_recurso = 'none'
        ruta_recurso = 'none'
        titulo = 'none'
        autor = 'none'
        asesor = 'none'
        facultad = 'none'
        grado = 'none'
        area1 = 'none' 
        area2 = 'none'
        clave1 = 'none' 
        clave2 = 'none' 
        clave3 = 'none' 
        clave4 = 'none'
        clave5 = 'none'
        clave6 = 'none'
        resumen = 'none'
        summary = 'none'
        fecha_disponible = 'none'
        curp_autor = 'none'
        curp_asesor = 'none'

        csv_writer.writerow([identificador, 
                    link_info,
                    nombre_recurso,
                    ruta_recurso,
                    titulo,
                    autor,
                    asesor,
                    facultad,
                    grado,
                    area1, area2,
                    clave1, clave2, clave3, clave4, clave5, clave6,
                    resumen, summary,
                    fecha_disponible,
                    curp_autor, curp_asesor])
    else:
        link_info = soup.find('div', class_='well')
        if link_info != None:
            try:
                link_info = link_info.code.text
                print(link_info)
            except Exception as e:
                link_info = 'none'
                print(link_info)
        else:
            link_info = 'none'
            print(link_info)

        nombre_recurso = soup.find('td', class_='standard break-all')
        if nombre_recurso != None:
            nombre_recurso = nombre_recurso.a.text
            print(nombre_recurso)
        else:
            nombre_recurso = 'none'
            print(nombre_recurso)

        ruta_recurso = soup.find('td', class_='standard break-all')
        if ruta_recurso != None:
            ruta_recurso = ruta_recurso.a['href']
            ruta_recurso = prefijo + ruta_recurso
            print(ruta_recurso)
        else:
            ruta_recurso = 'none'
            print(ruta_recurso)

        if soup.find_all('td', text='dc.title') != []:
            titulo = soup.find_all('td', text='dc.title')[0].next_sibling.text
            print(titulo)
        else:
            titulo = 'none'
            print(titulo)

        if soup.find_all('td', text='dc.creator') != []:
            autor = soup.find_all('td', text='dc.creator')[0].next_sibling.text
            print(autor)

            try:
                asesor = soup.find_all('td', text='dc.contributor')[0]
                asesor = asesor.next_sibling.text
                print(asesor)
            except Exception as e:
                asesor = 'none'
                print(asesor)

            try:
                facultad = soup.find_all('li')[18]
                facultad = facultad.a.text
                print(facultad)
            except Exception as e:
                facultad = 'none'
                print(facultad)

            try:
                grado = soup.find_all('td', text='dc.type')[0]
                grado = grado.next_sibling.text
                print(grado)
            except:
                grado = 'none'
                print(grado)

            if soup.find_all('td', text='dc.subject') != []:
                areas = soup.find_all('td', text='dc.subject')
                area1 = areas[0].next_sibling.text
                print(area1)
                try:
                    area2 = areas[1].next_sibling.text
                    print(area2)
                except Exception as e:
                    area2 = 'none'
                    print(area2)
            else:
                area1 = 'none'
                area2 = 'none'
                print(area1)
                print(area2)

        else:
            autor = 'none'
            asesor = 'none'
            facultad = 'none'
            grado = 'none'
            area1 = 'none'
            area2 = 'none'
            print(autor)
            print(asesor)
            print(facultad)
            print(grado)
            print(area1)
            print(area2)

        if soup.find_all('td', text='dc.identifier') != []:
            claves = soup.find_all('td', text='dc.identifier')
            if len(claves) == 3:
                    clave1 = claves[0].next_sibling.text
                    print(clave1)
                    clave2 = claves[1].next_sibling.text
                    print(clave2)
                    clave3 = claves[2].next_sibling.text
                    print(clave3)
                    clave4 = 'none'
                    print(clave4)
                    clave5 = 'none'
                    print(clave5)
                    clave6 = 'none'
                    print(clave6)
            elif len(claves) == 6:
                clave1 = claves[0].next_sibling.text
                print(clave1)
                clave2 = claves[1].next_sibling.text
                print(clave2)
                clave3 = claves[2].next_sibling.text
                print(clave3)
                clave4 = claves[3].next_sibling.text
                print(clave4)
                clave5 = claves[4].next_sibling.text
                print(clave5)
                clave6 = claves[5].next_sibling.text
                print(clave6)
            else:
                clave1 = 'none'
                print(clave1)
                clave2 = 'none'
                print(clave2)
                clave3 = 'none'
                print(clave3)
                clave4 = 'none'
                print(clave4)
                clave5 = 'none'
                print(clave5)
                clave6 = 'none'
                print(clave6)
        else:
            clave1 = 'none'
            print(clave1)
            clave2 = 'none'
            print(clave2)
            clave3 = 'none'
            print(clave3)
            clave4 = 'none'
            print(clave4)
            clave5 = 'none'
            print(clave5)
            clave6 = 'none'
            print(clave6)

        if soup.find_all('td', text='dc.description') != []:
            resumen = soup.find_all('td', text='dc.description')[0].next_sibling.text
            print(resumen)
            try:
                summary = soup.find_all('td', text='dc.description')[1].next_sibling.text
                print(summary)
            except Exception as e:
                summary = 'none'
                print(summary)
        else:
            resumen = 'none'
            summary = 'none'
            print(resumen)
            print(summary)

        try:
            fecha_disponible = soup.find_all('td', text='dc.date.available')[0].next_sibling.text
            print(fecha_disponible)
        except Exception as e:
            fecha_disponible = 'none'
            print(fecha_disponible)

        try:
            curp_autor = soup.find_all('td', text='dc.creator.identificador')[0].next_sibling.text
            print(curp_autor)
        except Exception as e:
            curp_autor = 'none'
            print(curp_autor)
        
        try:
            curp_asesor = soup.find_all('td', text='dc.contributor.identificador')[0].next_sibling.text
            print(curp_asesor)
        except Exception as e:
            curp_asesor = 'none'
            print(curp_asesor)
            
            
        csv_writer.writerow([identificador, 
                            link_info,
                            nombre_recurso,
                            ruta_recurso,
                            titulo,
                            autor,
                            asesor,
                            facultad,
                            grado,
                            area1, area2,
                            clave1, clave2, clave3, clave4, clave5, clave6,
                            resumen, summary,
                            fecha_disponible,
                            curp_autor, curp_asesor])

csv_file.close() 
