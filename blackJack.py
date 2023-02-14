import pydirectinput as pd
import pyautogui as pt
import time


num2 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/2.jpg'
num3 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/3.jpg'
num4 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/4.jpg'
num5 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/5.jpg'
num6 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/6.jpg'
num7 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/7.jpg'
num8 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/8.jpg'
num9 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/9.jpg'
num10 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/10.jpg'
num11 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/11.jpg'
num12 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/12.jpg'
num13 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/13.jpg'
num14 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/14.jpg'
num15 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/15.jpg'
num16 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/16.jpg'
num17 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/17.jpg'
num18 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/18.jpg'
num19 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/19.jpg'
num20 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/20.jpg'
num21 = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/21.jpg'
player = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/Player.jpg'
dealer = 'C:/Users/allen/PycharmProjects/bot/blackJackNumbers/Dealer.jpg'

num_list = [num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14,
            num15, num16, num17, num18, num19, num20, num21]
run1 = True
run2 = True


def hit():
    print('hit')
    x, y = (pt.locateCenterOnScreen('C:/Users/allen/PycharmProjects/bot/blackJackNumbers/hit.jpg',
                                    grayscale=True, confidence=.7))
    pd.moveTo(x, y)
    pd.click()


def stand():
    print('stand')
    x, y = (pt.locateCenterOnScreen('C:/Users/allen/PycharmProjects/bot/blackJackNumbers/stand.jpg',
                                    grayscale=True, confidence=.7))
    pd.moveTo(x, y)
    pd.click()
    run = True




def main():
    while run1:
        pd.keyDown('alt')
        pd.press('tab')
        pd.keyUp('alt')
        if pt.locateCenterOnScreen('C:/Users/allen/PycharmProjects/bot/blackJackNumbers/menu.jpg',
                                   grayscale=True, confidence=.95) is not None:
            x3, y3 = pt.locateCenterOnScreen('C:/Users/allen/PycharmProjects/bot/blackJackNumbers/deal.jpg',
                                             grayscale=True, confidence=.95)
            pd.moveTo(x3, y3)
            pd.click()
            time.sleep(2)
        x, y = (pt.locateCenterOnScreen('C:/Users/allen/PycharmProjects/bot/blackJackNumbers/Player.jpg',
                                        grayscale=True, confidence=.7))
        x1, y1 = (pt.locateCenterOnScreen('C:/Users/allen/PycharmProjects/bot/blackJackNumbers/Dealer.jpg',
                                          grayscale=True, confidence=.7))
        player_region = (x-169, y-49, 120, 100)
        dealer_region = (x1-169, y1-49, 120, 100)
        while run2:
            if pt.locateCenterOnScreen('C:/Users/allen/PycharmProjects/bot/blackJackNumbers/win.jpg',
                                       grayscale=True, confidence=.95) is not None:
                time.sleep(3)
            if pt.locateCenterOnScreen('C:/Users/allen/PycharmProjects/bot/blackJackNumbers/menu.jpg',
                                       grayscale=True, confidence=.95) is not None:
                x3, y3 = pt.locateCenterOnScreen('C:/Users/allen/PycharmProjects/bot/blackJackNumbers/deal.jpg',
                                                 grayscale=True, confidence=.95)
                pd.moveTo(x3, y3)
                pd.click()
                time.sleep(2)
            # Finds number of player and dealer
            for i in num_list:
                if pt.locateCenterOnScreen(i, grayscale=True, region=player_region, confidence=.95) is not None:
                    player_number = num_list.index(i) + 2
            for i in num_list:
                if pt.locateCenterOnScreen(i, grayscale=True, region=dealer_region, confidence=.95) is not None:
                    dealer_number = num_list.index(i) + 2

            print(player_number)
            print(dealer_number)
            if player_number == 2 or player_number == 3 or player_number == 4 or player_number == 5 or \
                    player_number == 6 or player_number == 7:
                hit()
            elif player_number == 8:
                if dealer_number == 5 or dealer_number == 6:
                    hit()
                else:
                    hit()

            elif player_number == 9:
                if dealer_number == 2 or dealer_number == 3 or dealer_number == 5 or dealer_number == 6:
                    hit()
                else:
                    hit()

            elif player_number == 10:
                if dealer_number == 10 or dealer_number == 11:
                    hit()
                else:
                    hit()

            elif player_number == 11:
                hit()

            elif player_number == 12:
                if dealer_number == 4 or dealer_number == 5 or dealer_number == 6:
                    stand()
                else:
                    hit()

            elif player_number == 13:
                if dealer_number == 2 or dealer_number == 3 or dealer_number == 4 or dealer_number == 5 or dealer_number\
                        == 6:
                    stand()
                else:
                    hit()

            elif player_number == 14:
                if dealer_number == 2 or dealer_number == 3 or dealer_number == 4 or dealer_number == 5 or dealer_number \
                        == 6:
                    stand()
                else:
                    hit()

            elif player_number == 15:
                if dealer_number == 2 or dealer_number == 3 or dealer_number == 4 or dealer_number == 5 or dealer_number\
                        == 6:
                    stand()
                else:
                    hit()

            elif player_number == 16:
                if dealer_number == 2 or dealer_number == 3 or dealer_number == 4 or dealer_number == 5 or dealer_number\
                        == 6:
                    stand()
                else:
                    hit()

            elif player_number == 17:
                stand()

            elif player_number == 18:
                stand()

            elif player_number == 19:
                stand()

            elif player_number == 20:
                stand()

            elif player_number == 21:
                stand()


if __name__ == "__main__":
    main()
