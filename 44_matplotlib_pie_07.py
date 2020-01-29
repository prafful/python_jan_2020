import matplotlib.pyplot as plt

socialmedia = ['facebook', 'twitter', 'youtube', 'instagram', 'linkedin']
views = [444, 542, 888, 1500, 100]
explodeone = [0 ,0 , 0.1, 0, 0]

plt.pie(views, labels=socialmedia, 
                explode=explodeone, 
                autopct='%1.1f%%', 
                wedgeprops={'width':0.8})

plt.show()