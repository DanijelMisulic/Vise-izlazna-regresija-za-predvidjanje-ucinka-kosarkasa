# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 00:37:32 2017

@author: Danijel
"""
from selenium import webdriver
import time 

chrome_path = "C:/Users/Danijel/Desktop/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

target = open('C:/Users/Danijel/Desktop/kvote/STATISTIKA.csv', 'a', encoding="utf-8")

with open("C:/Users/Danijel/Desktop/kvote/preostali linkovi.txt") as fajl:
    for line in fajl:
        driver.get(line)
        time.sleep(0.5)
        datum = driver.find_element_by_xpath("""//*[@id="utime"]""")

        domacin = driver.find_element_by_xpath("""//*[@id="flashscore_column"]/table/tbody/tr[1]/td[1]/span/a""")
        gost = driver.find_element_by_xpath("""//*[@id="flashscore_column"]/table/tbody/tr[1]/td[3]/span/a""")

        produzeci = driver.find_element_by_xpath("""//*[@id="flashscore_column"]/table/tbody/tr[3]/td""")

        rez_domacin = driver.find_element_by_xpath("""//*[@id="event_detail_current_result"]/span[1]""")
        rez_gost = driver.find_element_by_xpath("""//*[@id="event_detail_current_result"]/span[3]""")

        kvota_domacin = driver.find_element_by_xpath("""//*[@id="default-odds"]/tbody/tr[1]/td[2]/span""")
        kvota_gost = driver.find_element_by_xpath("""//*[@id="default-odds"]/tbody/tr[1]/td[3]/span""")


        broj_redova = driver.find_elements_by_xpath("""//*[@id="tab-player-statistics-0-statistic"]/div/div[1]/table/tbody/tr""")

        for i in range(1,len(broj_redova)+1):
            target.write(datum.text)
            target.write(",")
    
            target.write(domacin.text)
            target.write(",")
            target.write(gost.text)
            target.write(",")
    
            target.write(rez_domacin.text)
            target.write(",")
            target.write(rez_gost.text)
            target.write(",")
    
            target.write(produzeci.text)
            target.write(",")
    
            if produzeci.text == "Nakon produžetaka":
                produzetak_domacin = driver.find_element_by_xpath("""//*[@id="event_detail_current_result"]/span[4]/span[1]""")
                produzetak_gost = driver.find_element_by_xpath("""//*[@id="event_detail_current_result"]/span[4]/span[3]""")
                target.write(produzetak_domacin.text)
                target.write(",")
                target.write(produzetak_gost.text)
                target.write(",")
            else:
                target.write("/")
                target.write(",")
                target.write("/")
                target.write(",")
    
            target.write(kvota_domacin.text)
            target.write(",")
            target.write(kvota_gost.text)
            target.write(",")
    
            xpath = """//*[@id="tab-player-statistics-0-statistic"]/div/div[1]/table/tbody/tr[""" + str(i) + """]/td[1]"""
            xpath1 = """//*[@id="tab-player-statistics-0-statistic"]/div/div[1]/table/tbody/tr[""" + str(i) + """]/td[2]"""
            tabela_vr = driver.find_element_by_xpath(xpath)
            tabela_vr1 = driver.find_element_by_xpath(xpath1)

            target.write(tabela_vr.text)
            target.write(",")
            target.write(tabela_vr1.text)
            target.write(",")

            for j in range (3,17):
                vrednost = """//*[@id="player-statistics-basketball"]/tbody/tr[""" + str(i) + """]/td[""" + str(j) + """]"""
    
                tabela_vred = driver.find_element_by_xpath(vrednost)
                target.write(tabela_vred.text)
                target.write(",")

            target.write("\n")

target.close()

driver.close()
driver.quit()

   
