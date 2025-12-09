from pathlib import Path


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def read_prompt(agent_name: str, prompt_filename: str) -> str:
    prompt_file = (
        Path(__file__).parent / f"{agent_name}" / "prompts" / f"{prompt_filename}.md"
    )
    return prompt_file.read_text()


def crawl_website(url: str) -> str:
    """
    Use Selenium + headless Chrome to load a page and extract visible text.
    Works for JS-rendered sites.
    """
    # Configure headless Chrome
    options = Options()
    options.add_argument("--headless=new")  # modern headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)

        # Wait for JS to render (adjust as needed)
        time.sleep(3)

        # Extract all visible text
        body_text = driver.find_element(By.TAG_NAME, "body").text
        return body_text
    finally:
        driver.quit()


if __name__ == "__main__":
    # Test the crawl_website function
    url = "https://www.linkedin.com/in/ahsanikr/"
    content = crawl_website(url)
    print(content[:50000])
