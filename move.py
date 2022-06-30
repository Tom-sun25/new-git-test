import numpy as np
import  pandas as pd

def move():
    ratings = pd.read_json(r'D:\pycharmproject\move\ratings.json')
    print(ratings)
    #计算相似度矩阵 欧式距离1/1+欧式距离
    simmat = ratings.corr()
    print(ratings.corr())
    login_name ='Michael Henry'
    sim_users = simmat[login_name]
    sim_users = sim_users.drop(login_name)
    sim_users = sim_users[sim_users>0]
    print(sim_users)
    movie_list={}
    for sim_user,sim_score in sim_users.items():
        movies = ratings[sim_user]
        print(movies)
        for movie,score in movies.dropna().items():
            if np.isnan(ratings[login_name][movie]):
                if movie not in movie_list.keys():
                    movie_list[movie]=[[],[]]
                movie_list[movie][0].append(score)
                movie_list[movie][1].append(sim_score)
    #ml = sorted(movie_list.items(),key=lambda x:np.mean(x[1]),reverse=True)
    ml = sorted(movie_list.items(),key=lambda x:np.average(x[1][0],weights=x[1][1]),reverse=True)
    print(np.array(ml)[:, 0])
    print(ml)

if __name__ == '__main__':
    move()
    print("")