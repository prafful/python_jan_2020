import matplotlib.pyplot as plt


facebook_views = [127, 128, 254, 658, 958, 500, 9999, 225, 555, 666, 888, 777, 444, 11001]
youtube_views = [225, 555, 666, 888, 777, 444, 11001, 111, 222, 333, 444, 222, 555, 8888]
twitter_views = [111, 222, 333, 444, 222, 555, 8888, 127, 128, 254, 658, 958, 500, 9999]

days = range(1,15)

plt.scatter(days, facebook_views, label='Facebook Views',color='r', marker='D' )
plt.scatter(days, youtube_views, label='Youtube Views',color='g', marker='s')
plt.plot(days, twitter_views, label='Twitter Views', color='b', marker='o')

#label
plt.xlabel('Day Number')
plt.ylabel('Views')

#legend
plt.legend(loc="upper left")
#title
plt.title('Channel Views In A Week')
#limit of x and y axis
#plt.xlim(1,14)
#plt.ylim(100,1000)
plt.grid(color='y', linestyle=':')

#save chart as an image
#plt.savefig("Channel_Views.png", dpi=300, facecolor='y')

plt.show()