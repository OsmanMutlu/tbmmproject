import scrapy


class MainSpider(scrapy.Spider):
	name = "main"
	def start_requests(self):
		urls = [
			'https://www.tbmm.gov.tr/develop/owa/td_v2.sayfa_yonlendir?v_meclis=1&v_donem=20&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.xpath('//td[@valign]/a/@href').extract()
		thefile = open('test1.txt', 'w')
		#for i in range(0,len(page)-2,2):
		#	thefile.write("%s\n" % page[i])
		for i in page:
			thefile.write("%s\n" % i)
		#self.log(page)