from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup


def browser_setup():
    """
    Sets up Selenium to use Firefox and all the needed options for it
    :return: selenium driver to scrape with
    """
    fp = webdriver.FirefoxProfile()

    options = FirefoxOptions()
    options.headless = True  # set true to run in bg
    caps = DesiredCapabilities().FIREFOX
    caps["marionette"] = True  # set true to run in bg
    driver = webdriver.Firefox(firefox_profile=fp, capabilities=caps, executable_path=GeckoDriverManager().install(),
                               options=options)
    return driver


def scrape(position='developer', location='vilnius', seniority=None):
    """
    Sets up the driver, if connection is established will get the links to top projects,
    then uses those links to get the download links and filenames. Finally, loops through the projects and downloads
    them to a specified directory.
    :return: None
    """
    driver = browser_setup()
    try:
        get_jobs(driver, position, location, seniority)
    except Exception as e:
        print(e)
    finally:
        driver.quit()


def get_jobs(driver, position, location, seniority):
    """
    Goes to SourceForge filters to only windows suitable software. Gets the links to the given number of projects +25
    :param location: (str) What position are you looking for?
    :param position: (str) Where would you like to work - type city or country?
    :param seniority: (str) seniority - optional
    :param driver: Set up selenium driver
    :return: List of found jobs matching the search terms
    """
    url = f"https://www.linkedin.com/jobs/search/?keywords={position}&location={location}"
    driver.get(url)
    page_source = driver.page_source
    print("Searching for jobs!")
    soup = BeautifulSoup(page_source, "html.parser")
    jobs = list()
    #while check_exists_by_css(driver, 'infinite-scroller__show-more-button'):
    results = soup.find_all('a', {'class': 'base-card__full-link'}, href=True)
    for item in results:
        title = item.find('span').text.strip()
        link = item['href']
        job = [title, link]
        jobs.append(jobs)
    print(len(jobs))
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Load more results']"))).click()
    return jobs


#
# start_urls = [f'https://www.linkedin.com/jobs/search/?keywords={position}&location={location}',
#               f'https://eurojobs.com/search-results-jobs/?action=search&listing_type%5Bequal%5D=Job&keywords%5Ball_words%5D={position}&Location%5Blocation%5D%5Bvalue%5D={location}&Location%5Blocation%5D%5Bradius%5D=10',
#               f'https://www.eurotechjobs.com/job_search/keyword/{position}/keyword_location/{location}',
#               ]


def check_exists_by_css(driver, selector):
    try:
        driver.find_element(By.CSS_SELECTOR, selector)
    except NoSuchElementException:
        return False
    return True
