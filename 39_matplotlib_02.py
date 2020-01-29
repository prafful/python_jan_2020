import matplotlib.pyplot as plt


views = [127, 128, 254, 658, 958, 500, 999]
days = range(1,8)

#x,y
#label is required for legend

plt.plot(days, views, label='Channel Views', color='r', marker='D', markerfacecolor='b', linestyle='-.', linewidth=2)

#label
plt.xlabel('Day Number')
plt.ylabel('Views')

#legend
plt.legend(loc="upper left")
#title
plt.title('Channel Views In A Week')






plt.show()

