from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from tkinter import messagebox
import mysql.connector
from threading import *
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager
import math
from bs4 import BeautifulSoup
import csv
from tkinter import *
from tkinter import simpledialog

window = Tk()
window.title("JustDial Scrapper")
window.geometry("925x500+300+200")
window.configure(bg='#fff')

config = {
    'user': "us4ysjqeg4frhsrm",
    'password': "B1aUz79uvSHr53C7VThr",
    'host': "bi63d9qn701g0iqwf9lx-mysql.services.clever-cloud.com",
    'database': "bi63d9qn701g0iqwf9lx"
}

mydb = mysql.connector.connect(**config)

now = datetime.now()
rty = now.strftime('%d/%m/%Y %I:%M:%S')

def threading1():

    t1 = Thread(target=sign)
    t1.start()

def threading2():

    t2 = Thread(target=log)
    t2.start()

def threading3():

    t3 = Thread(target=forgot)
    t3.start()

def sign():

    def threading8():

        t8 = Thread(target=sub)
        t8.start()

    def sub():

        a = user16.get()
        b = user29.get()
        c = user39.get()

        cursor2 = mydb.cursor()
        sql = f"SELECT user_email FROM tbl_user WHERE user_email='{b}'"
        cursor2.execute(sql)
        result = cursor2.fetchall()

        d = len(result)

        if d == 0:

            cursor1 = mydb.cursor()
            sql = "INSERT INTO tbl_user (user_name, user_email, user_password, stat) VALUES (%s ,%s, %s, %s)"
            val = (f"{a}", f"{b}", f"{c}", "Inactive")
            cursor1.execute(sql, val)
            mydb.commit()

            messagebox.showinfo('information', f'{b} is your new UID\n{c} is your new password')

        else:

            messagebox.showinfo('information', f'{b} user already exist')

    new = Toplevel(window)
    new.title("Signup")
    new.geometry("925x500+200+100")
    new.configure(bg='#fff')

    frame16 = Frame(new, width=550, height=550, bg='white')
    frame16.place(x=290, y=70)

    heading17 = Label(frame16, text="Sign In", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, "bold"))
    heading17.place(x=100, y=5)

    user16 = Entry(frame16, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user16.place(x=30, y=80)
    user16.insert(0, 'Name')

    Frame(frame16, width=295, height=2, bg="black").place(x=25, y=107)

    user29 = Entry(frame16, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user29.place(x=30, y=150)
    user29.insert(0, "Email Id")

    Frame(frame16, width=295, height=2, bg="black").place(x=25, y=177)

    user39 = Entry(frame16, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user39.place(x=30, y=217)
    user39.insert(0, "Password")

    Frame(frame16, width=295, height=2, bg="black").place(x=25, y=247)

    Button(frame16, width=39, pady=7, text="Submit", bg="#57a1f8", fg="white", border=0, command=threading8).place(x=36,
                                                                                                                   y=305)


def forgot():

    def threading6():

        t6 = Thread(target=verify)
        t6.start()

    def verify():

        z = user11.get()

        cursor5 = mydb.cursor()
        sql3 = f"SELECT user_email FROM tbl_user WHERE user_email='{z}'"
        cursor5.execute(sql3)
        result5 = cursor5.fetchall()

        y = len(result5)

        if y == 0:

            messagebox.showinfo('information', f'{z} user does not exist')

        else:

            def threading7():

                t7 = Thread(target=ver2)
                t7.start()

            def ver2():

                x = user12.get()
                m = user21.get()

                if x == m:

                    cursor440 = mydb.cursor()
                    sql_update_query = f"""Update tbl_user set user_password = '{x}' where user_email = '{z}'"""
                    cursor440.execute(sql_update_query)
                    mydb.commit()

                    messagebox.showinfo('information', f'{x} is your new password')

                else:

                    messagebox.showinfo('information', 'Enter same password')

            new2 = Toplevel(window)

            new2.title("Verification")

            new2.geometry("925x500+200+100")

            new2.configure(bg='#fff')

            frame12 = Frame(new2, width=550, height=550, bg='white')

            frame12.place(x=290, y=70)

            heading12 = Label(frame12, text="Create new passsword", fg="#57a1f8", bg="white",
                              font=('Microsoft YaHei UI Light', 23, "bold"))

            heading12.place(x=10, y=5)

            user12 = Entry(frame12, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))

            user12.place(x=30, y=80)

            user12.insert(0, 'Create new password')

            Frame(frame12, width=295, height=2, bg="black").place(x=25, y=107)

            user21 = Entry(frame12, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))

            user21.place(x=30, y=130)

            user21.insert(0, "Reconfirm password")

            Frame(frame12, width=295, height=2, bg="black").place(x=25, y=157)

            Button(frame12, width=39, pady=7, text="Submit", bg="#57a1f8", fg="white", border=0,
                   command=threading7).place(x=35, y=200)

    new1 = Toplevel(window)

    new1.title("Forgot password")

    new1.geometry("925x500+200+100")

    new1.configure(bg='#fff')

    frame1 = Frame(new1, width=550, height=550, bg='white')

    frame1.place(x=290, y=70)

    heading1 = Label(frame1, text="Forgot password", fg="#57a1f8", bg="white",
                     font=('Microsoft YaHei UI Light', 23, "bold"))

    heading1.place(x=30, y=0)

    user11 = Entry(frame1, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))

    user11.place(x=30, y=80)

    user11.insert(0, 'Email Id')

    Frame(frame1, width=295, height=2, bg="black").place(x=25, y=107)

    Button(frame1, width=39, pady=7, text="Verify", bg="#57a1f8", fg="white", border=0, command=threading6).place(x=35,
                                                                                                                  y=150)


def log():

    global ac, title, bc, title1, nxyz, title2, dc, title3, ec, title4, fc, title5, gc, title6, hc, title7, ic, title8, jc, title9, text, text1, text2, text3, text4, text5, text6, text7, text8, text9, soup2, tet3, ti8, zsgc, texts6, title6s, text7s, hcs, title7s, title7s, text8s, text9s, jcs, jcs, title9s
    global khcs, jcs

    e = user1.get()

    f = user2.get()

    cursor558 = mydb.cursor()

    sql558 = f"SELECT stat FROM tbl_user WHERE stat='Active'"

    cursor558.execute(sql558)

    result558 = cursor558.fetchall()

    z = len(result558)

    cursor3 = mydb.cursor()

    sql1 = f"SELECT user_email FROM tbl_user WHERE user_email='{e}'"

    cursor3.execute(sql1)

    result1 = cursor3.fetchall()

    g = len(result1)

    if z == 0:

        if g == 0:

            messagebox.showinfo('information', f'{e} user does not exist')

        else:

            cursor4 = mydb.cursor()

            sql2 = f"SELECT user_password FROM tbl_user WHERE user_email='{e}'"

            cursor4.execute(sql2)

            result2 = cursor4.fetchall()

            i = result2[0][0]

            if f == i:

                cursor445 = mydb.cursor()

                sql_update_query1 = f"""Update tbl_user set Time = '{rty}' where user_email = '{e}'"""

                cursor445.execute(sql_update_query1)

                mydb.commit()

                cursor446 = mydb.cursor()

                sql_update_query2 = f"""Update tbl_user set stat = 'Active' where user_email = '{e}'"""

                cursor446.execute(sql_update_query2)

                mydb.commit()

                def threading5():

                    t5 = Thread(target=logoutyy)

                    t5.start()

                def logoutyy():

                    cursor447 = mydb.cursor()

                    sql_update_query9999 = f"""Update tbl_user set stat = 'Inactive' where user_email = '{e}'"""

                    cursor447.execute(sql_update_query9999)

                    mydb.commit()

                    messagebox.showinfo('information', 'You have successfully logged out')

                new50 = Toplevel(window)

                new50.title("Log out portal")

                new50.geometry("925x500+200+100")

                new50.configure(bg='#fff')

                frame166 = Frame(new50, width=550, height=550, bg='white')

                frame166.place(x=220, y=70)

                heading177 = Label(frame166, text="Click on the below button to log out", fg="#57a1f8", bg="white",
                                   font=('Microsoft YaHei UI Light', 23, "bold"))

                heading177.place(x=0, y=5)

                Button(frame166, width=39, pady=7, text="Log Out", bg="#57a1f8", fg="white", border=0,
                       command=threading5).place(x=105, y=204)

                newWin = Tk()

                newWin.withdraw()

                r123 = simpledialog.askstring(title="variable 1", prompt="Enter the location", parent=newWin)

                newWin.destroy()

                newWin1 = Tk()

                newWin1.withdraw()

                r1234 = simpledialog.askstring(title="variable 2", prompt="Enter the keyword to be searched",
                                               parent=newWin1)

                newWin1.destroy()

                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
                service_count = 1
                dict_service = {}
                fields = ['Name', 'Phone', 'Address', 'Status']
                out_file = open('JustDial.csv', 'w')
                csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)

                uq = f'https://www.justdial.com/{r123}'
                uy = f'/search?q={r1234}'
                u1 = uq + uy

                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.maximize_window()
                driver.delete_all_cookies()

                driver.get(u1)
                lenOfPage = driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                match = False
                while (match == False):
                    lastCount = lenOfPage
                    lenOfPage = driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount == lenOfPage:
                        match = True
                li_tags = driver.find_elements(By.CLASS_NAME, 'cntanr')
                zb = [li.find_element(By.CLASS_NAME, 'lng_cont_name').text for li in li_tags]
                az = [li.find_element(By.XPATH, './/a').get_attribute('href') for li in li_tags]
                az1 = len(az)
                for n in range(az1):
                    we = requests.get(f"{az[n]}/delay/10", headers=headers, timeout=120)
                    axz = ((we.status_code))
                    b = int(axz / 10 ** int(math.log10(axz)))
                    print(b)
                    if ((b == 2)):
                        soup = BeautifulSoup(we.text, "html.parser")
                        uext = soup.find_all(name="a", class_="mapicn")
                        for link in uext:
                          title = link.get('title')
                        filel = len(soup.find_all('style', {"type": "text/css"}, text=True))
                        if filel >=2:
                            text = soup.find_all('style', {"type": "text/css"}, text=True)[1]
                        data = text.contents[0].split('smoothing:grayscale}', 1)[1].split('\n')[0]
                        icon_items = [i.split(':')[0] for i in data.split('.') if len(i) > 0]
                        items = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ')', '(']
                        full_list = dict(zip(icon_items, items))
                        phone_numbers = soup.find_all('span', {'class': 'telnowpr'})
                        for iv in phone_numbers:
                            numbers = iv.find_all('span')
                            number = [full_list[y.attrs['class'][1]] for y in numbers]
                            ac = (''.join([str(elem) for elem in number]))
                        if ac is not None:
                            dict_service['Phone'] = ac
                        if title != None:
                            dict_service['Address'] = title
                        if b != None:
                            dict_service['Status'] = b
                        csvwriter.writerow(dict_service)
                        print("#" + str(service_count) + " ", dict_service)
                        service_count += 1
                driver.close()

                driver1 = webdriver.Chrome(ChromeDriverManager().install())
                driver1.maximize_window()
                driver1.delete_all_cookies()
                url1 = f'{u1}/page-2'
                driver1.get(u1)
                time.sleep(3)
                lenOfPage1 = driver1.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                match1 = False
                while (match1 == False):
                    lastCount1 = lenOfPage1
                    lenOfPage1 = driver1.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount1 == lenOfPage1:
                        match1 = True
                li_tags1 = driver1.find_elements(By.CLASS_NAME, 'cntanr')
                bz = [li1.find_element(By.XPATH, './/a').get_attribute('href') for li1 in li_tags1]
                bz1 = len(bz)
                for n1 in range(bz1):
                    we1 = requests.get(f"{bz[n1]}/delay/10", headers=headers, timeout=120)
                    axz1 = ((we1.status_code))
                    b1 = int(axz1 / 10 ** int(math.log10(axz1)))
                    print(b1)
                    if ((b1 == 2)):
                        soup1 = BeautifulSoup(we1.text, "html.parser")
                        uext1 = soup1.find_all(name="a", class_="mapicn")
                        for link1 in uext1:
                            title1 = link1.get('title')
                        filel1 = len(soup1.find_all('style', {"type": "text/css"}, text=True))
                        if filel1 >=2:
                            text1 = soup1.find_all('style', {"type": "text/css"}, text=True)[1]
                        data1 = text1.contents[0].split('smoothing:grayscale}', 1)[1].split('\n')[0]
                        icon_items1 = [i1.split(':')[0] for i1 in data1.split('.') if len(i1) > 0]
                        items1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ')', '(']
                        full_list1 = dict(zip(icon_items1, items1))
                        phone_numbers1 = soup1.find_all('span', {'class': 'telnowpr'})
                        for iv1 in phone_numbers1:
                            numbers1 = iv1.find_all('span')
                            number1 = [full_list1[y1.attrs['class'][1]] for y1 in numbers1]
                            bc = (''.join([str(elem1) for elem1 in number1]))
                        if bc is not None:
                            dict_service['Phone'] = bc
                        if title1 != None:
                            dict_service['Address'] = title1
                        if b1 != None:
                            dict_service['Status'] = b1
                        csvwriter.writerow(dict_service)
                        print("#" + str(service_count) + " ", dict_service)
                        service_count += 1
                driver1.close()

                driver2 = webdriver.Chrome(ChromeDriverManager().install())
                driver2.maximize_window()
                driver2.delete_all_cookies()
                url2 = f'{u1}/page-3'
                driver2.get(url2)
                time.sleep(3)
                lenOfPage2 = driver2.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                match2 = False
                while (match2 == False):
                    lastCount2 = lenOfPage2
                    lenOfPage2 = driver2.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount2 == lenOfPage2:
                        match2 = True
                li_tags2 = driver2.find_elements(By.CLASS_NAME, 'cntanr')
                cb = [li2.find_element(By.CLASS_NAME, 'lng_cont_name').text for li2 in li_tags2]
                cz = [li2.find_element(By.XPATH, './/a').get_attribute('href') for li2 in li_tags2]
                cz1 = len(cz)
                for n2 in range(cz1):
                    we2 = requests.get(f"{cz[n2]}/delay/10", headers=headers, timeout=120)
                    axz2 = ((we2.status_code))
                    b2 = int(axz2 / 10 ** int(math.log10(axz2)))
                    print(b2)
                    if ((b2 == 2)):
                        soup2 = BeautifulSoup(we2.content, "html.parser")
                        urxt2 = soup2.find_all(name="a", class_="mapicn")
                        for link2 in urxt2:
                            title2 = link2.get('title')
                        filel2 = len(soup2.find_all('style', {"type": "text/css"}, text=True))
                        if filel2 >=2:
                            text2 = soup2.find_all('style', {"type": "text/css"}, text=True)[1]
                        data2 = text2.contents[0].split('smoothing:grayscale}', 1)[1].split('\n')[0]
                        icon_items2 = [i2.split(':')[0] for i2 in data2.split('.') if len(i2) > 0]
                        items2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ')', '(']
                        full_list2 = dict(zip(icon_items2, items2))
                        phone_numbers2 = soup2.find_all('span', {'class': 'telnowpr'})
                        for iv2 in phone_numbers2:
                            numbers2 = iv2.find_all('span')
                            number2 = [full_list2[yq2.attrs['class'][1]] for yq2 in numbers2]
                            nxyz = (''.join([str(elem2) for elem2 in number2]))
                        if nxyz is not None:
                            dict_service['Phone'] = nxyz
                        if title2 is not None:
                            dict_service['Address'] = title2
                        if b2 != None:
                            dict_service['Status'] = b2
                        csvwriter.writerow(dict_service)
                        print("#" + str(service_count) + " ", dict_service)
                        service_count += 1
                driver2.close()

                driver3 = webdriver.Chrome(ChromeDriverManager().install())
                driver3.maximize_window()
                driver3.delete_all_cookies()
                url3 = f'{u1}/page-4'
                driver3.get(url3)
                lenOfPage3 = driver3.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                match3 = False
                while (match3 == False):
                    lastCount3 = lenOfPage3
                    lenOfPage3 = driver3.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount3 == lenOfPage3:
                        match3 = True
                li_tags3 = driver3.find_elements(By.CLASS_NAME, 'cntanr')
                db = [li3.find_element(By.CLASS_NAME, 'lng_cont_name').text for li3 in li_tags3]
                dz = [li3.find_element(By.XPATH, './/a').get_attribute('href') for li3 in li_tags3]
                dz1 = len(dz)
                for n3 in range(dz1):
                    we3 = requests.get(f"{dz[n3]}/delay/10", headers=headers, timeout=120)
                    axz3 = ((we3.status_code))
                    b3 = int(axz3 / 10 ** int(math.log10(axz3)))
                    print(b3)
                    if ((b3 == 2)):
                        soup3 = BeautifulSoup(we3.content, "html.parser")
                        uext3 = soup3.find_all(name="a", class_="mapicn")
                        for link3 in uext3:
                            title3 = link3.get('title')
                        filel3 = len(soup3.find_all('style', {"type": "text/css"}, text=True))
                        if filel3 >= 2:
                            tet3 = soup3.find_all('style', {"type": "text/css"}, text=True)[1]
                        data3 = tet3.contents[0].split('smoothing:grayscale}', 1)[1].split('\n')[0]
                        icon_items3 = [i3.split(':')[0] for i3 in data3.split('.') if len(i3) > 0]
                        items3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ')', '(']
                        full_list3 = dict(zip(icon_items3, items3))
                        phone_numbers3 = soup3.find_all('span', {'class': 'telnowpr'})
                        for iv3 in phone_numbers3:
                            numbers3 = iv3.find_all('span')
                            number3 = [full_list3[y3.attrs['class'][1]] for y3 in numbers3]
                            dc = (''.join([str(elem3) for elem3 in number3]))
                        if dc is not None:
                            dict_service['Phone'] = dc
                        if title3 is not None:
                            dict_service['Address'] = title3
                        if b3 != None:
                            dict_service['Status'] = b3
                        csvwriter.writerow(dict_service)
                        print("#" + str(service_count) + " ", dict_service)
                        service_count += 1
                driver3.close()

                driver4 = webdriver.Chrome(ChromeDriverManager().install())
                driver4.maximize_window()
                driver4.delete_all_cookies()
                url4 = f'{u1}/page-5'
                driver4.get(url4)
                lenOfPage4 = driver4.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                match4 = False
                while (match4 == False):
                    lastCount4 = lenOfPage4
                    lenOfPage4 = driver4.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount4 == lenOfPage4:
                        match4 = True
                li_tags4 = driver4.find_elements(By.CLASS_NAME, 'cntanr')
                eb = [li4.find_element(By.CLASS_NAME, 'lng_cont_name').text for li4 in li_tags4]
                ez = [li4.find_element(By.XPATH, './/a').get_attribute('href') for li4 in li_tags4]
                ez1 = len(ez)
                for n4 in range(ez1):
                    we4 = requests.get(f"{ez[n4]}/delay/10", headers=headers, timeout=120)
                    axz4 = ((we4.status_code))
                    b4 = int(axz4 / 10 ** int(math.log10(axz4)))
                    print(b4)
                    if ((b4 == 2)):
                        soup4 = BeautifulSoup(we4.content, "html.parser")
                        uext4 = soup4.find_all(name="a", class_="mapicn")
                        for link4 in uext4:
                            title4 = link4.get('title')
                        filel4 = len(soup4.find_all('style', {"type": "text/css"}, text=True))
                        if filel4 >= 2:
                            text4 = soup4.find_all('style', {"type": "text/css"}, text=True)[1]
                        data4 = text4.contents[0].split('smoothing:grayscale}', 1)[1].split('\n')[0]
                        icon_items4 = [i4.split(':')[0] for i4 in data4.split('.') if len(i4) > 0]
                        items4 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ')', '(']
                        full_list4 = dict(zip(icon_items4, items4))
                        phone_numbers4 = soup4.find_all('span', {'class': 'telnowpr'})
                        for iv4 in phone_numbers4:
                            numbers4 = iv4.find_all('span')
                            number4 = [full_list4[y4.attrs['class'][1]] for y4 in numbers4]
                            ec = (''.join([str(elem4) for elem4 in number4]))
                        if ec != None:
                            dict_service['Phone'] = ec
                        if title4 is not None:
                            dict_service['Address'] = title4
                        if b4 != None:
                            dict_service['Status'] = b4
                        csvwriter.writerow(dict_service)
                        print("#" + str(service_count) + " ", dict_service)
                        service_count += 1
                driver4.close()

                driver5 = webdriver.Chrome(ChromeDriverManager().install())
                driver5.maximize_window()
                driver5.delete_all_cookies()
                url5 = f'{u1}/page-6'
                driver5.get(url5)
                time.sleep(3)
                lenOfPage5 = driver5.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                match5 = False
                while (match5 == False):
                    lastCount5 = lenOfPage5
                    lenOfPage5 = driver5.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount5 == lenOfPage5:
                        match5 = True
                li_tags5 = driver5.find_elements(By.CLASS_NAME, 'cntanr')
                fb = [li5.find_element(By.CLASS_NAME, 'lng_cont_name').text for li5 in li_tags5]
                fz = [li5.find_element(By.XPATH, './/a').get_attribute('href') for li5 in li_tags5]
                fz1 = len(fz)
                for n5 in range(fz1):
                    we5 = requests.get(f"{fz[n5]}/delay/10", headers=headers, timeout=120)
                    axz5 = ((we5.status_code))
                    b5 = int(axz5 / 10 ** int(math.log10(axz5)))
                    print(b5)
                    if ((b5 == 2)):
                        soup5 = BeautifulSoup(we5.content, "html.parser")
                        uext5 = soup5.find_all(name="a", class_="mapicn")
                        for link5 in uext5:
                            title5 = link5.get('title')
                        filel5 = len(soup5.find_all('style', {"type": "text/css"}, text=True))
                        if filel5 >= 2:
                            text5 = soup5.find_all('style', {"type": "text/css"}, text=True)[1]
                        data5 = text5.contents[0].split('smoothing:grayscale}', 1)[1].split('\n')[0]
                        icon_items5 = [i5.split(':')[0] for i5 in data5.split('.') if len(i5) > 0]
                        items5 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ')', '(']
                        full_list5 = dict(zip(icon_items5, items5))
                        phone_numbers5 = soup5.find_all('span', {'class': 'telnowpr'})
                        for iv5 in phone_numbers5:
                            numbers5 = iv5.find_all('span')
                            number5 = [full_list5[y5.attrs['class'][1]] for y5 in numbers5]
                            fc = (''.join([str(elem5) for elem5 in number5]))
                        if fc is not None:
                            dict_service['Phone'] = fc
                        if title5 is not None:
                            dict_service['Address'] = title5
                        if b5 != None:
                            dict_service['Status'] = b5
                        csvwriter.writerow(dict_service)
                        print("#" + str(service_count) + " ", dict_service)
                        service_count += 1
                driver5.close()

                driver6s = webdriver.Chrome(ChromeDriverManager().install())
                driver6s.maximize_window()
                driver6s.delete_all_cookies()
                url6s = f'{u1}/page-7'
                driver6s.get(url6s)
                time.sleep(3)
                lenOfPage6s = driver6s.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                match6s = False
                while (match6s == False):
                    lastCount6s = lenOfPage6s
                    lenOfPage6s = driver6s.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount6s == lenOfPage6s:
                        match6s = True
                li_tags6s = driver6s.find_elements(By.CLASS_NAME, 'cntanr')

                gsz = [li6s.find_element(By.XPATH, './/a').get_attribute('href') for li6s in li_tags6s]
                gsz1 = len(gsz)
                for n6s in range(gsz1):
                    wes6 = requests.get(f"{gsz[n6s]}/delay/10", headers=headers, timeout=120)
                    axsz6 = ((wes6.status_code))
                    bs6 = int(axsz6 / 10 ** int(math.log10(axsz6)))
                    print(bs6)
                    if ((bs6 == 2)):
                        soups6 = BeautifulSoup(wes6.content, "html.parser")
                        uexts6 = soups6.find_all(name="a", class_="mapicn")
                        for link6s in uexts6:
                            title6s = link6s.get('title')
                        filels6 = len(soups6.find_all('style', {"type": "text/css"}, text=True))
                        if filels6 >= 2:
                            texts6 = soups6.find_all('style', {"type": "text/css"}, text=True)[1]
                        datas6 = texts6.contents[0].split('smoothing:grayscale}', 1)[1].split('\n')[0]
                        icon_items6s = [i6s.split(':')[0] for i6s in datas6.split('.') if len(i6s) > 0]
                        items6s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ')', '(']
                        full_list6s = dict(zip(icon_items6s, items6s))
                        phone_numbers6s = soups6.find_all('span', {'class': 'telnowpr'})
                        for iv6s in phone_numbers6s:
                            numbers6s = iv6s.find_all('span')
                            number6s = [full_list6s[y6s.attrs['class'][1]] for y6s in numbers6s]
                            zsgc = (''.join([str(elem6s) for elem6s in number6s]))
                        if zsgc is not None:
                            dict_service['Phone'] = zsgc
                        if title6s is not None:
                            dict_service['Address'] = title6s
                        if bs6 != None:
                            dict_service['Status'] = bs6
                        csvwriter.writerow(dict_service)
                        print("#" + str(service_count) + " ", dict_service)
                        service_count += 1
                driver6s.close()

                driver7s = webdriver.Chrome(ChromeDriverManager().install())
                driver7s.maximize_window()
                driver7s.delete_all_cookies()
                url7s = f'{u1}/page-8'
                driver7s.get(url7s)
                time.sleep(3)
                lenOfPage7s = driver7s.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                match7s = False
                while (match7s == False):
                    lastCount7s = lenOfPage7s
                    lenOfPage7s = driver7s.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                    if lastCount7s == lenOfPage7s:
                        match7s = True
                li_tags7s = driver7s.find_elements(By.CLASS_NAME, 'cntanr')
                hb = [li7s.find_element(By.CLASS_NAME, 'lng_cont_name').text for li7s in li_tags7s]
                hzs = [li7s.find_element(By.XPATH, './/a').get_attribute('href') for li7s in li_tags7s]
                hz1s = len(hzs)
                for n7s in range(hz1s):
                    we7s = requests.get(f"{hzs[n7s]}/delay/10", headers=headers, timeout=120)
                    axz7s = ((we7s.status_code))
                    b7s = int(axz7s / 10 ** int(math.log10(axz7s)))
                    print(b7s)
                    if ((b7s == 2)):
                        soul7s = BeautifulSoup(we7s.content, "html.parser")
                        uext7s = soul7s.find_all(name="a", class_="mapicn")
                        for link7s in uext7s:
                            title7s = link7s.get('title')
                        filel7s = len(soul7s.find_all('style', {"type": "text/css"}, text=True))
                        if filel7s >= 2:
                            text7s = soul7s.find_all('style', {"type": "text/css"}, text=True)[1]
                        data7s = text7s.contents[0].split('smoothing:grayscale}', 1)[1].split('\n')[0]
                        icon_items7s = [i7s.split(':')[0] for i7s in data7s.split('.') if len(i7s) > 0]
                        items7s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ')', '(']
                        full_list7s = dict(zip(icon_items7s, items7s))
                        phone_numbers7s = soul7s.find_all('span', {'class': 'telnowpr'})
                        for iv7s in phone_numbers7s:
                            numbers7s = iv7s.find_all('span')
                            number7s = [full_list7s[y7s.attrs['class'][1]] for y7s in numbers7s]
                            hcs = (''.join([str(elem7s) for elem7s in number7s]))
                        if hcs is not None:
                            dict_service['Phone'] = hcs
                        if title7s is not None:
                            dict_service['Address'] = title7s
                        if b7s != None:
                            dict_service['Status'] = b7s
                        csvwriter.writerow(dict_service)
                        print("#" + str(service_count) + " ", dict_service)
                        service_count += 1
                driver7s.close()


                out_file.close()

            else:

                messagebox.showinfo('information', 'Wrong password')

    else:

        messagebox.showinfo('information', 'Somebody is already using the software')


img = PhotoImage(file="login.png")
Label(window, image=img, bg='white').place(x=50, y=50)

frame = Frame(window, width=350, height=350, bg='white')
frame.place(x=490, y=70)

heading = Label(frame, text="JustDial Scrapper", fg="#57a1f8", bg="white",
                font=('Microsoft YaHei UI Light', 23, "bold"))
heading.place(x=30, y=5)

user1 = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user1.place(x=30, y=80)
user1.insert(0, 'UID')

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

user2 = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user2.place(x=30, y=150)
user2.insert(0, "Password")
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, pady=7, text="Log In", bg="#57a1f8", fg="white", border=0, command=threading2).place(x=35,
                                                                                                             y=204)
Button(frame, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=threading1).place(x=35,
                                                                                                              y=255)
Button(frame, width=39, pady=7, text="Forgot password", bg="#57a1f8", fg="white", border=0, command=threading3).place(
    x=35, y=305)
window.mainloop()