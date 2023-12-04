from Moexfilm.core import env


class ApplicationContext:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ApplicationContext, cls).__new__(cls)
            cls._instance.config = env
        return cls._instance


application_context = ApplicationContext()
