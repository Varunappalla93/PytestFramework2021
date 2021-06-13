from configparser import ConfigParser

# config=ConfigParser()
#
# config.read("config.ini")
#
# print(config.get("locator-login","username"))  # //input[@id='identifierId']
#
# print(config.get("basic info","implicit.wait")) # 10


def readconfig(section,key):
    config = ConfigParser()
    config.read("C:\\Users\\VARUN\\Desktop\\Varun_Personal\\POM_Framework_Arora\\ConfigurationData\\config.ini")
    return config.get(section,key)


# c=readconfig("locators","username_xpath")
# print(c)        # //input[@id='identifierId'

