import requests
from bs4 import BeautifulSoup
import json

class pccSpyder():
	def __init__(self):
		pass
		
	def get_data(self, keyword):
		url = "http://web.pcc.gov.tw/tps/pss/tender.do"
		params = {"method": "search",
				"searchMode": "common",
				"searchType": "basic",
				"searchMethod": "true",
				"tenderUpdate": "",
				"searchTarget": "",
				"orgName": "",
				"orgId": "",
				"hid_1": "1",
				"tenderName": keyword,
				"tenderId": "",
				"tenderType": "tenderDeclaration",
				"tenderWay": "1,2,3,4,5,6,7,10,12",
				"tenderDateRadio": "on",
				"tenderStartDateStr": "108/04/06",
				"tenderEndDateStr": "108/04/12",
				"tenderStartDate": "108/04/12",
				"tenderEndDate": "108/04/12",
				"isSpdt": "Y",
				"proctrgCate": "",
				"btnQuery": "查詢",
				"hadUpdated": ""}
				
		res = requests.get(url, params=params)
		soup = BeautifulSoup(res.content, "lxml")
		print_area = soup.find("div", id="print_area")
		item = print_area.find_all("tr")
		title = print_area.find("tr").find_all("td")
		title_list = []
		for i in range(len(title)):
			title_list.append(title[i].text)
		data = []

		for i in range(len(item)-1):
			temp = {}
			iitem = print_area.find_all("tr")[i].find_all("td")
			for j in range(len(iitem)-1):
				print(title_list[j], end=":")
				temp[title_list[j]] = iitem[j].text.strip().replace("\t", "").replace("\r\n", "").replace("\n\n", "")
				print(iitem[j].text.strip().replace("\t", "").replace("\r\n", "").replace("\n\n", ""))
			data.append(temp)

		data_json = json.dumps(data)
		
		return data_json
		
if __name__ == "__main__":
	pcc = pccSpyder()
	keyword = input("Please enter keyword:")
	data = pcc.get_data(keyword)
	print(data)