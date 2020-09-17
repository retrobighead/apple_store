
class AppleStore: # お店
    def __init__(self, apple_price=100): # コンストラクタ: クラスが実体化（インスタンス化）されるときにはじめに実行される
        self.apple_price = apple_price # クラス変数

    def buy_apple(self, apple_num, money): # クラスメソッド : りんごを買う
        total_price = apple_num * self.apple_price

        if money >= total_price:
            bought_apple_num = apple_num
            change = money - total_price
        else:
            bought_apple_num = 0
            change = money

        return bought_apple_num, change

apple_num = int(input("買いたい個数: "))
money = 500

apple_store = AppleStore()

a, b = apple_store.buy_apple(apple_num, money)

print("買うことができたりんごの数: " + str(a))
print("残りの所持金: " + str(b))