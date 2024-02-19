from datetime import datetime, timedelta

# 定義女士們的月經週期
menstrual_cycles = [30, 41, 28, 27, 36, 33, 28, 30, 35, 21, 25, 31]

# 設定起始日期和結束日期
start_date = datetime(2023, 11, 24)
end_date = datetime(2024, 2, 23)

# 計算每位女士的下一個週期開始日期
next_period_dates = []
for cycle in menstrual_cycles:
    next_period_date = start_date + timedelta(days=cycle)
    next_period_dates.append(next_period_date)

# 檢查每一天有多少女士經歷了最多3次月經週期
counts = [0] * len(menstrual_cycles)
current_date = start_date
while current_date <= end_date:
    for i, next_date in enumerate(next_period_dates):
        if current_date >= next_date:
            counts[i] += 1
            next_period_dates[i] = next_date + timedelta(days=menstrual_cycles[i])
    current_date += timedelta(days=1)

# 找到最小的開始日期，使得至少9位女士經歷最多3次月經週期
min_start_date = None
for i, count in enumerate(counts):
    if count >= 3 and counts.count(count) >= 9:
        if min_start_date is None or next_period_dates[i] < min_start_date:
            min_start_date = next_period_dates[i]

print("最小的開始日期是:", min_start_date)
