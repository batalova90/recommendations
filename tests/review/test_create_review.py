import pytest
from selenium.webdriver.common.by import By


# надо удалять обзоры
testdata = [
    {"name":  "Test review",
     "rating": "4",
     "slug": "test1",
     "text": "Check test",
     "path_image": "/home/anastasiya/ittransition/recommendations/tests/review/image/solyanka.jpg",
     "review_name": "Test 1"},
    
    {"name": "Test review 2",
     "rating": "3",
     "slug": "test2",
     "text": "Check test",
     "path_image": "/home/anastasiya/ittransition/recommendations/tests/review/image/venom.jpg",
     "review_name": "Test 2"},

    {"name": "Test review 3",
     "rating": "2",
     "slug": "test3",
     "text": "Check test",
     "path_image": "/home/anastasiya/ittransition/recommendations/tests/review/image/idiot.jpg",
     "review_name": "Test 3"},

    {"name": "Test review 4",
     "rating": "1",
     "slug": "test4",
     "text": "Check test",
     "path_image": "/home/anastasiya/ittransition/recommendations/tests/review/image/maer.jpg",
     "review_name": "Test 4"}

]


@pytest.mark.parametrize("review", testdata, ids=[repr(x) for x in testdata])
def test_create_review(app, review):
    app.open_create_review_page()
    app.driver.find_element(
            By.ID,
            "id_creation-name"
    ).send_keys(review["name"])
    app.driver.find_element(
            By.ID,
            "id_creation-rating"
    ).send_keys(review["rating"])
    dropdown = app.driver.find_element(
            By.ID,
            "id_creation-category"
    )
    dropdown.find_element(
            By.XPATH,
            "//option[. = 'movie' ]").click()
    app.driver.find_element(
            By.CSS_SELECTOR,
            "option:nth-child(2)"
    ).click()
    app.driver.find_element(
            By.ID,
            "id_creation-slug"
    ).send_keys(review["slug"])
    app.driver.find_element(
            By.ID,
            "id_review-text"
    ).send_keys(review["text"])
    app.driver.find_element(
            By.ID,
            "id_review-name"
    ).send_keys(review["review_name"])
    app.driver.find_element(
            By.CSS_SELECTOR,
            ".btn"
    ).click()
    app.driver.find_element_by_xpath(
            "//input[@type='file']"
    ).send_keys(review["path_image"])
    app.driver.find_element(
            By.CSS_SELECTOR, ".btn"
    ).click()
    app.open_homepage()
    last_review_name = app.driver.find_element(
            By.CSS_SELECTOR,
            ".text-muted:nth-child(1)"
    ).text

    assert review["review_name"] == last_review_name, "The review were not created"
