import matplotlib.pyplot as plt
""" plt.xlabel("x축")
plt.xlabel("y축")

plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")
#solid 픽셀크기, 간격
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (4, 2)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (18, 1)), label="PData(km)")
#색
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="g", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="b", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="lime", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#1f77b4", label="Value(m)")
#모양 설정 
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, dash_capstyle="round", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", label="Value(m)") 
#마커지정
                             	# c=cyan d=diamond / c=색깔 , d= 모형
plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "go-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "co--", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")
#marker 파라메터 사용
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$test$", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$y$", label="PData(km)")
#그래프 영역 채우기
xdata = [2, 3, 6, 7, 10]
ydata = [1, 4, 5, 8, 9]
y1data = [2, 4, 6, 8, 10]

plt.plot(xdata, ydata)
plt.xlabel("x_data")
plt.plot("y_data")

#세로 축 채우기
plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
plt.fill_between(xdata[1:4], ydata[1:4], alpha=1)
plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.3)
#가로 축 채우기 
plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
plt.fill_betweenx(ydata[1:3], xdata[2:4], alpha=0.3)

plt.plot([1, 4, 5, 6, 9],[2, 3, 6, 7, 10])
plt.plot(xdata, ydata)

#두 선간 채우기
plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3],color="C2", alpha=0.5)
#영역 색 채우기 x축 / y축
plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)
plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 5.5, 3.1], alpha=1)
 """
 
#배경설정
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic_val = {"x_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.plot("x_data", "y_data", data=dic_val, label="Value(m)")
#plt.plot([1,4,5,9],[2,3,8,10])
plt.xlabel("x_data")
plt.ylabel("y_data")

#배경 그리드 
#plt.grid()
#plt.grid(axis="x")
#plt.grid(axis="x")

plt.grid(color="g", alpha=0.5, linestyle="-")
plt.grid(color="g", alpha=0.5, linestyle=".")

plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
plt.grid(axis="x", color="r", alpha=0.3, linestyle="-")
plt.grid(axis="y", color="g", alpha=0.5, linestyle="-.")

#눈금표시 
plt.xticks()
plt.yticks()

plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10])

plt.xticks([1,3,5,7,9,11])
plt.yticks([2,4,6,8,10])
#라벨 지정
plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
#눈금 안쪽 / 바깥쪽 
plt.tick_params(axis="x", direction="in")
#plt.tick_params(axis="x", direction="out")
plt.tick_params(axis="y", direction="in")

plt.show() """

#막대그래프
x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["C2", "lime", "#57ADCC"]

plt.bar(x_years, y_data)
#색지정 
plt.bar(x_years, y_data, color="g")
plt.bar(x_years, y_data, color="C7")
plt.bar(x_years, y_data, color="#57ADCC")
#개별 색 지정
plt.bar(x_years, y_data, color=clr)
#너비
plt.bar(x_years, y_data, color=clr, align="edge", width=2)
plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
plt.bar(x_years, y_data, color=clr, align="edge", width=0.1)
#막대 위치 선정 
plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", width=0.5)
# 라인 색 선택
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="C2", width=0.5)
# 테두리 라인 설정
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=2)
#축 지표 설정 
plt.xticks(x_years)
plt.yticks(y_data, y_data)
plt.yticks([100, 200, 300, 400, 500, 600, 900])
#수평, 가로 그래프
plt.barh(x_years, y_data)
#그래프 설정 
#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

plt.show()

