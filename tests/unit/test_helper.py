from unittest.mock import patch, MagicMock
from src.helper import crawl_website
import pytest
from selenium.webdriver.common.by import By


@patch("src.helper.webdriver.Chrome")
def test_crawl_website(mock_chrome_driver: MagicMock):
    """
    Tests the crawl_website function by mocking the selenium webdriver.

    This test ensures that the function correctly initializes the Chrome driver,
    navigates to the given URL, extracts the body text, and properly quits
    the driver, all without actually making any network requests or needing
    a real browser.
    """
    # Arrange
    url = "http://example.com"
    expected_text = "This is the body of the test website."

    # Configure the mock driver and its methods
    mock_driver_instance = MagicMock()
    mock_element = MagicMock()
    mock_element.text = expected_text
    mock_driver_instance.find_element.return_value = mock_element

    # Set the return value of the patched webdriver.Chrome call
    mock_chrome_driver.return_value = mock_driver_instance

    # Act
    actual_text = crawl_website(url)

    # Assert
    assert actual_text == expected_text

    # Verify that the driver was initialized and used as expected
    mock_chrome_driver.assert_called_once()
    options_arg = mock_chrome_driver.call_args.kwargs.get("options")
    assert options_arg is not None
    assert "--headless=new" in options_arg.arguments

    mock_driver_instance.get.assert_called_with(url)
    mock_driver_instance.find_element.assert_called_with(By.TAG_NAME, "body")
    mock_driver_instance.quit.assert_called_once()

