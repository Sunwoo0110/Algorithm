from collections import defaultdict

def solution(fees, records):
    answer = []
    
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    car_dict = defaultdict(int) ## 입출차 기록
    time_dict = defaultdict(int) ## 누적 주차 시간 기록
    fee_dict = defaultdict(int) ## 최종 주차 요금 기록
    
    for record in records:
        time, car_num, tpe = record.split(" ")
        h, m = map(int, time.split(":"))
        min_time = h*60+m
        
        if car_num in car_dict.keys():
            time_dict[car_num] += min_time-car_dict[car_num]
            del car_dict[car_num]
        else:
            car_dict[car_num] = min_time
                
    for key, value in car_dict.items():
        time_dict[key] += 23*60+59-value
    
    time_list = sorted(time_dict)
    
    for car_num in time_list:
        time = time_dict[car_num]
        fee = 0
        
        if time > basic_time:
            fee += basic_fee
            add_fee = ((time-basic_time)//unit_time)*unit_fee if (time-basic_time)%unit_time == 0 else ((time-basic_time)//unit_time + 1)*unit_fee
            fee += add_fee
            
        else:
            fee = basic_fee
        answer.append(fee)
    
    return answer