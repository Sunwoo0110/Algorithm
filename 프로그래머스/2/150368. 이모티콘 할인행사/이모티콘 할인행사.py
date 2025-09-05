def solution(users, emoticons):
    rates = [10, 20, 30, 40]
    m = len(emoticons)

    disc = [[price*(100-r)//100 for r in rates] for price in emoticons]

    res_plus_cnt, res_price = -1, -1
    disc_choice = [0]*m ## 각 이모티콘 할인율 저장

    def dfs(idx):
        nonlocal res_plus_cnt, res_price

        if idx == m:
            plus_cnt = 0
            price = 0
            
            for need_rate, need_price in users:
                spend = 0
                for i in range(m):
                    if rates[disc_choice[i]] >= need_rate: ## 기준 할인 이상만 구매
                        spend += disc[i][disc_choice[i]]
                if spend >= need_price: ## 기준 금액 넘으면 이모티콘 플러스
                    plus_cnt += 1
                else:
                    price += spend

            ## 조건 우선순위 비교
            if (plus_cnt > res_plus_cnt) or (plus_cnt == res_plus_cnt and price > res_price):
                res_plus_cnt, res_price = plus_cnt, price
            return

        for r in range(4):
            disc_choice[idx] = r
            dfs(idx+1)

    dfs(0)
    return [res_plus_cnt, res_price]

