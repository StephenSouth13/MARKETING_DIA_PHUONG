import pandas as pd
import numpy as np

# Tạo dữ liệu mô phỏng lượng khách Metro số 1 theo giờ (Dựa trên dự báo 20 triệu khách/năm)
days = pd.date_range(start='2026-01-01', end='2026-12-31', freq='D')
hours = range(6, 24) # Metro chạy từ 6h đến 24h

data = []
for day in days:
    for hour in hours:
        # Giả lập giờ cao điểm (7-9h và 17-19h)
        if (7 <= hour <= 9) or (17 <= hour <= 19):
            base_pax = np.random.randint(5000, 8000)
        else:
            base_pax = np.random.randint(1000, 3000)
        
        # Giả lập doanh thu thương mại ngầm (Dự báo 0.5$ mỗi khách)
        revenue = base_pax * 0.5 * 25000 # Chuyển sang VNĐ
        
        data.append([day, hour, base_pax, revenue])

df = pd.DataFrame(data, columns=['Ngày', 'Giờ', 'Lượng_Khách', 'Doanh_Thu_Dự_Kiến'])
df.to_csv('HCMC_Underground_Economy_Dataset.csv', index=False)
print("Đã tạo file HCMC_Underground_Economy_Dataset.csv thành công!")