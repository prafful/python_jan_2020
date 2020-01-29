import matplotlib.pyplot as plt


views = [127, 128, 254, 658, 1100, 500, 999]
days = range(1,8)

max_views = max(views)
index_of_max_views = days[views.index(max_views)]

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

#annotation
plt.annotate('Maximum Views', 
                xy=(index_of_max_views, max_views), 
                xytext=(2,900) , 
                arrowprops = dict(facecolor='b', shrink=0.1))




plt.show()

