import pandas as pd

# Load dữ liệu
df = pd.read_csv("retail_cluster_simulation.csv")

# Tổng doanh thu theo mô hình
summary = df.groupby("Model")["Revenue_million"].sum()
print(summary)

# So sánh trung bình mỗi cửa hàng
avg_store = df.groupby(["Model","Store"])["Revenue_million"].mean()
print(avg_store)

import matplotlib.pyplot as plt

summary.plot(kind="bar")
plt.title("So sánh doanh thu: Cụm KHÁC hãng vs CÙNG hãng")
plt.ylabel("Doanh thu (triệu VND)")
plt.show()

