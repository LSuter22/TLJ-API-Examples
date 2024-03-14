import requests

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
URL = "http://45.131.138.38:7043/GuestCardBluetooth"
Data = {
    'cer': '72DBA4B307C86F7B',
    'room': "4BD9D8E19FE977A3B499C50DFF0C7689",
    'EMailAddr': "51A6F6892C1DEC5926B4CD4142AE0051",
    'BeginTime': '71292B73C7E8D9077401D5B336DD0D56226DE7D2FFD27CA6E521E77B73BCAA41',
    'EndTime': 'DB999B49EFCEBB7FEA04DD909A21F7DB226DE7D2FFD27CA6E521E77B73BCAA41',
    'CheckInMode': 'new'
}

response = requests.post(URL, data=Data)
print(response.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



