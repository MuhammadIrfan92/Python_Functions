



def scrapper(url , chromedriverpath,finder ):
    from selenium import webdriver
    PATH = chromedriverpath
    driver = webdriver.Chrome(PATH)

    driver.get(url)
    print(driver.title)

    data = driver.find_element_by_id(finder)
    return data.text


if __name__ == "__main__":
    import csv
    chromedriverpath = "C:\Program Files (x86)\chromedriver.exe"
    url =  "https://finance.yahoo.com/quote/%5EDJI?p=%5EDJI"
    finder="Lead-4-QuoteHeader-Proxy"
    data = scrapper(url, chromedriverpath, finder)
    text_lis = data.split("\n")
    with open("data.csv",'w',newline="") as f:
        writer = csv.writer(f)
        for i in text_lis:
            writer.writerow(i)



