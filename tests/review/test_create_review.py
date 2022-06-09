import pytest
from selenium.webdriver.common.by import By

from data.add_review import testdata

# надо удалять обзоры

@pytest.mark.parametrize(
        "review",
        testdata,
        ids=[repr(x) for x in testdata]
)
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
    app.driver.implicitly_wait(2)
    app.open_homepage()
    last_review_name = app.driver.find_element(
            By.CSS_SELECTOR,
            ".text-muted:nth-child(1)"
    ).text

    assert review["review_name"] == last_review_name, "The review were not created"


def test_matches_db_ui(app, db):
    db_set = set(db.get_review_name())
    testdata_set = set([x.get("review_name") for x in (testdata)])
    assert testdata_set.issubset(db_set), "Database doesn't match test data"
