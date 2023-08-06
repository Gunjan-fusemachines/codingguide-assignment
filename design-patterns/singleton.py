class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._load_configuration()
        return cls._instance

    def _load_configuration(self):
        # Simulating loading configuration from a file
        self.settings = {}
        with open('design-patterns/config.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key)

# Client code
def main():
    config_manager1 = ConfigurationManager()
    config_manager2 = ConfigurationManager()

    print("Config manager 1 settings:")
    print(config_manager1.get_setting('database_url'))
    print(config_manager1.get_setting('api_key'))

    print("\nConfig manager 2 settings:")
    print(config_manager2.get_setting('database_url'))
    print(config_manager2.get_setting('api_key'))

    print("\nAre config managers the same instance?")
    print(config_manager1 is config_manager2)

if __name__ == "__main__":
    main()
