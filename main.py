import requests, openpyxl
from bs4 import BeautifulSoup

# storing the page for processing
def download_site():
    print("Write site id here (like org.wikipedia):")
    app_id = input()
    url = "https://play.google.com/store/apps/details?id=" + app_id

# adding headers to simulate a person
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0"
    }

    req = requests.get(url, headers=headers)
    my_page = req.text


    with open("index.html", "w", encoding="utf-8") as file:
        file.write(my_page)

# parsing the file and searching for the attributes we need

def get_attr():
    with open("index.html", encoding="utf-8") as file:
        src = file.read()


    soup = BeautifulSoup(src, "lxml")
    app_name = soup.find(class_="AfwdI")
    comp_name = soup.find(class_="Vbfug auoIOc")
    star_assesment = soup.find(class_="TT9eCd")
    reviews = soup.find(class_="g1rdde")
    downloads = soup.find(class_="wVqUob").find_next_sibling()
    #print("List attr:\n")
    #print(f"{app_name.text}\n{comp_name.text}\n{star_assesment.text}\n{reviews.text}\n{downloads.text}")
    write_data_to_xl(app_name.text, comp_name.text, star_assesment.text, reviews.text, downloads.text)


# writing a file to an excel spreadsheet
def write_data_to_xl(app, comp, star, rev, downloads):
    wb = openpyxl.load_workbook('data_app.xlsx')
    sheet = wb['Sheet1']

    # Find the next empty row
    next_row = sheet.max_row + 1

    sheet[f'A{next_row}'] = app
    sheet[f'B{next_row}'] = comp
    sheet[f'C{next_row}'] = star
    sheet[f'D{next_row}'] = rev
    sheet[f'E{next_row}'] = downloads
    wb.save('data_app.xlsx')



download_site()
get_attr()



