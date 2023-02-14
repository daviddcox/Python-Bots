from classes import Scrape
import datetime
import concurrent.futures

run = True
best_buy = Scrape()
amazon = Scrape()
game_stop = Scrape()
walmart = Scrape()
target = Scrape()
status = []

web_list = [('best buy:', "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?acampID=0&c"
             "mp=RMX&irclickid=SPXVn3yeixyLUFQ05-R4sULoUkEV4cR0KXS1zA0&irgwc=1&loc=Narrativ&mpid=376373&ref"
             "=198&skuId=6428324", "(//div[contains(@class, 'fulfillment-add-to-cart-button')])[1]"),
            ('amazon:', "https://www.amazon.com/Xbox-X/dp/B08H75RTZ8/ref=sr_1_1?crid=3BNUIT39L7DVN&dchild=1&keywords=x"
                        "box%2Bseries%2Bx&qid=1616456618&sprefix=xbox%2B%2Caps%2C204&sr=8-1&th=1",
             "(//span[contains(@class, 'a-size-medium a-color-price')])[1]"),
            ('game stop:', "https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x/"
                           "B224744V.h"
                           "tml?view=new&utm_source=rakutenls&utm_medium=affiliate&utm_content=CNET&utm_campaign=10&u"
                           "tm_kx"
                           "confid=tebx5rmj3&cid=afl_10000087&affID=77777&sourceID=0JlRymcP1YU-Iihft1SWNqfifG0_gEmP2w",
             "(//button[contains(@class, 'add-to-cart btn btn-primary ')])[1]"),
            ('walmart:', "https://www.walmart.com/ip/XB1-Xbox-Series-X/443574645?irgwc=1&sourceid=imp_RMYy4u3gyxyLWG%3"
                         "Aw"
                         "Ux0Mo3ZzUkEV4cRsKXS1zA0&veh=aff&wmlspartner=imp_159047&clickid=RMYy4u3gyxy"
                         "LWG%3AwUx0Mo3ZzUkEV4c"
                         "RsKXS1zA0&sharedid=cnet&affiliates_ad_id=565706&campaign_id=9383",
             "(//div[contains(@class, 'prod-blitz-copy-message')])"),
            ('target:', "https://www.target.com/p/xbox-series-x-console/-/A-80790841?clkid=6e3942eaN61ea"
                        "11eba6ba42010a24"
                        "6c43&lnm=81938&afid=CNET%20Media%20Group&ref=tgt_adv_xasd0002",
             "//div[contains(@class, 'h-text-orangeDark')]")]

instance_list = [best_buy, amazon, game_stop, walmart, target]


def run_list(name):
    global status
    name -= 1
    instance_list[name].google(web_list[name][1])
    if web_list[name][0] == 'amazon:':
        instance_list[name].click("//*[text() = 'Xbox Series X']")

    text = instance_list[name].check_available(web_list[name][2])
    status.append(web_list[name][0])
    status.append(text)
    print('')
    print(web_list[name][0])
    print(text)


while run:
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(web_list)) as executor:
        executor.map(run_list, range(len(web_list)))
    print('')
    print(datetime.datetime.now().strftime("%m-%d-%Y %H:%M"))
