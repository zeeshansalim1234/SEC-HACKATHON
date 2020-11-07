no_of_users=0
class user_info:  #class for managing all user info


    sums=[]
    friends_preferences=[]
    def __init__(self,name,email,password,dob,loc,bio,pic,school,work,interest,post,friends):

        self.name=name
        self.email=email
        self.password=password
        self.dob=dob
        self.loc=loc
        self.bio=bio
        self.pic=pic
        self.school=school
        self.work=work
        self.interest=interest
        self.post=post
        self.friends=friends


arr=[]
arr.append(user_info(1,2,3,4,5,6,7,8,9,1,5,2))
arr.append(user_info(1,2,3,4,5,6,7,8,9,1,5,2))
print(len(arr))
for i in range(0,len(arr)):

    for j in range(0,len(arr)):

        if(i!=j):

            if(arr[i].loc==arr[j].loc):
                arr[i].sums[j]+=20

            if(arr[i].interest==arr[j].interest):
                arr[i].sums[j]+=10

            elif((arr[i].interest in arr[j].interest )or(arr[j].interest in arr[i].interest)):
                arr[i].sums[j]+=5

            list_set=set(arr[i].friends)
            intersection= list_set.intersection(arr[j].friends)
            intersection_list=list(intersection)
            arr[i].sums[j]+=10*(len(intersection_list))

    arr[i].friends_preferences=[i[0] for i in sorted(enumerate(arr[i].sums), key=lambda k: k[1], reverse=True)]



