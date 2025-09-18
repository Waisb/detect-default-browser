from winreg import *

def get_default_browser():
    """Возвращает windows ProgId браузера по умолчанию"""
    # Only for Windows OS
    # Он вернёт ChromeHTML для Chrome, FirefoxURL для Firefox и IE.HTTP для Internet Explorer.
    try:
        with OpenKey(HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice") as key:
            browser = QueryValueEx(key, 'Progid')[0]
            return browser
    except Exception as e:
        return False



def get_driver_by_browser(Progid):
    from selenium import webdriver

    if Progid == "ChromeHTML":
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        from selenium.webdriver.chrome.service import Service as ChromeService

        options = ChromeOptions()
        options.accept_insecure_certs = True
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")

        service = ChromeService("chromedriver.exe")
        return webdriver.Chrome(service=service, options=options)

    elif Progid == "FirefoxURL":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        from selenium.webdriver.firefox.service import Service as FirefoxService

        options = FirefoxOptions()
        options.accept_insecure_certs = True
        # Опционально: доверять корпоративным корневым сертификатам
        options.set_preference("security.enterprise_roots.enabled", True)

        service = FirefoxService("geckodriver.exe")
        return webdriver.Firefox(service=service, options=options)

    elif Progid == "MSEdgeHTM":
        from selenium.webdriver.edge.options import Options as EdgeOptions
        from selenium.webdriver.edge.service import Service as EdgeService

        options = EdgeOptions()
        options.accept_insecure_certs = True
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")

        service = EdgeService("msedgedriver.exe")
        return webdriver.Edge(service=service, options=options)

    elif Progid == "IE.HTTP":
        from selenium.webdriver.ie.options import Options as IEOptions
        from selenium.webdriver.ie.service import Service as IEService

        options = IEOptions()
        # IE частично поддерживает этот капабилити:
        options.accept_insecure_certs = True
        # При необходимости:
        # options.ignore_protected_mode_settings = True

        service = IEService("IEDriverServer.exe")
        return webdriver.Ie(service=service, options=options)

    else:
        raise ValueError("Unsupported browser type")
