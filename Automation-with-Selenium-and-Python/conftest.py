import pytest
from selenium import webdriver

supported_languages = {
    "ar": "العربيّة",
    "ca": "català",
    "cs": "česky",
    "da": "dansk",
    "de": "Deutsch",
    "en-gb": "British English",
    "el": "Ελληνικά",
    "es": "español",
    "fi": "suomi",
    "fr": "français",
    "it": "italiano",
    "ko": "한국어",
    "nl": "Nederlands",
    "pl": "polski",
    "pt": "Português",
    "pt-br": "Português Brasileiro",
    "ro": "Română",
    "ru": "Русский",
    "sk": "Slovensky",
    "uk": "Українська",
    "zh-hn": "简体中文"
}


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language:'ar','ca','cs','da','de','en-gb','el','es','fi',"
                          "'fr','it','ko','nl','pl','pt','pt-br','ro','ru','sk','uk','zh-cn'")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # можно было с этим, но я решил пойти другим путем :)
    # browser_language = request.config.getoption("language")
    # options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages':
    #                                           browser_language})

    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    if language in supported_languages:
        link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
        print(f"\nstart with language: {supported_languages[language]}({language}) browser for test..")
    else:
        joined_browsers = ', '.join(supported_languages.keys())
        raise pytest.UsageError(f"--language is invalid, supported languages: {joined_browsers}")

    yield link
