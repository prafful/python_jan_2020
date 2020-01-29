import matplotlib.pyplot as plt


facebook_views = [127, 128, 554, 658, 958, 500, 9999, 525, 555, 666, 888, 777, 4444, 11001]
rangebin = [0, 1000,15000]

plt.hist(facebook_views, rangebin, label="Views Distribution")

#label
plt.xlabel('Day Number')
plt.ylabel('Views')

#legend
plt.legend(loc="lower right")
#title
plt.title('Channel Views Distribution In A Week')
#limit of x and y axis
#plt.xlim(1,14)
#plt.ylim(100,1000)
plt.grid(color='y', linestyle=':')

#save chart as an image
#plt.savefig("Channel_Views.png", dpi=300, facecolor='y')

plt.show()