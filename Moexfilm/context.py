from Moexfilm.core import env
from injector import inject,Injector,Module


class ApplicationContext(Module):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ApplicationContext, cls).__new__(cls)
            cls._instance.config = env
            cls._instance.injector = Injector([cls._instance])
        return cls._instance

    @inject
    def inject(self):
        pass




application_context = ApplicationContext()
