# Определение браузера по умолчанию в Windows  
1) Получает данные о браузере по умолчанию из реестра
> get_default_browser() -> str (ProgId)
2) Подбирает подходящий selenium драйвер по данным с реестра   
> get_driver_by_browser(ProgId) -> driver
